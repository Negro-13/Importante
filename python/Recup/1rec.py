import requests, json
print('Ingrese la cantidad de posts deseados')
cantposts = int(input())

url = 'https://jsonplaceholder.typicode.com/users'
response = requests.get(url)

userVocal = []
userCons = []
if response.status_code == 200:
    data = response.json()
    for i in range(cantposts):
        if data[i]['name'].startswith('A') or data[i]['name'].startswith('E')  or data[i]['name'].startswith('I')  or data[i]['name'].startswith('O')  or data[i]['name'].startswith('U'):
            userVocal.append(data[i])
        else:
            userCons.append(data[i])
print(f'Los post de usuarios q su nombre comiencen con vocal son: {userVocal}')
with open('./Recup/Data/UsersVocal.json', 'w') as archivo:
    json.dump(userVocal, archivo)
print(f'Los post de usuarios q su nombre comiencen con consonantes son: {userCons}')
with open('./Recup/Data/UsersCons.json', 'w') as archivo:
    json.dump(userCons, archivo)