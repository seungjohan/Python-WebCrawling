import requests
from bs4 import BeautifulSoup


res = requests.get("https://www.google.com/search?sxsrf=ALeKk01zreiakgUn68k-YghojJtm3QBZXQ:1628677306134&q=showtimes&stick=H4sIAAAAAAAAAOPg3cDI-IhRnlvg5Y97wlJik9acvMYowMXnm1-WmRqckV9ekpmbWsyziJWzGMYBAK98tN0zAAAA&npsic=0&sxsrf=ALeKk01zreiakgUn68k-YghojJtm3QBZXQ:1628677306134&ved=2ahUKEwjemaTi36jyAhWPfd4KHf5bDmsQ0CsoADAUegQIARAy")
res.raise_for_status

soup = BeautifulSoup(res.text, "lxml")

genres = soup.find_all("div", attrs={"class":"znKVS"})

# for i in genres:
#     genres_list[i] = genres
#     print("genre_{}".format(genres_list[i]))
for idx, genre in enumerate(genres):
    genre_list = genre.get_text()
    print(genre)


images=soup.find_all("g-img", attrs={"class": "BA0A6c"})


for image in images:
    print(images["src"])

    image_url = image["src"]

    if image_url.startswith("//"):
        image_url = "https" + image_url




# switch문으로