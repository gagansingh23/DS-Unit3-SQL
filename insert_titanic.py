import pandas as pd
import paycopg2
import csv

dbname = 'jvdtvvjt'
user = 'jvdtvvjt'
password = '8vsCvY5AJDgNtKOGWQVo8mH7lIUgt_df'
host = 'postgres://jvdtvvjt:8vsCvY...@rajje.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname=dbname, user=user, 
                            password=password, host=host)
                        
pg_curs = pg_conn.cursor()

titanic = """
CREATE TABLE titanic (
  survived       INTEGER,
  name  varchar(200) NOT NULL,
  pClass    INTEGER
);
"""

with open('titanic)

pg_curs.execute(titanic)
pg_conn.commit('titanic.csv', 'r') as f:
next(f)
pg_curs.copy_from(f, 'titanic', sep=',')
pg_conn.commit()

#url = ('https://github.com/gagansingh23/DS-Unit-3-Sprint-2-SQL-and-Databases/blob/master/module2-sql-for-analysis/titanic.csv')

#titanic = pd.read_csv(url)

#print(titanic.head(5))

query = # 
pg_curs.execute(query)
pg_curs.fetchall()

