import urllib.request, urllib.parse, urllib.error
import json


url= input("Enter Url:")
#if len(url) < 1 : break
print('Retrieving', url)

connection=urllib.request.urlopen(url)
data=connection.read()

print ('Retrieving', len(data),'characters')

js=json.loads(data)

count=0
sum=0

for i in js['comments']:
        count=count+1
        sum=sum+i['count']

print ("Sum : ", sum)
print ("Count : ", count)
