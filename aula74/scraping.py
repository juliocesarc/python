from urllib import response
import requests
from bs4 import BeautifulSoup


url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.s-post-summary'):
    titulo = pergunta.select_one('.s-link')
    hora = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.s-post-summary--stats-item-number')
    print(titulo.text)
    print(hora.text)
    print(votos.text)