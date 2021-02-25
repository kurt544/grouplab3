import urllib.request

print('Beginning download...')

url = 'https://s3.amazonaws.com/tcmg476/http_access_log' 

urllib.request.urlretrieve(url, 'http.log')

