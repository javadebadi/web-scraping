import requests

url = "https://en.wikipedia.org/wiki/List_of_HTTP_status_codes"

header = {
    "From":"Javad Ebadi <javadebadi@ipm.ir"
}

response = requests.get(url, header = header)
if response.status_code != 200:
    print("Failed to get HTML: ",
            response.status_code, response.reason)
    exit()

html = response.text
print(html)
