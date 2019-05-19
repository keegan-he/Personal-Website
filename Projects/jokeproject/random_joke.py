import requests

url = ('http://api.icndb.com/jokes/random')
response = requests.get(url)
data = response.json()
joke = data["joke"]
print(data)
#print(joke)