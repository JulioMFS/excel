import urllib.request
import urllib
import json

url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"

query = input("What do you want to search for ? >> ")

query = urllib.urlencode( {'q' : query } )

response = urllib.urlopen (url + query ).read()

data = json.loads ( response )

results = data [ 'responseData' ] [ 'results' ]

for result in results:
    title = result['title']
    url = result['url']
    print ( title + '; ' + url )