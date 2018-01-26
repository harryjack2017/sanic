import requests


r = requests.get("https://www.douban.com/")
print(r.status_code)

# print(r.text)
search = "https://www.douban.com/search"
r=requests.get(search, params={"q": "python", "cat": "1001"})

print(r.url)
print(r.encoding)

print(r.content)


r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})

print(r.text)


print(r.headers)

r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})

print(r.status_code)
cs = {'token': '12345', 'status': 'working'}

