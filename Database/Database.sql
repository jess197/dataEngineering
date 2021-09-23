CREATE DATABASE deliverycenter; 
USE deliverycenter;


CREATE TABLE deliveries(
  driver_id INT, 
  delivery_order_id INT, 
  delivery_id INT, 
  delivery_distance_meters INT,
  delivery_status VARCHAR(25),
  PRIMARY KEY(delivery_id)
  );
 
SELECT *  FROM deliveries;