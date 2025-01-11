# SudanChapter_AnalyzeHealthcareAccessibility - Data Collection


## Socioeconomic and Demographic Data:   
Income levels, education, age distribution, and population density  
[HDX : Sudan - Human Development Indicators ](https://data.humdata.org/dataset/hdro-data-for-sudan)  

1. Human Development Indicators for Sudan  
    data: [hdro_indicators_sdn.csv](./demographics/hdro_indicators_sdn.csv)  
    source: [United Nation Development Program](https://data.humdata.org/dataset/hdro-data-for-sudan)  
    ![qucik link](./demographics/screenshots/Screenshot%202025-01-03%20at%2017-18-12%20Sudan%20-%20Human%20Development%20Indicators%20-%20Humanitarian%20Data%20Exchange.png)  

2. Aggregated Human Development Indicators for SudanCSV  
    data: [hdro_indicators_aggregates_sdn.csv](./demographics/hdro_indicators_aggregates_sdn.csv)  
    source: [United Nation Development Program](https://data.humdata.org/dataset/hdro-data-for-sudan)   

3. Sudan - Economic, Social, Environmental, Health, Education, Development and Energy - World Bank  
    data: (./demographics/indicators_sdn.csv)  
    source: world bank  
    source link: https://data.humdata.org/dataset/world-bank-combined-indicators-for-sudan  
    ![quick charts](./demographics/screenshots/Screenshot%202025-01-03%20at%2017-11-15%20Sudan%20-%20Economic%20Social%20Environmental%20Health%20Education%20Development%20and%20Energy%20-%20Humanitarian%20Data%20Exchange.png)  
    

4. Sudan Gender   
    world-bank-gender-indicators-for-sudan    
    data: [gender_sdn.csv](./demographics/gender_sdn.csv)   
    source: [world bank](https://data.humdata.org/dataset/world-bank-gender-indicators-for-sudan)   
    ![quick charts](./demographics/screenshots/Screenshot%202025-01-03%20at%2017-07-30%20Sudan%20-%20Gender%20-%20Humanitarian%20Data%20Exchange.png)   

5. Sudan Displacement Situation (Countrywide) - IDPs [IOM DTM]   
    data: [dtm_sdn_smu-bi-weekly-13-_-17122024_v02_public_hdx.xlsx](./demographics/dtm_sdn_smu-bi-weekly-13-_-17122024_v02_public_hdx.xlsx)  
    source: [UN Migration, international orgranization for migration](https://data.humdata.org/dataset/sudan-displacement-situation-countrywide-idps-iom-dtm)  

6. World Population Prospects (2024)  
    data (full): [WPP2024_GEN_F01_DEMOGRAPHIC_INDICATORS.xlsx](./demographics/WPP2024_GEN_F01_DEMOGRAPHIC_INDICATORS.xlsx)  
    data (compact): [WPP2024_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT.xlsx](./demographics/WPP2024_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT.xlsx)  

7. Sudan - Education Indicators   
    data : [SDG 4 Global and Thematic data](./demographics/sdg_data_sdn.csv)  
    data : [SDG 4 Global and Thematic indicator data](./demographics/sdg_indicatorlist_sdn.csv)   
    Data : primary-secondary-enrollment-completion-rates  
    source: UNESCO 
    source link: https://data.humdata.org/dataset/unesco-data-for-sudan
    ![quick chart](./demographics/screenshots/Screenshot%202025-01-03%20at%2018-01-41%20Sudan%20-%20Education%20Indicators%20-%20Humanitarian%20Data%20Exchange.png)  
    Source : Our World  
    Source Link : https://ourworldindata.org/global-education#key-insights  

## Geographic  
1. Sudan Health Facilities
    * data -points: [hotosm_sdn_health_facilities_points_shp.zip](./geographic/hotosm_sdn_health_facilities_points_shp.zip)  
    * data -polygons: [hotosm_sdn_health_facilities_polygons_shp.zip](hotosm_sdn_health_facilities_polygons_shp.zip)   
    * source: [Humanitarian OpenStreetMap Team - open street map - ESRI Shapefile](https://data.humdata.org/dataset/hotosm_sdn_health_facilities)  
    ![quick chart](./geographic/screenshot/Screenshot%202025-01-03%20at%2017-36-44%20Sudan%20Health%20Facilities%20(OpenStreetMap%20Export)%20-%20Humanitarian%20Data%20Exchange.png) _(excluded from merging due to overlap with data collected for other segments)_
2. Geometric data of Sudan's administrative areas on 3 levels (states, districts, district subdivisions)
    * data : [GADM Spatial Database by Country](https://gadm.org/download_country.html)
    * date range : -
    * granularity : state, district and district subdivison level
4. Satellite data on vegetation, water content and water body changes (NDVI, NDWI) on district subdivision level (state >> district >> district subdivision)
    * data : [Copernicus Sentinel-2 Mission](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-2)
    * date range : 07/2015 - 01/2025
    * granularity : district subdivison level
5. Aggregated weather data by date from OpenWeatherMap (precipitation, humidity, temperature, etc.)
    * data : [OpenWeatherMap One Call API 3.0 - Daily Aggregation](https://openweathermap.org/api/one-call-3#history_daily_aggregation)
    * date range : 01/2022 - 12/2024
    * granularity : state level, for one day per week
6. Infrastructure data from OpenStreetMap (highways, railways, waterways)
    * data : [OpenStreetMap API](https://wiki.openstreetmap.org/wiki/API_v0.6)
    * date range : -
    * granularity : district level
7. Sudan's major cities' location from Simplemaps by state
    * data : [Simplemaps database](https://simplemaps.com/data/world-cities)
    * date range : -
    * granularity : state level
   
## Healthcare
## Sources for Healthcare Data in Sudan

This document provides an overview of the data sources referenced for compiling the healthcare infrastructure and personnel distribution in Sudan.

### Key Data Sources

1. WHO Sudan Country Profile
   - Website: [WHO Sudan Country Page](https://data.who.int/countries/729)
   - Provides general healthcare statistics for Sudan, including health expenditure and personnel ratios.

2. World Bank Public Expenditure Reviews (PER)
   - Source: World Bank Reports on Healthcare Spending
   - Insights into government health expenditure, fiscal allocations, and workforce financing.

3. Sudan National Health Policy 2017-2030
   - Document hosted on: [WHO National Planning Cycles](https://extranet.who.int/countryplanningcycles/sites/default/files/public_file_rep/SDN_Sudan_National-Health%20Policy_2017-2030.pdf)
   - Contains strategic health workforce planning, hospital distribution, and geographic healthcare disparities.

4. Statista
   - Website: [Statista Health Metrics for Sudan](https://www.statista.com/outlook/co/health-indicators/sudan)
   - Offers up-to-date statistics on healthcare personnel density, hospital beds, and smoking rates.

5. AP News on Cholera Cases (2024)
   - Article: [Fast-rising cholera cases across war-torn Sudan](https://apnews.com/article/b204925d3398e08aff6761b21d0937f1)
   - Reports on current public health crises affecting healthcare infrastructure.

6. Doctors Without Borders
   - Article: [Health system on the verge of collapse in Khartoum](https://www.doctorswithoutborders.org/latest/sudan-health-system-verge-collapse-khartoum)
   - Information on operational healthcare facilities and conflict impact.

7. Regional WHO Public Health Crisis Updates
   - Statement: [WHO Regional Director on Health Crisis in Sudan](https://www.emro.who.int/media/news/regional-director-statement-on-the-health-crisis-in-sudan.html)
   - Context on conflict-related healthcare system breakdown and infrastructure damage.

8. Reuters Health Reports on Sudan
   - Article: [Mass starvation and healthcare collapse risk](https://www.reuters.com/world/africa/very-real-risk-mass-starvation-some-regions-sudan-who-2024-06-12)
   - Current impact of political and economic instability on Sudan’s healthcare workforce.

9. Macrotrends
   - Website: [Sudan Healthcare Spending Trends](https://www.macrotrends.net/global-metrics/countries/SDN/sudan/healthcare-spending)
   - Historical and current healthcare expenditure data.
  
## Historical Context Data:

1.) Conflict Information Dataset:
    - [https://github.com/OmdenaAI/SudanChapter_AnalyzeHealthcareAccessibility/blob/main/02_Data_collection/historical_context/conflict_data_sdn.csv](url)

2.) Alternative Conflict Information Dataset:
    -[https://github.com/OmdenaAI/SudanChapter_AnalyzeHealthcareAccessibility/blob/main/02_Data_collection/historical_context/gedevents-2025-01-04.csv](url)

3.) Historical Economic Indices in Sudan
    -[https://github.com/OmdenaAI/SudanChapter_AnalyzeHealthcareAccessibility/blob/main/02_Data_collection/historical_context/deflators_sdn.csv](url)

4.) Historical Health Indicator in Sudan:
    -[https://github.com/OmdenaAI/SudanChapter_AnalyzeHealthcareAccessibility/blob/main/02_Data_collection/historical_context/historical_health_indicators_sdn.csv](url)

5.) Historical Food Security Data:
    - [https://github.com/OmdenaAI/SudanChapter_AnalyzeHealthcareAccessibility/blob/main/02_Data_collection/historical_context/suite-of-food-security-indicators_sdn.csv](url)

6.) Refugee Information:
    - [https://github.com/OmdenaAI/SudanChapter_AnalyzeHealthcareAccessibility/blob/main/02_Data_collection/historical_context/statistic_id1232812_african-countries-hosting-the-most-refugees-2023.xlsx](url)

7.) Life Expectancy at Birth in Sudan 2022:
    - [https://github.com/OmdenaAI/SudanChapter_AnalyzeHealthcareAccessibility/blob/main/02_Data_collection/historical_context/statistic_id971229_life-expectancy-at-birth-in-sudan-2022-by-gender.xlsx](url)

8.) Sudanese Civil War Mortalities:
    - [https://github.com/OmdenaAI/SudanChapter_AnalyzeHealthcareAccessibility/blob/main/02_Data_collection/historical_context/Sudanese_War_Mortalities.xlsx](url)
