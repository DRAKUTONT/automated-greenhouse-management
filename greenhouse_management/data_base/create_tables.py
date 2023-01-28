from greenhouse_management.data_base.connect_to_db import connect_to_database


def create_tables():
    query_1 = '''CREATE TABLE "temperature" (
                "temp_1"	REAL,
                "temp_2"	REAL,
                "temp_3"	REAL,
                "temp_4"	REAL,
                "average_temp"	REAL,
                "id"	INTEGER
            );'''

    query_2 = '''CREATE TABLE "humidity" (
                "hum_1"	REAL,
                "hum_2"	REAL,
                "hum_3"	REAL,
                "hum_4"	REAL,
                "average_hum"	REAL,
                "id"	INTEGER
            );'''

    query_3 = '''CREATE TABLE "soil_humidity" (
                "soil_hum_1"	REAL,
                "soil_hum_2"	REAL,
                "soil_hum_3"	REAL,
                "soil_hum_4"	REAL,
                "soil_hum_5"	REAL,
                "soil_hum_6"	REAL,
                "average_soil_hum"  REAL,
                "id"	INTEGER
            );'''

    connect_to_database(query_1, mode='w')
    connect_to_database(query_2, mode='w')
    connect_to_database(query_3, mode='w')
