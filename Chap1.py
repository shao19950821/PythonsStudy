import requests
res=requests.get("https://www.baidu.com/")
savefile=open("baidu.html","wb+")
savefile.write(res.content)
savefile.close()