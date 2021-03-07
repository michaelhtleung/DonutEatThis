import requests

def test():
    # r = requests.get('https://api.github.com/events')
    # print(r)

    r = requests.get('https://foodb.ca/api/v1/compoundreport/compound')
    # print(r)
    return r