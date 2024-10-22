# Reading CSv with Pandas #
import pandas as pd

from dataEngineering.Load.insertDataDelivery import insertDataDelivery

deliveries = pd.read_csv('../datalab-d/datasets/deliveries.csv')

for row in deliveries.iterrows():
    driver_id = row[1]['driver_id']
    delivery_order_id = row[1]['delivery_order_id']
    delivery_id = row[1]['delivery_id']
    delivery_distance_meters = row[1]['delivery_distance_meters']
    delivery_status = row[1]['delivery_status']

    if(str(driver_id) == 'nan'):
        continue

    if(str(delivery_order_id) == 'nan'):
        continue

    if(str(delivery_id) == 'nan'):
        delivery_id = 0

    if(str(delivery_distance_meters) == 'nan'):
        delivery_distance_meters = 0

    if(delivery_status == 'nan'):
        delivery_status = ''

    insertDataDelivery(driver_id, delivery_order_id, delivery_id,delivery_distance_meters,delivery_status)












