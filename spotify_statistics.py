import json
months = ["Ocak","Şubat","Mart","Nisan","Mayıs","Haziran","Temmuz","Ağustos","Eylül","Ekim","Kasım","Aralık"]

jsonList = []
i=0
while(True):
    try:
        fileName = f"StreamingHistory{i}.json"
        file = open(fileName,"r")
        jsonList.extend(json.loads(file.read()))
        file.close()
        i+=1
    except:
        break

msEachMonth = {}
artistCount = {}
for i in(jsonList):

    if(i["artistName"] in artistCount.keys()):
        artistCount[i["artistName"]][0] += 1
        artistCount[i["artistName"]][1] += i["msPlayed"]
        if(i["trackName"] in artistCount[i["artistName"]][2].keys()):
            artistCount[i["artistName"]][2][i["trackName"]][0] += 1
            artistCount[i["artistName"]][2][i["trackName"]][1] += i["msPlayed"]
        else:
            artistCount[i["artistName"]][2][i["trackName"]] = [1, i["msPlayed"]]
    else:
        artistCount[i["artistName"]] = [1, i["msPlayed"],{i["trackName"]:[1, i["msPlayed"]]}]


    if( i["endTime"][:4]  in  msEachMonth.keys()):
        if(months[int(i["endTime"][5:7])-1] in msEachMonth[i["endTime"][:4]].keys()):
            msEachMonth[i["endTime"][:4]][months[int(i["endTime"][5:7])-1]] += i["msPlayed"]
        else:
            msEachMonth[i["endTime"][:4]][months[int(i["endTime"][5:7])-1]] = i["msPlayed"]
    else:
        msEachMonth[i["endTime"][:4]] = {months[int(i["endTime"][5:7])-1]:i["msPlayed"]}

artistCount = sorted(artistCount.items(),key= lambda x: x[1][1], reverse= True)
print(artistCount[0])
statsFile = open("listening_statistics.txt", "wt")

for i in artistCount:
    if(int(i[1][1]/60000) > 0):
        statsFile.write(f"{i[0]}{(70-len(i[0])) * ' '} {i[1][0]}{(6-len(str(i[1][0])))*' '} kez {int(i[1][1]/60000)}{(6 - len(str(int(i[1][1]/60000)))) * ' '} dakika\n")
        statsFile.write("\n")
        songCount = sorted(i[1][2].items(), key= lambda x: x[1][1], reverse=True)
        for j in songCount:
            if(int(j[1][1]/60000) > 0):
                statsFile.write(f"{5 * ' '}{j[0][:65]}{(70-len(j[0][:65])) * ' '} {j[1][0]}{(6-len(str(j[1][0])))*' '} kez {int(j[1][1]/60000)}{(6 - len(str(int(j[1][1]/60000)))) * ' '} dakika\n")
    statsFile.write("\n\n")    

statsFile.close()

for j in(msEachMonth.keys()):
    for k in(msEachMonth[j].keys()):
        print(f"\n{j} yılının {k}{(8-len(k))*' '} ayında {int(msEachMonth[j][k]/60000)}{(6-len(str(int(msEachMonth[j][k]/60000))))*' '} dakika",end="")

print(" müzik dinlediniz.")
