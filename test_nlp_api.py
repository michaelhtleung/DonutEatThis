from google.cloud import language_v1


# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
# words = ['pas', 'recongeler', '.', 'Nous', 'recommended', 'for', "d'assurer", 'la', 'qualité', 'du', 'OVEN', 'MODE', '10', '2.', 'Dispose', 'seule', '450', '1.', 'Preheat', 'is', 'Préchau', '2.', 'Spread', 'of', 'patties', 'on', 'a', 'sheet', 'and', 'bake', 'for', '10', 'minutes', '.', 'pendan', '3.', 'Flip', 'patties', 'over', '.', '3.', 'Retour', '4.', 'Continue', 'baking', 'for', '7-10', 'minutes', '7-10', 'minute', 'to', 'a', 'light', 'golden', 'colour', 'légère', 'INGREDIENTS', ':', 'POTATOES', ',', 'VEGETABLE', 'OIL', '(', 'SOYBEAN', 'Cavendish', 'Farms', 'OIL', 'AND', '/', 'OR', 'CANOLA', 'OIL', ')', 'YELLOW', 'CORN', 'FLOUR', ',', 'Les', 'Fermes', 'Caven', 'MODIFIED', 'POTATO', 'STARCH', 'SALT', ',', 'DEXTROSE', ',', 'SODIUM', 'ACID', 'PYROPHOSPHATE', 'Dieppe', ',', 'NB', 'INGRÉDIENTS', ':', 'POMMES', 'DE', 'TERRE', ',', 'HUILE', 'VÉGÉTALE', 'PROUDLY', 'PRODU', '(', 'DE', 'SOYA', 'ET', '/', 'OU', 'HUILE', 'DE', 'CANOLA', ')', ',', 'FARINE', 'New', 'Annan', ',', 'PE', ',', 'W', 'DE', 'JAUNE', ',', 'AMIDON', 'DE', 'POMMES', 'DE', 'TERRE', 'MODIFIÉ', ',', 'SEL', ',', 'DEXTROSE', 'PYROPHOSPHATE', 'ACIDE', 'Prepared', 'DE', 'SODIUM', 'in', 'Canada', 'TM', '/', '*', 'Trademarks', 'of', 'Cavendish', 'Farms', 'Corporation', '.', 'All', 'Rights', 'Reserved', '.', 'MC', '/', 'Marques', 'de', 'commerce', 'Les', 'Fermes', 'Cavendish', 'Incorporée', '.', 'Tous', 'les', 'droits', 'sont', 'réservés', '.', 'SATISFACTION', '100', '%', 'DE', 'SATISFACTION', 'Find', 'recipe', 'inspi', 'cavendishfarms', 'des', 're']

text = u"Goodbye, world!"
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
