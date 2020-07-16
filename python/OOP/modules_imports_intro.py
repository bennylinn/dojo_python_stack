import urllib.request as request
import arithmetic as ar

response = request.urlopen("http://www.codingdojo.com")
html = response.read()

print(ar.Arithmetic.add(3, 3))

