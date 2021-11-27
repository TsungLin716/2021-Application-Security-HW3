import os
import csv
import mysql.connector

mydb = mysql.connector.connect(
  host=os.getenv('MYSQL_HOST'),
  user="root",
  password=os.getenv('MYSQL_ROOT_PASSWORD'),
  database='GiftcardSiteDB',
)

mycursor = mydb.cursor(prepared=True)
user_file = open('/users.csv')
product_file = open('/products.csv')
for row in csv.reader(user_file):
    last_login = row[1]
    user = row[2]
    password = row[3]

    print("Loading row:", row)
    mycursor.execute("INSERT INTO LegacySite_user (last_login, username, password) VALUES (%s, %s, %s)", (last_login, user, password))


for row in csv.reader(product_file):
	product_id = row[0]
	product_name = row[1]
	product_image_path = row[2]
	recommended_price = row[3]
	description = row[4]

	print("Loading row:", row)
	mycursor.execute("INSERT INTO LegacySite_product (product_id, product_name, product_image_path, recommended_price, description) VALUES (%s, %s, %s, %s, %s)", (product_id, product_name, product_image_path, recommended_price, description))




mydb.commit()
print("Done!")
