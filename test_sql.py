import mysql.connector 

# enter your server IP address/domain name
# HOST = "192.168.86.30" # or "domain.com"
HOST = "localhost" # or "domain.com"
# database name, if you want just to connect to MySQL server, leave it empty
DATABASE = "foodb"
# this is the user you create
USER = "root"
# user password
PASSWORD = "test"
# connect to MySQL server
cnx = mysql.connector.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
print("Connected to:", cnx.get_server_info())
# enter your code here!

# SQL Query 1:
cursor = cnx.cursor()
query = (f"SELECT DISTINCT c.name FROM compounds AS c INNER JOIN compound_synonyms AS cs ON c.id=cs.source_id WHERE cs.synonym LIKE '%s%'")
cursor.execute(query, ('%dextrose%'))
name_list = []
for (name) in cursor:
    print(name)
    name_list.append(name[0])
cursor.close()










cnx.close()
