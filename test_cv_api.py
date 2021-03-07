import os

# [START vision_fulltext_detection]
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
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    # remove words with any french
                    exit_early = False
                    try:
                        for language in word.property.detected_languages:
                            if 'fr' == language.language_code:
                                exit_early = True
                                break
                    except:
                        pass
                    if exit_early:
                        pass
                    # if word.property:
                    #     if word.property.detected_languages:
                    #         for language in word.property.detected_languages:
                    #             # breakpoint()
                    #             if language.language_code:
                    #                 # breakpoint()
                    #                 if 'fr' == language.language_code:
                    #                     # breakpoint()
                    #                     continue
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
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


def test():
    # The name of the image file to annotate
    file_name = os.path.abspath('hashbrowns_ingredients.jpeg')
    response = detect_document(path=file_name)
    return response

file_name = os.path.abspath('hashbrowns_ingredients.jpeg')
response = detect_document(path=file_name)
print(response)