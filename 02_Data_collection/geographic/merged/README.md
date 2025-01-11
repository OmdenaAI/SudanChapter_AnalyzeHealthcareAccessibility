## Dataset Overview
This dataset provides comprehensive geometric, satellite, and weather data related to Sudan's administrative areas across three levels: state, district, and district subdivision. It integrates various data sources to support the analysis of administrative boundaries, vegetation indices, weather patterns, and changes in water content and wawter bodies such as stagnant water bodies where the breeding of mosquitoes (malaria vectors) and other infectious diseases may occur. Assessing vegetation growth for vector-borne diseases (like malaria) and cholera can also be useful.


## Data Sources
1. Geometric Data
    * Description: Geometric data of Sudan's administrative areas on three levels: states, districts, and district subdivisions.
    * Source: [GADM Spatial Database by Country](https://gadm.org/download_country.html)
    * Date Range: -
    * Granularity: State, district, and district subdivision level
2. Satellite Data on Vegetation and Water Indices
    * Description: Satellite data on vegetation, water content, and water body changes (NDVI, NDWI indices) for district subdivision level (state >> district >> district subdivision).
    * Source: [Copernicus Sentinel-2 Mission](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-2)
    * Date Range: July 2015 – January 2025
    * Granularity: District subdivision level
3. Weather Data
    * Description: Aggregated weather data by date, including precipitation, humidity, temperature, and other metrics, recorded weekly.
    * Source: [OpenWeatherMap One Call API 3.0 - Daily Aggregation](https://openweathermap.org/api/one-call-3#history_daily_aggregation)
    * Date Range: January 2022 – December 2024
    * Granularity: State level, aggregated weekly
4. Infrastructure Data _[DISCLAIMER: this data is currently not included in the merged file but it's available if needed]_
    * Description: Infrastructure data including highways, railways, and waterways for Sudan's districts.
    * Source: [OpenStreetMap API](https://wiki.openstreetmap.org/wiki/API_v0.6)
    * Date Range: -
    * Granularity: District level
5. Major Cities' Location
    * Description: Locations of Sudan's major cities by state.
    * Source: [Simplemaps database](https://simplemaps.com/data/world-cities)
    * Date Range: -
    * Granularity: State level


## Data Dictionary  

| **Column Name**                  | **Description**                                                                                             | **Type**          | **Granularity**              | **Example Value**                                     |  
|-----------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------|-----------------------------|-----------------------------------------------------|  
| `GID_L0`                          | Unique identifier for country-level administrative areas.                                                   | `string`          | Country                     | `SDN`                                               |  
| `GID_L1`                          | Unique identifier for state-level administrative areas.                                                     | `string`          | State                       | `SDN.1_1`                                           |  
| `GID_L2`                          | Unique identifier for district-level administrative areas.                                                  | `string`          | District                    | `SDN.1.2_1`                                         |  
| `GID_L3`                          | Unique identifier for district subdivision-level administrative areas.                                      | `string`          | District Subdivision        | `SDN.1.2.3_1`                                       |  
| `COUNTRY`                         | Name of the country (Sudan).                                                                                | `string`          | Country                     | `Sudan`                                             |  
| `NAME_L1`                         | Name of the state.                                                                                          | `string`          | State                       | `NorthDarfur`                                       |  
| `NAME_L2`                         | Name of the district.                                                                                       | `string`          | District                    | `Kutum`                                             |  
| `NAME_L3`                         | Name of the district subdivision.                                                                           | `string`          | District Subdivision        | `Karnoy`                                            |  
| `GEOMETRY_L1`                     | Geometric data (polygons) for state boundaries.                                                             | `geometry`        | State                       | `MULTIPOLYGON (((32.7365 13.7191, 32.7335 13.749, ...)))`            |  
| `GEOMETRY_L2`                     | Geometric data (polygons) for district boundaries.                                                          | `geometry`        | District                    | `MULTIPOLYGON (((33.1141 14.8749, 32.9916 14.9108, ...))`             |  
| `GEOMETRY_L3`                     | Geometric data (polygons) for district subdivision boundaries.                                              | `geometry`        | District Subdivision        | `MULTIPOLYGON (((32.9784 15.1733, 33.0415 15.2452, ...)))`            |  
| `COORDINATES_L1`                  | Coordinates (centroids) for state boundaries.                                                               | `object`          | State                       | `[(26.989, 11.7898), (26.8901, 11.7679),  ...]`                       |  
| `COORDINATES_L2`                  | Coordinates (centroids) for district boundaries.                                                            | `object`          | District                    | `[(25.2552, 14.1369), (25.2314, 14.1837),  ...]`                       |  
| `COORDINATES_L3`                  | Coordinates (centroids) for district subdivision boundaries.                                                | `object`          | District Subdivision        | `[23.1315, 15.7106), (23.1535, 15.7122),  ...]`                       |  
| `CENTROID_COORDINATES_L1`         | Centroid of state-level polygons.                                                                           | `object`          | State                       | `(16.210072141665464, 25.56137078287929)`                       |  
| `CENTROID_COORDINATES_L2`         | Centroid of district-level polygons.                                                                        | `object`          | District                    | `(14.970643898696625, 23.99197320791689)`                       |  
| `CENTROID_COORDINATES_L3`         | Centroid of district subdivision-level polygons.                                                            | `object`          | District Subdivision        | `(15.276145500285851, 23.579148396331252)`                       |  
| `SENTINEL_2_NDVI_L3`              | NDVI (Normalized Difference Vegetation Index) values at district subdivision level.                         | `object`          | District Subdivision        | `{'data': [{'interval_from': '2015-10-20', 'interval_to': '2015-10-21', 'ndvi_min': 0.005310070235282183, 'ndvi_max': 0.005310070235282183, 'ndvi_mean': 0.005310070235282183}, {}, ...]}`            |  
| `SENTINEL_2_NDWI_L3`              | NDWI (Normalized Difference Water Index) values at district subdivision level.                              | `object`          | District Subdivision        | `{'data': [{'interval_from': '2015-10-20', 'interval_to': '2015-10-21', 'ndvi_min': -0.011544699780642986, 'ndvi_max': -0.011544699780642986, 'ndvi_mean': -0.011544699780642986}, {}, ...]}`            |  
| `WEATHER_WEEKLY_L1`               | Aggregated weather data (e.g., precipitation, temperature) for state-level, recorded weekly.            | `object`          | State                       | `{'2022-01-01': {'cloud_cover': 65.0, 'humidity_percentage': 12.0, 'precipitation_total_mm': 0.0, 'temperature_min_celsius': 19.78, 'temperature_max_celsius': 30.0, 'temperature_afternoon_celsius': 28.83, 'temperature_night_celsius': 21.03, 'temperature_evening_celsius': 25.44, 'temperature_morning_celsius': 19.78, 'pressure_hpa': 1012.0, 'wind_max_speed_kmh': 6.04, 'wind_max_direction_degrees': 347.0}, '2022-01-08': {}, ...}` |  
| `MAJOR_CITIES_L1`                 | Names and coordinates of major cities in each state.                                                        | `object`          | State                       | `{'city': 'Khartoum', 'lat': 15.6, 'lon': 32.5}`   |    


## Further Reading

* Copernicus Sentinel Missions:
    - [Sentinel Hub](https://dataspace.copernicus.eu/analyse/apis/sentinel-hub)
    - [Sentinel Missions](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data)
    - [Sentinel-2](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-2)
    - [Sentinel-2 Level 1C](https://documentation.dataspace.copernicus.eu/Data/SentinelMissions/Sentinel2.html#sentinel-2-level-1c-top-of-atmosphere-toa)
    - [Sentinel-2 Level 1C - API access, requests](https://documentation.dataspace.copernicus.eu/APIs/SentinelHub/Data/S2L1C.html)
    - [Complete list of Sentinel-2 composites and algorithms](https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel/sentinel-2/)
    - [Sentinel-3](https://dataspace.copernicus.eu/explore-data/data-collections/sentinel-data/sentinel-3)
    - [Sentinel-3 SLSTR](https://sentiwiki.copernicus.eu/web/s3-slstr-instrument)
    - [Interactive Map with Sentinel-2 L1C data](https://browser.dataspace.copernicus.eu/?zoom=11&lat=15.50919&lng=32.49491&themeId=DEFAULT-THEME&visualizationUrl=U2FsdGVkX19thDCcH4aD62EybqrdKXcd17vDo0WcFB6ko02GLJfB8SIQCq9sqQv7S2j2YALE4BYcee7XZX18YmeVrBEZNebFhpic1tporv2XUjNN94K80mCTRL9%2FFUba&datasetId=S2_L1C_CDAS&fromTime=2025-01-01T00%3A00%3A00.000Z&toTime=2025-01-01T23%3A59%3A59.999Z&layerId=7-NDWI&demSource3D=%22MAPZEN%22&cloudCoverage=10&dateMode=SINGLE)
