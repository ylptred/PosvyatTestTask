from bs4 import BeautifulSoup
import requests
from flask import Flask
import random

url = 'https://anekdoty.ru/pro-programmistov/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
results = soup.find_all('p')
anecks = []

for result in results:
    anecks.append(result.text)

app = Flask(__name__)

@app.route("/")
def text():
    while True:
        random_index = random.randint(0, len(anecks) - 1)
        return "Держи рандомный анекдот: " + '\n' + anecks[random_index]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)
