import json

f = open("StreamingHistory7.json","r")
json1 = json.loads(f.read())
f.close()
f = open("StreamingHistory8.json","r")
json2 = json.loads(f.read())
f.close()
f = open("StreamingHistory9.json","r")
json3 = json.loads(f.read())
f.close()

ms = 0
for i in(json1):
    if(i["endTime"][3]=="2"):
        ms += i["msPlayed"]
for i in(json2):
    if(i["endTime"][3]=="2"):
        ms += i["msPlayed"]
for i in(json3):
    if(i["endTime"][3]=="2"):
        ms += i["msPlayed"]     

print(ms/1000/60/60/24)        
