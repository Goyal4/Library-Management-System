#!/usr/bin/env python
# coding: utf-8

# In[5]:


import mysql.connector as mc
DB_NAME='library'
TB_NAME='data'
def create_db():
    global DB_NAME
    try:
        con=mc.connect(user="root",password="2112",host="localhost")
        if con.is_connected(): 
            cur=con.cursor() # cur user defined name
            DB_NAME=input("enter database name")
            cur.execute("CREATE DATABASE if NOT Exists {}".format(DB_NAME))
        else:
            print('sorry cannot connect')           
    except: print("some error")       
    finally: con.close()
def create_tb():
    global TB_NAME
    try:
        con=mc.connect(user="root",password="2112",host="localhost",database='library')
        if con.is_connected(): 
            cur=con.cursor() # cur user defined name
            cur.execute("use {}".format(DB_NAME))
            TB_NAME=input("enter table name")
            cur.execute('''CREATE TABLE if NOT Exists {}(serial_no int Primary key AUTO_INCREMENT,
            Title varchar(35) not null, Author varchar(35) not null,Status varchar(35) not null,Genre varchar(35) not null)'''
                        .format(TB_NAME))
        else:
            print('sorry cannot connect')    
    except: print("some error")       
    finally: con.close()
def insert_rec():
    while (True):
        try:
            con=mc.connect(user="root",password="2112",host="localhost",database='library')
            if con.is_connected(): 
                cur=con.cursor() # cur user defined name
                title=input("enter Title")
                author=input("enter The name of author")
                status=input("enter status")
                genre=input("Enter Genre")
                cur.execute("use {}".format(DB_NAME))
                sql="INSERT INTO data(Title,Author,Status,Genre) VALUES(%s,%s,%s,%s)"
                cur.execute(sql,(title,author,status,genre))
                con.commit()
            else:
                print('sorry cannot connect')
        except Exception as err: print("some error"+err)
        con.close()
        m=input("do you want to enter more records?")
        if (m=='no'): break
def delete_rec():
    try:
        con=mc.connect(user="root",password="2112",host="localhost",database='library')
        if con.is_connected(): 
            cur=con.cursor()
            title=input("enter name of book")
            sql="delete FROM data WHERE Title = %s"
            cur.execute(sql,(title,))
            con.commit()
        else:
            print('sorry cannot connect')
    except Exception as err: print("some error"+str(err))
    finally: con.close()

def display_all_rec():
    try:
        con=mc.connect(user="root",password="2112",host="localhost",database='library')
        if con.is_connected(): 
            cur=con.cursor()
            cur.execute("use {}".format(DB_NAME))
            sql="select * FROM data"
            cur.execute(sql)
            while True:
                i=cur.fetchone()
                if not i:
                    break
                print("Serial number: {}".format(i[0]))
                print("Title: {}".format(i[1]))
                print("Author: {}".format(i[2]))
                print("Status: {}".format(i[3]))
                print("Genre : {}".format(i[4])) 
                print()
                      
        else:
            print('sorry cannot connect')
    except Exception as err: print("some error"+str(err))
    finally: con.close()
        
def search_title_rec():
    try:
        con=mc.connect(user="root",password="2112",host="localhost",database='library')
        if con.is_connected(): 
            cur=con.cursor()
            title=input("enter name of the book")
            cur.execute("use {}".format(DB_NAME))
            sql="select * FROM data where title = %s"
            cur.execute(sql,(title,))
            while True:
                i=cur.fetchone()
                if not i:
                    if cur.rowcount==0:
                        print("sorry no such book found")
                    break
                print("Serial number: {}".format(i[0]))
                print("Title: {}".format(i[1]))
                print("Author: {}".format(i[2]))
                print("Status: {}".format(i[3]))
                print("Genre : {}".format(i[4])) 
                print()
        else:
            print('sorry cannot connect')
    except Exception as err: print("some error"+str(err))
    finally: con.close()
        
def search_author_rec():
    try:
        con=mc.connect(user="root",password="2112",host="localhost",database='library')
        if con.is_connected(): 
            cur=con.cursor()
            cur.execute("use {}".format(DB_NAME))
            author=input("enter the name of author")
            sql="select * FROM data where author = %s"
            cur.execute(sql,(author,))
            while True:
                i=cur.fetchone()
                if not i:
                    if cur.rowcount==0:
                        print("sorry no book found by this author")
                    break
                print("Serial number: {}".format(i[0]))
                print("Title: {}".format(i[1]))
                print("Author: {}".format(i[2]))
                print("Status: {}".format(i[3]))
                print("Genre : {}".format(i[4])) 
                print()
                      
        else:
            print('sorry cannot connect')
    except Exception as err: print("some error"+str(err))
    finally: con.close()
create_db()
create_tb()


# In[ ]:




