import requests, json

url ='https://jsonplaceholder.typicode.com/users'
print('Ingrese la ciudad de donde quiere buscar un usuaruio:')
citi = input()
city = citi.capitalize()

usersInCity = []
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    for i in range(10):
        if city == data[i]['address']['city']:
            print(f"El usuario {data[i]['name']} si esta en {city}")
            usersInCity.append(data[i])
        else:
            print(f"El usuario {data[i]['name']} no esta en {city}")

with open('./Recup/Data/filteredUsers.json', 'w') as archivo:
    json.dump(usersInCity, archivo)