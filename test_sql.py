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
search_term = 'dextrose'

# # SQL Query 1:
# cursor = cnx.cursor()
# query = (f"SELECT DISTINCT c.name FROM compounds AS c INNER JOIN compound_synonyms AS cs ON c.id=cs.source_id WHERE cs.synonym LIKE '%{search_term}%'")
# cursor.execute(query)
# name_list = []
# for (element) in cursor:
#     element = element[0]
#     print(element)
#     name_list.append(element)
# cursor.close()

# SQL Query 2:
cursor = cnx.cursor()
query = (f"SELECT DISTINCT c.subklass FROM compounds AS c INNER JOIN compound_synonyms AS cs ON c.id=cs.source_id WHERE cs.synonym LIKE '%{search_term}%'")
cursor.execute(query)
subclass = None
for (element) in cursor:
    element = element[0]
    # print(element)
    # if the first word is 21 letters long, that's probably not the one we want to keep
    if element != 'NULL' and element != 'None' and element != None and len(element.split(' ')[0]) < 20:
        subclass = element
print(f'subclass: {subclass}')
cursor.close()

# SQL Query 3:
cursor = cnx.cursor()
query = (f"SELECT DISTINCT he.description FROM compounds AS c INNER JOIN compound_synonyms AS cs ON c.id=cs.source_id INNER JOIN compounds_health_effects AS che ON c.id=che.compound_id INNER JOIN health_effects AS he ON he.id=che.health_effect_id WHERE cs.synonym LIKE '%{search_term}%'")
cursor.execute(query)
effects = []
for (element) in cursor:
    element = element[0]
    # print(element)
    if element != 'NULL' and element != 'None' and element != None:
        effects.append(element)
print(f'effects: {effects}') # list of str
cursor.close()

# Sentiment Analysis:
from google.cloud import language_v1
# Instantiates a client
client = language_v1.LanguageServiceClient()
effects = ''.join(effects)
document = language_v1.Document(content=effects, type_=language_v1.Document.Type.PLAIN_TEXT)
# Detects the sentiment of the text
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
# print("Text: {}".format(effects))
# print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
is_healthy = None
if sentiment.score >= 0:
    is_healthy = True
else:
    is_healthy = False
print(f'is_healthy: {is_healthy}')
    






cnx.close()
