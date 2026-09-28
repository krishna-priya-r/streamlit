#define a class to perform database operation on Book table.
#create a class named BookListCreateRetreiveUpdateDelete and define methods
#list() for readimg all records
#create() for creating new record
#retrieve() for readins specific record
#update(id,data) for updating a specific record
#delete(id) for deleting a specific record

import mysql.connector

class BookListCreateRetreiveUpdateDelete:

       def __init__(self):
           self.con=mysql.connector.connect(user="root",password="root",host="localhost",database="library_db")
           self.c=self.con.cursor()
           print("successfully connected")
       def list(self):
           query='select * from Book;'
           self.c.execute(query)
           self.records=self.c.fetchall()
           # if self.records:
           #     for row in self.records:
           #         print(row)
           # else:
           #     print("no record found")
           return self.records

       def create(self,title,author,price,pages,language):
           self.title=title
           self.author=author
           self.price=price
           self.pages=pages
           self.language=language
           query="insert into Book (title,author,price,pages,language) values(%s,%s,%s,%s,%s);"
           data=(self.title,self.author,self.price,self.pages,self.language,)
           self.c.execute(query,data)
           self.con.commit()
           print("inserted")

       def retrieve(self,id):

           query="select * from Book where id=%s"
           data=(id,)
           self.c.execute(query,data)
           self.record=self.c.fetchone()
           return self.record

       def update(self,id,title,author,price,pages,language):
          query="update Book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
          value=(title,author,price,pages,language,id,)
          self.c.execute(query,value)
          self.con.commit()
          if self.c.rowcount > 0:
              return True
          else:
              return False

       def delete(self,id):
           query = "delete from Book where id=%s"
           data=(id,)
           self.c.execute(query, data)
           self.con.commit()
           if self.c.rowcount>0:
                  return True
           else:
                  return False



book_instance= BookListCreateRetreiveUpdateDelete()

book_instance.update(1,'title12','author11',200,150,'eng')