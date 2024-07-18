#importing csv file
import kaggle
!kaggle datasets download shivamb/netflix-shows -f netflix_titles.csv

#extracting csv from zip file
import zipfile
zip_ref =  zipfile.ZipFile('netflix_titles.csv.zip')
zip_ref.extractall()
zip_ref.close()

#importing pandas
import pandas as pd
df = pd.read_csv('netflix_titles.csv')

#connecting sql server with pandas
import sqlalchemy as sal
engine = sal.create_engine('mssql://DESKTOP-63D6CEJ\\SQLEXPRESS/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn =engine.connect()

df.to_sql('netflix_raw', con=conn, index=False, if_exists='append')
conn.close()
