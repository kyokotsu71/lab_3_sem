import requests

link = "https://example.com"


def request(m, url, data=None):
    res = None
    if m == 'GET':
        res = requests.get(url)
    elif m == 'OPTIONS':
        res = requests.options(url)
    elif m == 'POST':
        res = requests.post(url, data=data)

    print(f'Метод: {m}')
    if data:
        print(f'Тело: {data}')
    print(f'Код: {res.status_code}')
    print(f'Заголовки: {res.headers}')
    print(f'Тело: {res.text}')


request('GET', link)
request('OPTIONS', link)
request('POST', link, '123')

