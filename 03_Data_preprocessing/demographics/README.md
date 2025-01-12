# Data Dictionary on Socio- economic demographic data 

Below is the data dictionary for the dataset demographicsAlt.csv : 

| **Column Name** | **Description**                              | **Data Type** | **Possible Values/Units** | **Source**     | **Remarks**                             |
|-----------------|----------------------------------------------|---------------|---------------------------|----------------|-----------------------------------------|
| **Region**      | Name of the region                           | String        | List of regions           | Survey Data    | May contain missing values              |
| **Year**        | Year of observation                          | Integer       | 1950–2024                 | Historical Data| No missing values                      |
| **Indicator**   | Name of the indicator (e.g., Life Expectancy)| String        | Life Expectancy, etc.     | WHO            |                                         |
| **Percentage**  | Value of the indicator (%)                   | Float         | 0–100                     | WHO            | Indicating, if value is a number or percentage|
| **Age**  | Age                      | String         | 5+, 18-22                     | WHO            | Range of Ages in the indicator  |
| **Gender**  | Gender                      | String         | Male, Female                     | WHO            | Gender, if specificed in the indicator |
| **Quintile**  | Quintile                   | String         | 1st, First                     | WHO            | Population grouping into 5 quntiles, 1 being poorest, 5, being richest |
