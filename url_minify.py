#!/usr/bin/python
import MySQLdb as mysql
from datetime import datetime

# MySQL connection string
conn = mysql.connect(host="localhost", user="bkrueger", passwd="omg134!", db="urls")

# Arbitrary stuff
original_url = raw_input("Input URL: ")
original_url = "http://"+original_url
print original_url

# This section will check to see if the original URL is already in the database and return the value
# Of original_url and final_url in DB if so, if not, it will proceed to create the row and return values.

# Make the changes and commit them to DB
cursor = conn.cursor( );
cursor.execute("INSERT INTO urls (original_url, final_url, img_id) VALUES ({0}, 'http://ya.ps/a3', 'a3');".format('"'+original_url+'"'))
print "Value added"
print "Affected rows: ", cursor.rowcount;
conn.commit()
