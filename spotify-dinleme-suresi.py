import json
months = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]

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

msEachMonth = {}
for i in(jsonList):
    if( i["endTime"][:4]  in  msEachMonth.keys()):
        if(months[int(i["endTime"][5:7])-1] in msEachMonth[i["endTime"][:4]].keys()):
            msEachMonth[i["endTime"][:4]][months[int(i["endTime"][5:7])-1]] += i["msPlayed"]
        else:
            msEachMonth[i["endTime"][:4]][months[int(i["endTime"][5:7])-1]] = i["msPlayed"]
    else:
        msEachMonth[i["endTime"][:4]] = {months[int(i["endTime"][5:7])-1]:i["msPlayed"]}


for j in(msEachMonth.keys()):
    for k in(msEachMonth[j].keys()):
        print(f"\n{j} yılının {k}{(8-len(k))*' '} ayında {int(msEachMonth[j][k]/60000)}{(6-len(str(int(msEachMonth[j][k]/60000))))*' '} dakika",end="")

print(" müzik dinlediniz.")    
