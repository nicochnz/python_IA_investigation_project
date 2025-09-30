import requests
from bs4 import BeautifulSoup
from ollama import generate

res = requests.get("https://tldr.tech/webdev/2025-09-29")
parser = BeautifulSoup(res.text, "html.parser")

for desc in parser.find_all("div", "newsletter-html"):
  print(desc.get_text())
  res = generate(model='gemma3:latest',
               prompt=f'write me a ten word summary of this article {desc.get_text()}', stream=False)
  print(f"synthèse par IA: {res.response}")
  break

# Trouver comment scraper la page avec bs4
