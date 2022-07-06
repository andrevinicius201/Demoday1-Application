"""
Created on Sat Jul 25 13:34:18 2020
@author: hp
"""

import pymysql
import aws_credentials as rds
conn = pymysql.connect(
        host= "tutorial-db-cluster-demo.cluster-cq6la0ijpzvo.us-east-1.rds.amazonaws.com", #endpoint link
        port = 3306,
        user = "tutorial_user", # admin
        password = "12345678", #adminadmin
        db = "sample"
        )

#cursor=conn.cursor()
#drop_table="drop table Details;"
#cursor.execute(drop_table)

#Criando tabela
#cursor=conn.cursor()
#create_table=
#CREATE TABLE Details (id INT NOT NULL AUTO_INCREMENT, name varchar(200),email varchar(200), comment varchar(200), gender varchar(200),PRIMARY KEY(id));
#cursor.execute(create_table)


#Deletando tudo da tabela
# cursor=conn.cursor()
# delete_table="""
# delete from Details where 1=1
# """
# cursor.execute(delete_table)


def insert_details(name,email,comment,gender):
    cur=conn.cursor()
    cur.execute("INSERT INTO Details (name,email,comment,gender) VALUES (%s,%s,%s,%s)", (name,email,comment,gender))
    conn.commit()

def get_details():
    conn.commit()
    cur=conn.cursor()
    cur.execute("SELECT *  FROM Details")
    details = cur.fetchall()
    return details

def delete(id):
    print("entrou aqui")
    cur=conn.cursor()
    cur.execute("DELETE FROM Details WHERE id = %s" % (id))
    conn.commit()
    return "deleted"  
