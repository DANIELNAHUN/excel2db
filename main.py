import os

import pandas as pd
import pymysql
from dotenv import load_dotenv

load_dotenv()

def connection_db_local():
    conn = pymysql.connect(host=os.getenv("IP_SERVER_DATABASE"), database=os.getenv(
        'BD_SERVER'), user=os.getenv('USER_SERVER'), passwd=os.getenv('PASSWORD_SERVER'))
    return conn


def read_excel(file):
    df = pd.read_excel(file)
    for i, row in df.iterrows():
        tarifa = row['tarifa_internet']
        velocidad = int(row['velocidad'])
        sql = f"UPDATE dim_tarifas_internet SET velocidad = {velocidad} WHERE tarifa_internet LIKE '{tarifa}'"

        try:
            conn = connection_db_local()
            try:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    conn.commit()
            finally:
                conn.close()
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print(f"Error not connect in mysql {e}")


url= "files\Tarifa_internet.xlsx"
read_excel(url)