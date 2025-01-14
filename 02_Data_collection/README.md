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

## Disease Surveillance Data:
Overview: Data collected for disease surveillance was partitioned into two separate CSV files based on the data they represented. Data representing the count of individual cases and deaths for each disease condition were collected in the combined_2018_2019_2024. The data on the disease indicators of the various disease conditions were collected into the disease_indicators CSV file. 
## 1.	Sudan disease counts dataset (combined_2018_2019_2024.csv)

### Description:
The Sudan Disease Counts dataset provides vital data for understanding the epidemiology of various disease conditions nationwide. It includes information on the total number of reported cases and deaths for each disease, organized by state and year. 
Note:	The 2018 dataset did not have reports on “deaths”; therefore, we provided death cases for the 2019 and 2024 datasets. The Heart_Storkes_Cummulative data reported in 2024 only recorded values for the Northern and Red Sea states, delineating other rows of zero values, and were consequently removed. The two observations for the Heart_Storkes_Cummulative condition were labeled as “other” in the 2024 dataset. Also, the disease cases reported for Cholera may not be accurate since cholera-prone states such as Kassala, Northern, and Red Sea recorded zero cholera cases.

### Key Features:
States: Represents the geographic regions within Sudan where the data was collected.
Year: Covers 2018, 2019, and 2024, providing a multi-year perspective on disease trends.
Disease: Details specific diseases tracked during the surveillance period.
Cases: Indicates the number of confirmed cases for each disease condition.
Deaths: Records the corresponding fatalities attributed to each disease.
File name: combined_2018_2019_2024.csv

### Sources: 
2018_prevalence_of_diseases_outpatient_clinics_per_state: https://data.humdata.org/dataset/300f9677-da29-4698-bb3c-bc3331b254d1/resource/6c1fff73-a418-4f2c-                                                                 86ca-748019180501/download/2018_prevalence_of_diseases_outpatient_clinics_per_state.xlsx
Sudan-disease-outbreaks-2019: https://data.humdata.org/dataset/33ea8b09-7501-46d2-89b1-8376a1d8834f/resource/b9465fc1-15d4-462e-91df-        
                              2f2c39ee5cc3/download/sudan-disease-outbreaks-2019.xlsx
Sudan_disease_2024:             
    https://app.powerbi.com/viewr=eyJrIjoiZDdhYjczYmItMmU1My00OGRiLWIxMTUtM2VjZjg4YjE5ZmNlIiwidCI6ImIzZTVkYjVlLTI5NDQtNDgzNy05OWY1LTc0ODhhY2U1NDMxOSIsImMiOjh9

## 2.	Disease indicator dataset (disease_indicators.csv)

### Description: 
The Disease Indicator Dataset provides essential health metrics for monitoring and evaluating the prevalence and impact of several diseases in Sudan. The dataset combines confirmed case counts and estimated mortality rates, providing a comprehensive overview of disease trends and their variability across different years. It includes metadata for contextual information such as the region, country, and dimensions of interest, making it valuable for surveillance and public health planning.
Note:	Two observations (rows 486 and 489) showed similar values of 7 years difference for the period of data collection (YEAR (DISPLAY), STARTYEAR, ENDYEAR) compared to the remaining data set. 

### Key Features:
Indicators Include metrics such as:
GHO (CODE) and GHO (DISPLAY) columns in the dataset reference specific health indicators tracked within the GHO, such as the number of confirmed malaria cases or the estimated malaria mortality rate. The GHO (URL) column provides a direct link to the official WHO page with more details about each indicator
Year: This feature captures data for specific years (e.g., 2014, 2020, and 2021), enabling trend analysis.
Region and Country: Identifies Sudan within the Eastern Mediterranean Region (EMR).
Uncertainty Range: The dataset provides a confidence interval for mortality rates, indicating the range of possible values (low to high).
Numeric and Display Values: Includes raw numeric values alongside formatted values for straightforward interpretation.
File name: disease_indicators.csv

### Sources:
Malaria Indicators for Sudan: https://data.humdata.org/dataset/2e8b6442-56ef-4bff-98eb-dfbfc62f28ed/resource/c2e96c5d-2ce5-44d7-a91b-a8728ffd05c4/download/malaria_indicators_sdn.csv

Tuberculosis Indicators for Sudan: https://data.humdata.org/dataset/2e8b6442-56ef-4bff-98eb-dfbfc62f28ed/resource/2963cf5b-fbbc-41be-bbe3-407777a13dd4/download/tuberculosis_indicators_sdn.csv

Neglected tropical diseases indicators for Sudan: https://data.humdata.org/dataset/2e8b6442-56ef-4bff-98eb-dfbfc62f28ed/resource/f2a8fb09-58e1-4298-9343-ace48ee91628/download/neglected_tropical_diseases_indicators_sdn.csv

Noncommunicable diseases indicators for Sudan: https://data.humdata.org/dataset/2e8b6442-56ef-4bff-98eb-dfbfc62f28ed/resource/5462eebd-91f3-43fd-9836-4b76641832bf/download/noncommunicable_diseases_indicators_sdn.csv

HIV Indicators for Sudan: https://data.humdata.org/dataset/2e8b6442-56ef-4bff-98eb-dfbfc62f28ed/resource/87772772-883b-4f12-ba82-d01165a3e503/download/hiv_indicators_sdn.csv

Hepatitis Indicators for Sudan: https://data.humdata.org/dataset/2e8b6442-56ef-4bff-98eb-dfbfc62f28ed/resource/410a6688-ce62-462a-8432-d8a39ff9cae2/download/hepatitis_indicators_sdn.csv

Sexually Transmitted Infections Indicators for Sudan: https://data.humdata.org/dataset/2e8b6442-56ef-4bff-98eb-dfbfc62f28ed/resource/500dae5a-36ef-4816-8355-082342153b13/download/sexually_transmitted_infections_indicators_sdn.csv


