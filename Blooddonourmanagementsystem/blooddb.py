import mysql.connector


class Blooddonor:
    def __init__(self):
        self.con = mysql.connector.connect(user="root", password='root', host='localhost', database='blooddb')
        self.c = self.con.cursor()

    def post(self,name,bloodgroup,phone,city,last_donation):
         self.name=name
         self.bloodgroup=bloodgroup
         self.phone=phone
         self.city=city
         self.last_donation=last_donation
         query="insert into donor(name,blood_group,phone,city,last_donation)values(%s,%s,%s,%s,%s)"
         data=(self.name,self.bloodgroup,self.phone,self.city,self.last_donation,)
         self.c.execute(query,data)
         self.con.commit()
         if self.c.rowcount>0:
             print("inserted successfully")
         else:
             print("not inserted")

    def get(self):
        query='select * from donor'
        self.c.execute(query)
        records=self.c.fetchall()
        if records:
            return records

    def retrieve(self,id):
        data=(id,)
        query="select * from donor where id=%s"
        self.c.execute(query,data)
        record=self.c.fetchone()
        if record:
            return record


    def put(self,id,name,bloodgroup,phone,city,last_donation):
         self.id=id
         self.name=name
         self.bloodgroup=bloodgroup
         self.phone=phone
         self.city=city
         self.last_donation=last_donation
         query="update donor set name=%s,blood_group=%s,phone=%s,city=%s,last_donation=%s where id=%s"
         data=(self.name,self.bloodgroup,self.phone,self.city,self.last_donation,self.id,)
         self.c.execute(query,data)
         self.con.commit()
         return self.c.rowcount > 0

    def delete(self,id):
        self.id=id
        data=(self.id,)
        query="delete from donor where id=%s"
        self.c.execute(query,data)
        self.con.commit()
        return self.c.rowcount > 0


