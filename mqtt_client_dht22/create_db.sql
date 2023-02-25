# CREATE DATABASE IF NOT EXISTS db_smt;
CREATE TABLE IF NOT EXISTS db_smt.tb_temp_humi(
	id INT NOT NULL AUTO_INCREMENT,
	id_sensor varchar(20) NOT NULL,
	temp_value FLOAT,
	humi_value FLOAT,
	date_time DATETIME,
	PRIMARY KEY (id_temp_humi)
	);
