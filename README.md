# Spotify Dinleme İstatistikleri
https://www.spotify.com/tr/account/privacy/ adresinden oluşturduğunuz talep üzerine size gelen mail aracılığıya indirdiğiniz Spotify verilerinizi
kullanarak hangi ay kaç dakika müzik dinlediğinizi ekrana bastırır. Ek olarak her bir sanatçı ve her bir parçayı kaç kez ve kaç dakika dinlediğinizi listening_statistics.txt isimli dosyaya yazar. (!!!Dizinin içinde aynı isimde dosya varsa üstüne yazılacaktır.)

spotify_statistics.py dosyasını, indirdiğiniz zip dosyasını açtığınızda oluşan dizinin içine kopyalayıp oradan çalıştırmanız yeterlidir.

Linux:
```
python3 spotify_statistics.py
```
Windows (python kurulumu gereklidir.):
```
python spotify_statistics.py
```

# Spotify Listening Statistics

The script prints how many minutes you have listened to music on Spotify per month last one year, using the data you requested from https://www.spotify.com/tr/account/privacy/. It also calculates how many times and how many minutes you listened to artists and songs, than writes this information to the file named listening_statisctics.txt. (!!!If a file with this name already exists, it will be overwritten.)

You just need to copy the file named spotify_statistics.py to the directory which you extracted from the zip file that you have downloaded.

Linux:
```
python3 spotify_statistics.py
```
Windows (python installation is required.):
```
python spotify_statistics.py
```