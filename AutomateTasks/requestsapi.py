import requests

response = requests.get('http://automatetheboringstuff.com/files/rj.txt')
response.raise_for_status()
playFile = open('Rj.txt', 'wb')
for chunk in response.iter_content(100000):
    playFile.write(chunk)
playFile.close()
