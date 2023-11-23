import pandas as pd
import pyodbc as pyo
import sqlite3

class KetNoi:
    # Kết nối đến cơ sở dữ liệu
    def getTable(self, query):
        connection = pyo.connect(driver='ODBC Driver 17 for SQL Server', host='DESKTOP-KHGPLPT\MAY1', database='DATA', trusted_connection='yes')
        # df = pd.read_sql(query, connection)
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchall()
        # print(row)
        cursor.close()
        connection.close()
        # print(df)
        return row

kn = KetNoi()
kn.getTable('select * from SuKien')


