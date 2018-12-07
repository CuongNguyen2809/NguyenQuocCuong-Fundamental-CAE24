from urllib.request import urlopen
import json

url = "https://wind.waqi.info/nsearch/full/hanoi?n=4"

#1 . Open conection
conn = urlopen(url) # mo ket noi toi duong link

#2 . Read data
raw_data = conn.read()  # thao tac doc du lieu 


#3 . Decode data (giai ma data)
text = raw_data.decode("utf-8")

#4. Covert data from str to dict
data = json.loads(text)


results = data["results"]
result = results[1]
# print(result["s"]["a"])
# print(result["s"]["n"][0])
print(result["s"]["a"])
print(result["s"]["n"][0])