import requests
from bs4 import BeautifulSoup

url ="https://www.eltiempo.es/barcelona.html"

response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find('span', {'class': 'Temperatura'})
    
    if links:
        print(temperatura = links.text)
    else:
        print("No encontró la temperatura en la página")


    # for link in links:
    #     print (link.text)
else:
    print("Error ak acceder a la página", response.status_code)