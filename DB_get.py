from sqlalchemy import text
import csv

def get_rows(m):
 stmt = text("SELECT * FROM flat WHERE rooms=:y ")
 stmt = stmt.bindparams( y=m)
 res=db.execute(stmt).fetchall()
 with open('C:\python\predict\myoutput.csv', 'w') as out:
     csv_out = csv.writer(out)
     csv_out.writerow(['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG', 'Date', 'Postcode', 'Regionname' ,'Propertycount', 'Distance', 'CouncilArea'])
     for row in res:
         csv_out.writerow(row)
 return res





