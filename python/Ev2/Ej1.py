import requests, json

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

def isPrime(n):
    if n == 3 or n == 2:
        return True
    for i in range(2, n-1):
        if n % i != 0:
            return True
        else:
            return False

if response.status_code == 200:
    idPrime = []
    idNoPrime = []
    data = response.json()
    print('Ingrese una cantidad de posts entre 1 y 100')
    cantPosts = int(input())
    if cantPosts >= 1 and cantPosts <= 100:
        for i in range(cantPosts):
            if isPrime(data[i]['id']) == True:
                idPrime.append(data[i])
            else:
                idNoPrime.append(data[i])
    else:
        print('Seleccione un numero entre 1 y 100')
        cantPosts = int(input())

with open('./Ev2/Descargas/dlXPrimes.json', 'w') as archivo:
    json.dump(idPrime, archivo)
with open('./Ev2/Descargas/dlXNotPrimes.json', 'w') as archivo:
    json.dump(idNoPrime, archivo)
