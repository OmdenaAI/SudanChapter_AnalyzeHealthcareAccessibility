# Data Dictionary on Socio- economic demographic data 

Below is the data dictionary for the dataset demographicsAlt.csv : 

| **Column Name** | **Description**                              | **Data Type** | **Possible Values/Units** | **Source**     | **Remarks**                             |
|-----------------|----------------------------------------------|---------------|---------------------------|----------------|-----------------------------------------|
| **Region**      | Name of the region                           | String        | List of regions           | Survey Data    | May contain missing values              |
| **Year**        | Year of observation                          | Integer       | 1950–2024                 | Historical Data| No missing values                      |
| **Indicator**   | Name of the indicator (e.g., Life Expectancy)| String        | Life Expectancy, etc.     | WHO            |                                         |
| **Age**  | Age                      | String         | 5+, 18-22                     | WHO            | Range of Ages in the indicator  |
| **Gender**  | Gender                      | String         | Male, Female                     | WHO            | Gender, if specificed in the indicator |
| **Quintile**  | Quintile                   | Integer | 1,2,3,4,5,9 | WHO | Population grouping into 5 quntiles, 1 being poorest, 5, being richest, 9 means quantile not defined |
| **values are in percentage**  | Boolean to indicate if values under year are numbers or percentage | Boolean | True  or False | WHO | True means values are in percentage, False means is a number |
| **non-zero-year-columns**  | meta column, indicators, how many years have values availale | Integer | ranging from 1 to 74 | WHO | Count of the years for which indictor values are available |
