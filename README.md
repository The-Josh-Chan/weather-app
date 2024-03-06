# weather-app
This weather app was originally supposed to pull solar data from power.larc.nasa.gov to be used in a 5th year design project at Queen's University. However, reports took precident and solar data was provided by our faculty advisor. After the design project was done, the this project was refurbished to take weather data and upload to a local sqlite3 database. I wanted to see if I could build something that could make an API call and upload the data to a database. Following CRUD principals, it can insert weather data into the sqlite3 database, retreive data, update data and delete data.

The API call only takes temperature at 2 meters above the ground. other data can be taken but can be updated to take more data. Sqlite3 data tables will need to be updated if so. 
