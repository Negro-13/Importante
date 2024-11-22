import json, requests

url = 'https://jsonplaceholder.typicode.com/posts'

print('Ingrese el id del usuario:')
idUser = int(input())
print('Ingrese la palabra con la q quiera buscar en los post')
word = input()
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    i = 0
    cantTotal = 0
    for i  in range(100):
        if data[i]['userId'] == idUser :
            cantTitle = data[i]['title'].count(word)
            cantPost =  data[i]['body'].count(word)
            cantTotal += cantPost + cantTitle
    print(f"En los post del usuario id {idUser}, contiene {cantTotal} veces la palabra {word}")