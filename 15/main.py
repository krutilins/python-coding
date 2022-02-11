"""rifme generator"""
import requests

r = requests.get('https://rifmus.net/rifma/%D0%B4%D0%B2%D0%B0%D0%B4%D1%86%D0%B0%D1%82%D1%8C', auth=('user', 'pass'))
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.text)
print(r.json())