import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def show_error(e):
    print('Error code:', e.errno)
    print('SQLSTATE value:', e.sqlstate)
    print('Error message:', e.msg)
    print('Error:', e)
    s = str(e)
    print('Error:', s)


def connect():
    global conn
    try:
        conn = mysql.connector.connect(
            host=os.getenv('_HOST_MYSQL'),
            user=os.getenv('_USER_MYSQL'),
            password=os.getenv('_PASSWORD_MYSQL'),
        )
    except mysql.connector.Error as e:
        print('Erro ao conectar')
        show_error(e)


def reconnect():
    try:
        if conn.is_closed():
            conn.reconnect()
    except mysql.connector.Error as e:
        print('Erro ao reconectar')
        show_error(e)


def disconnect():
    try:
        if conn.is_connected():
            conn.close()
    except mysql.connector.Error as e:
        print('Erro ao desconectar')
        show_error(e)


def insert_values(values):
    sql = (
        'INSERT INTO db_smt.tb_temp_humi ('
        'id_sensor,temp_value,humi_value,date_time) '
        'VALUES ('
        '%s, %s, %s, %s);'
    )
    reconnect()

    if conn.is_connected():
        try:
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            cursor.close()
        except mysql.connector.Error as e:
            print('Erro ao inserir dados')
            show_error(e)
        finally:
            disconnect()


def select_values(id_sensor):
    sql = 'SELECT * FROM db_smt.tb_temp_humi WHERE id_sensor = %s ORDER BY id DESC LIMIT 1;'
    reconnect()

    if conn.is_connected():
        try:
            cursor = conn.cursor()
            cursor.execute(sql, (id_sensor,))
            values = cursor.fetchall()
            cursor.close()
        except mysql.connector.Error as e:
            print('Erro ao buscar dados')
            show_error(e)
        finally:
            disconnect()
            keys = ['id', 'id_sensor', 'temp_value', 'humi_value', 'date_time']
            dici = dict(zip(keys, values[0]))
            dici['date_time'] = dici['date_time'].strftime('%Y%m%d%H%M%S')
            return dici


if __name__ == '__main__':
    teste = eval(
        '{"id_sensor":"sensor_ambiente_1","temp_value":18.60, "humi_value":18.60}'
    )
    values = teste.values()
    connect()
    sensor = 'sensor_ambiente_1'
    print(select_values(sensor))
