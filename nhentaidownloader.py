import requests as req
from bs4 import BeautifulSoup
import os
print("輸入號碼後，會創建一個資料夾並將圖片下載至裡面。若已有同名資料夾，請刪除該資料夾後重新執行程式。")
num = input("輸入n網本子號碼:")
murl = 'https://nhentai.net/g/'+num+'/1/'
r = req.get(murl)
soup = BeautifulSoup(r.text, 'html.parser')
page = soup.find('span', attrs={"class": "num-pages"})
os.mkdir(num)
os.chdir(os.getcwd()+"/"+num)
for i in range(1, int(page.string)+1):

    url = 'https://nhentai.net/g/'+num+'/'+str(i)+'/'
    r1 = req.get(url)
    a = BeautifulSoup(r1.text, 'html.parser')
    pic = a.find_all(["img", "src"])
    images = pic
    image = images[1]
    picurl = image.get("src")
    file = req.get(picurl)
    open(str(i)+'.jpg', 'wb').write(file.content)
    print("下載進度:("+str(i)+"/"+str(page.string)+")")
print("下載完成!，請關閉視窗")
