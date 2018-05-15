import json
import requests


def table_json(url) -> str:
    # url = 'http://localhost/api/g?p=test'

    s = ''

    r = requests.get(url)

    print(r.text)
    j: {} = r.json()

    p = list(j.keys()) [0]

    for i in j [p]:
        s = s + i + '</br>'

    return s


if __name__ == '__main__':
    # test
    table_json('http://localhost/api/g?p=test')
