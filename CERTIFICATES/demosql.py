import sqlite3  
import hashlib
class SQL:
    def __init__(self):
        pass       
 
    def insertData(self,title,nickname,full_name,gender,contact,email,event):
        self.conn = sqlite3.connect('attendees.db')
        self.c= self.conn.cursor()             
        id_code = full_name+contact+email
        result  =hashlib.md5(id_code.encode())
        id_hash = result.hexdigest()
        self.c.execute("insert into tbl_attendees values('{id}','{a}','{b}','{c}','{d}','{e}','{f}','{g}')".format(a= title, b= nickname,c=full_name,d=gender, e=contact, f=email,g=event,id=id_hash) )
        self.conn.commit()
        self.conn.close()
    def insertEvent(self, id, event_name, days, venue):
        self.conn = sqlite3.connect('attendees.db')
        self.c= self.conn.cursor()
        self.c.execute("insert into tbl_events values('{}','{}','{}','{}')".format(id,event_name,days,venue))   
        self.conn.commit()
        self.conn.close()

    def selectAllEvents(self):
        self.conn = sqlite3.connect('attendees.db')
        self.c= self.conn.cursor()    
        self.c.execute("""SELECT * FROM tbl_events""")
        self.listOfData= list(self.c.fetchall())        
        self.conn.commit()
        self.conn.close()
        return (self.listOfData)
    def selectAllAttendees(self):
        self.conn = sqlite3.connect('attendees.db')
        self.c= self.conn.cursor()    
        self.c.execute("""SELECT * FROM tbl_attendees""")
        self.listOfData= list(self.c.fetchall())        
        self.conn.commit()
        self.conn.close()
        return (self.listOfData)

    def selectSpecificEvent(self):
        self.conn = sqlite3.connect('attendees.db')
        self.c= self.conn.cursor()    
        self.c.execute("""SELECT event_name FROM tbl_events""")
        self.listEvent= (self.c.fetchall())        
        self.conn.commit()
        self.conn.close()
        return (self.listEvent)
    
    def printData(self):
        self.conn = sqlite3.connect('attendees.db')
        self.c= self.conn.cursor()    
        self.c.execute("""SELECT * FROM tbl_attendees""")
        self.listOfData= list(self.c.fetchall())        
        self.conn.commit()
        self.conn.close()
        for i in self.listOfData:
            print(i)
SQL.printData
    




