
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector
import sqlalchemy
import sys
sys.path.insert(0,"/home/apprenant/PycharmProjects/db_recommandation/conf/conf.py")

def mysql_connect():
  from conf.conf import mysql_pseudo, mysql_mdp
  mysql_username = mysql_pseudo
  mysql_password = mysql_mdp
  database_name = 'nutri_score'
  database_connection = sqlalchemy.create_engine(
    'mysql+mysqlconnector://{0}:{1}@localhost/{2}'.format(mysql_username, mysql_password, database_name),
    pool_recycle=1, pool_timeout=57600).connect()
  return database_connection
print("done")
database_connection = mysql_connect()
print("done")
df = pd.read_csv("/home/apprenant/Downloads/recommandation.tsv", sep='\t', low_memory=False)
print("done")
#df.to_sql('nutri_all', database_connection, if_exists='replace', index=False)
print("done")