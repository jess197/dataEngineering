import dataEngineering.Database.connectdb as db
cursor = db.connection.cursor()
def insertDataDelivery(driver_id,delivery_order_id,delivery_id,delivery_distance_meters,delivery_status):
    mysql_insert_query = """INSERT INTO deliveries(driver_id,delivery_order_id,delivery_id,delivery_distance_meters,delivery_status) 
                         VALUES (%s, %s, %s, %s, %s)"""
    record = (driver_id,delivery_order_id,delivery_id,delivery_distance_meters,delivery_status)
    try:
        cursor.execute(mysql_insert_query,record)
        db.connection.commit()
    except:
        print(record,type(driver_id))
        print(driver_id)
        raise
