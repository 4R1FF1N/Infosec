import requests 

url = ( 
    "https://google.com",
    "https://google.co.uk"
)

for x in url:
    requests.get(x)
    print(x)
