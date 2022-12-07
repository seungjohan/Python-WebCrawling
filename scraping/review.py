import requests
from bs4 import BeautifulSoup

# url = "http://blog.naver.com/tmdwh7275"
# headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
# res = requests.get(url, headers=headers)
# print("responseCode :", res.status_code)
#
# # if res.status_code == requests.status_codes.ok:
# #     print("No Error")
# # else:
# #     print("Error")
#
# res.raise_for_status()
# print(res.text)
#
# with open("blog_naver.html", "w", encoding="utf8") as f:
#     f.write(res.text)



# print(soup.title.get_text)
# print(soup.a)
# print(soup.a.attrs)
# print(soup.a["href"])
#
# print(soup.find(attrs={"class":"Nbtn_upload"}))
# print(soup.find("li", attrs={"class":"rank01"}))

# urlnaver = "https://comic.naver.com/webtoon/weekday"
# res = requests.get(urlnaver)
# res.raise_for_status()
#
# soup = BeautifulSoup(res.text, "lxml")
#
# cartoons = soup.find_all("a", attrs={"class":"title"})
# for cartoon in cartoons:
#     print(cartoon.get_text())



urlkakao = "https://webtoon.kakao.com/original-webtoon?tab=wed"
res = requests.get(urlkakao)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
webtoons = soup.find_all("a", attrs={"href":"title"})
for webtoon in webtoons:
    print(webtoon.get_text())