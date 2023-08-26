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
        sql = f"UPDATE dim_tarifas_internet SET velocidad = {velocidad} WHERE tarifa_internet LIKE '{tarifa}%'"
        print(sql)
    #     values =[]
    #     for j in range(0,columns):
    #         val = df.loc[i][j]
    #         if val != val:
    #             val = ""
    #         values.append(val)
    #     tpl = tuple(values)
    #     result.append(tpl)
    # with open("files\df.txt",'w')as file:
    #     file.write(str(result))


url= "files\Tarifa_internet.xlsx"
read_excel(url)