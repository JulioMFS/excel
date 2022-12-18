import requests

# Making a GET request
#r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
r = requests.get('http://osae.pt/pt/pesquisas/1/1/1')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)

print(r.url)
print(r.status_code)
