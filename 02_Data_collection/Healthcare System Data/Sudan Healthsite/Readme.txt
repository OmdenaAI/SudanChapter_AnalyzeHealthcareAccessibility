Information regarding five datasets:


1. translated_sudan_healthsites: Translated arabic names to English. 

2. translated_health_facilities: Translated arabic names to English.

3. concatenated_data_with_duplicate_values: Concatenated 1 and 2 without any change based on 'Name' as a Primary Key.

4. concatenated_data_without_duplicate_values: All duplicated values removed based on 'Name' (as a primary key).

5. concatenated_data_without_duplicate_nan_val_to_0: converted all NaN values to 0 (dropping might cause many rows to remove, hence).

6. sudan_health sites with co-ordinates: Seperated geometry points into X and Y columns
