import requests 

API_KEY = 'AIzaSyCV1daJ_OQsgUTWpGw2nnbKeCZB8aQk3KU'
SEARCH_ENGINE_ID = '54babb708747d40ce'
query = input('What do you want to search?: ')

url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={SEARCH_ENGINE_ID}"

response = requests.get(url) #sends http request to the url above
data = response.json() #converts response from json into python object (so now can access it using syntax)

for i, item in enumerate(data.get("items")[:10], start=1): #looks for items in the main json directory which contains the title data
    print(f"{i}. {item['title']}") #goes inside the items folder and extracts the titles inside that directory