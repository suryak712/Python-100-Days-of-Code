from bs4 import BeautifulSoup

from selenium import webdriver

with open("bs4-start/website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)
# print(soup.find_all("a"))
print(soup.find(name="h1", id="name"))  # Find the h1 element with id "name"
print(soup.select_one(selector="p a"))  # Find the first anchor tag inside a paragraph
print(soup.select(selector=".heading"))  # Find all elements with the "heading" class