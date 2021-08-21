import requests
from bs4 import BeautifulSoup


for year in range(2012, 2021) :
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={}%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84".format(year)

    res = requests.get(url)
    res.raise_for_status

    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thum_msk"})

    for idx, image in enumerate(images):
        image_url = image["src"]
        print(image["src"])

        if image_url.startswith("//"):
            image_url = "https" + image_url