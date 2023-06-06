import requests
website = "https://jsonplaceholder.typicode.com/posts/2"
print(requests.get(website).json())
response = requests.put(website, json={
    "userId": 2,
    "id": 2,
    "title": "Hello",
    "body": "Hello World"
    })
print(response.json())
