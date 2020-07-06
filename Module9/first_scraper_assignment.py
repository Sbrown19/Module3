import request
url = 'https://www.dmacc.edu/schedule/Pages/result.aspx?Term=2019034Campus=1;4&5
response = request.get(url)
html = response.content
f = open("requestResult.txt","w+")
f.writelines(str(html))
f.close()
