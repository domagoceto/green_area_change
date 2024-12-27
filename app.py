import ee
import geemap
from flask import Flask, render_template, request
import pandas as pd

# GEE kimlik doğrulama ve başlatma
project_id = 'ee-turelhaticezehra'
ee.Initialize(project=project_id)

# CSV dosyasını yükle
file_path = 'ndvi_results_bartin_il_ve_ilce.csv'
df = pd.read_csv(file_path)

# Flask uygulamasını başlatma
app = Flask(__name__)

def calculate_green_area_change(start_year, end_year, ilce):
    start_data = df[(df['year'] == start_year) & (df['district'] == ilce)]
    end_data = df[(df['year'] == end_year) & (df['district'] == ilce)]

    if not start_data.empty and not end_data.empty:
        start_area = start_data['total_green_area_ha'].values[0]
        end_area = end_data['total_green_area_ha'].values[0]
        
        area_change = end_area - start_area
        
        if start_area > 0:
            percentage_change = (area_change / start_area) * 100
        else:
            percentage_change = 0
        
        return start_area, end_area, area_change, percentage_change
    else:
        return None, None, None, None


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        il = request.form['il']
        ilce = request.form['ilce']
        
        try:
            start_year = int(request.form['start_year'])
            end_year = int(request.form['end_year'])
        except ValueError:
            return "Yıl verileri geçersiz."

        bartin = ee.FeatureCollection("FAO/GAUL/2015/level1").filter(ee.Filter.eq('ADM1_NAME', il))

        # İlçe seçildiğinde sadece ilçe sınırlarını ekleyelim
        if ilce != "Toplam":
            ilce_sinirlar = ee.FeatureCollection("FAO/GAUL/2015/level2") \
                .filter(ee.Filter.eq('ADM2_NAME', ilce)) \
                .filter(ee.Filter.eq('ADM1_NAME', il))  # Bartın ili ile eşleşiyor
            bartin = ilce_sinirlar  # Sadece ilçe sınırlarını kullanıyoruz
        else:
            ilce_sinirlar = bartin  # Toplam için il sınırlarını kullanıyoruz

        start_date = f'{start_year}-06-01'
        end_date = f'{end_year}-09-30'

        def get_ndvi(start_date, end_date):
            sentinel_collection = ee.ImageCollection("COPERNICUS/S2_HARMONIZED") \
                .filterBounds(bartin) \
                .filterDate(start_date, end_date) \
                .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10))

            if sentinel_collection.size().getInfo() == 0:
                return None

            sentinel_mosaic = sentinel_collection.median().clip(bartin)

            red = sentinel_mosaic.select('B4')
            nir = sentinel_mosaic.select('B8')
            ndvi = nir.subtract(red).divide(nir.add(red)).rename('NDVI')
            
            return ndvi

        # NDVI hesapla
        ndvi_start = get_ndvi(f'{start_year}-06-01', f'{start_year}-09-30')
        ndvi_end = get_ndvi(f'{end_year}-06-01', f'{end_year}-09-30')

        if ndvi_start is None or ndvi_end is None:
            return "Seçilen tarihlerde veri bulunamadı."

        # Yeşil alan değişimini hesapla
        ndvi_diff = ndvi_end.subtract(ndvi_start).rename('NDVI_change')

        # Artan ve azalan alanları işaretle
        green_area_change = ndvi_diff.gt(0.2).multiply(ee.Image(1)).add(ndvi_diff.lt(-0.2).multiply(ee.Image(-1)))  # Yeşil artış ve kırmızı azalış birleştirildi

        # Web haritası oluşturma
        Map = geemap.Map()
        Map.centerObject(bartin, 9)
        Map.addLayer(bartin, {'color': 'FFFFFF'}, "Bartın Ili")

        # Yeşil alan değişimlerini tek bir katmanda gösterme (Yeşil artış ve kırmızı azalış)
        Map.addLayer(green_area_change, {'min': -1, 'max': 1, 'palette': ['red', 'white', 'green']}, "Yeşil Alan Değişimi")

        # Yüzde değişimi hesapla
        start_area, end_area, area_change, percentage_change = calculate_green_area_change(start_year, end_year, ilce)

        # Yüzde değişim değeri sayıya dönüştürülüyor
        if percentage_change is not None:
            try:
                percentage_change = float(percentage_change)
            except ValueError:
                percentage_change = 0  # Geçersiz veri durumunda 0 olarak kabul edebiliriz.
        
        # Sayıları dört basamağa yuvarlamak
        start_area = "{:.4f}".format(start_area)
        end_area = "{:.4f}".format(end_area)
        area_change = "{:.4f}".format(area_change)
        percentage_change = "{:.4f}".format(percentage_change)

        # HTML çıktısını oluşturma
        map_html = Map.to_html()

        if start_area is not None:
            return render_template('index.html', map_html=map_html, percentage_change=percentage_change,
                                   start_area=start_area, end_area=end_area, area_change=area_change,
                                   start_year=start_year, end_year=end_year)
        else:
            return render_template('index.html', map_html=map_html, percentage_change="Veri bulunamadı")

    return render_template('index.html', map_html='', percentage_change=None)



if __name__ == '__main__':
    app.run(debug=True)
