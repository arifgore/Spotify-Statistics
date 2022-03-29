import json

jsonList = []
i=0
while(True):
    try:
        fstring = f"StreamingHistory{i}.json"
        f = open(fstring,"r")
        jsonList.extend(json.loads(f.read()))
        f.close()
        i+=1
    except:
        break

msEachYear = {}

for i in(jsonList):
    if( i["endTime"][:4]  in  msEachYear.keys()):
        msEachYear[i["endTime"][:4]] += i["msPlayed"]
    else:
        msEachYear[i["endTime"][:4]] = i["msPlayed"]

for j in(msEachYear.keys()):
    print(f"\n{j} yılında {int(msEachYear[j]/60000)} dakika",end="")

print(" müzik dinlediniz.")    
