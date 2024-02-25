'''
Author: Renn Everette P. Caday
Date: Feb. 25, 2024
Description: This python file retrieves taxi data from 
  online source, transforms it and visualizes the plot
'''

import pyarrow.parquet as pq 
import sqlite3
import matplotlib.pyplot as plt
  
trips = pq.read_table('C:/xPersonal/Initial Exam/yellow_tripdata_2023-02.parquet') 
trips = trips.to_pandas()

# filter the data
filtered = trips[(trips['passenger_count'] > 0) & (trips['tpep_dropoff_datetime'] > '2023-02-01') & (trips['tpep_dropoff_datetime'] < '2023-03-01')]

con = sqlite3.connect("initExam.db")
cur = con.cursor()

cur.execute("create table if not exists yellowtaxi_feb_daily(VendorID int, tpep_pickup_datetime datetime, tpep_dropoff_datetime datetime, passenger_count real, trip_distance real, RatecodeID int real,store_and_fwd_flag int,PULocationID int,DOLocationID int,payment_type int,fare_amount real,extra real,mta_tax real,tip_amount real,tolls_amount real,improvement_surcharge real,total_amount real,congestion_surcharge real,Airport_fee real)")

# insert data into sql
filtered.to_sql('yellowtaxi_feb_daily', con, index=False, if_exists='replace')

 
# group by tpep_dropoff_datetime and get sum of total amount
dfg = filtered.groupby([filtered['tpep_dropoff_datetime'].dt.date])['total_amount'].sum()
print(dfg)

# plot the group by result
ax = dfg.plot.bar(figsize=(8, 5), ylabel='Total Amount',xlabel='Date')
plt.title("Yellow Taxi Daily Total Amount For February 2023")

# show the plot
plt.show()