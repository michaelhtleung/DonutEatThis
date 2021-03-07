import common_words

import os
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

payload = {
    'ingredients': []
}

def detect_document(path):
    """Detects document features in an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    # [START vision_python_migration_document_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    result = []

    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            # print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                # print('Paragraph confidence: {}'.format(paragraph.confidence))

                for word in paragraph.words:
                    # breakpoint()
                    # remove words with any french
                    exit_early = False
                    try:
                        if 'fr' in str(word.property.detected_languages):
                            exit_early = True
                            break
                    except:
                        pass
                    if exit_early:
                        pass
                    

                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ]).lower()
                    # remove common words
                    cw = common_words.get_common_words()
                    if word_text in cw:
                        continue

                    # remove common baking words
                    cw = {'preheat', 'minutes', 'pendan', 'flip', 'patties', 'colour', 'fermes', 'caven', 'modified', 'starch', 'sodium',  'dieppe', 'annan', 'canada', 'trademarks', 'cavendish', 'farms', 'rights', 'reserved'}
                    if word_text in cw:
                        continue

                    # print('Word text: {} (confidence: {})'.format(
                    #     word_text, word.confidence))
                    if word.confidence > 0.90:
                        result.append(word_text)
    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    # return response
    return result
    # [END vision_python_migration_document_text_detection]
# [END vision_fulltext_detection]

# TODO: replace with request data received in middleware
# The name of the image file to annotate
file_name = os.path.abspath('hashbrowns_ingredients.jpeg')
search_term_list = detect_document(path=file_name)

def isEnglish(s):
    # Taken from:https://stackoverflow.com/questions/27084617/detect-strings-with-non-english-characters-in-python
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

# remove filler words:

# import nltk
# words = set(nltk.corpus.words.words())
# search_term_list = [nltk.wordpunct_tokenize(s).lower() for s in search_term_list]
# search_term_list = [s for s in search_term_list if isEnglish(s) and len(s) >= 4 and s in words]
# search_term_list = [nltk.wordpunct_tokenize(s) for s in search_term_list]

search_term_list = [s for s in search_term_list if isEnglish(s) and len(s) >= 4]
print(f"search_term_list: {search_term_list}")

from tqdm import tqdm
for search_term in tqdm(search_term_list):
    # SQL Query 1:
    cursor = cnx.cursor()
    query = (f"SELECT DISTINCT c.name FROM compounds AS c INNER JOIN compound_synonyms AS cs ON c.id=cs.source_id WHERE cs.synonym LIKE '%{search_term}%'")
    cursor.execute(query)
    name_list = []
    for (element) in cursor:
        element = element[0]
        # print(element)
        name_list.append(element)
    cursor.close()
    if len(name_list) == 0:
        continue

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
    cursor.close()
    # print(f'subclass: {subclass}')
    if subclass == None:
        continue

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
    # print(f'effects: {effects}') # list of str
    cursor.close()
    if len(effects) == 0:
        continue

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
    # print(f'is_healthy: {is_healthy}')

    payload['ingredients'].append({
        'formal_name': search_term,
        'score': sentiment.score,
        'synonym': subclass,
        # 'links': "placeholder link",
        # 'link_image_data': 'placeholder image data',
    })

cnx.close()

print(payload)

import json
with open('data.json', 'w') as outfile:
    json.dump(payload, outfile)
