import request, json

url = ''
response = request.get(url)
if response.status_code == 200:
    