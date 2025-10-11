import requests 

API_KEY = 'AIzaSyCV1daJ_OQsgUTWpGw2nnbKeCZB8aQk3KU'
SEARCH_ENGINE_ID = '54babb708747d40ce'
query = input('What do you want to search?: ')

url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={SEARCH_ENGINE_ID}"
#url is googles custom search API
response = requests.get(url) #sends http request to the url above
data = response.json() #converts response from javascript into python object (so now can access it using syntax)

items = data.get("items")
first = items[0]
second = items[1]
third = items[2]
fourth = items[3]
fifth = items[4]
sixth = items[5]
seventh =  items[6]
eigth = items[7]
ninth = items[8]
tenth = items[9]
print(first['title'])
print(second['title'])
print(third['title'])
print(fourth['title'])
print(fifth['title'])
print(sixth['title'])
print(seventh['title'])
print(eigth['title'])
print(ninth['title'])
print(tenth['title'])

