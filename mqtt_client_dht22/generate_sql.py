import numpy as np
from datetime import datetime

sensores = ['sensor_ambiente_1','sensor_ambiente_2','sensor_ambiente_3','sensor_drybox','sensor_geladeira']

sql="""
# CREATE DATABASE IF NOT EXISTS db_smt;
CREATE TABLE IF NOT EXISTS db_smt.tb_temp_humi(
	id_temp_humi INT NOT NULL AUTO_INCREMENT,
	id_sensor varchar(20) NOT NULL,
	temp_value FLOAT,
	humi_value FLOAT,
	date_time DATETIME,
	PRIMARY KEY (id_temp_humi)
	);

"""

for i in range(10000):
    id_sensor = np.random.choice(sensores)
    temp = np.random.uniform(low=18.0, high=30.0, size=None)
    humi = np.random.uniform(low=20.0, high=60.0, size=None)
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    sql += f'\nINSERT INTO db_smt.tb_temp_humi (id_sensor,temp_value,humi_value,date_time) VALUES ("{id_sensor}",{temp:.2f},{humi:.2f},{date});'

with open(file='generate_values.sql',mode='w') as f:
    f.write(sql)