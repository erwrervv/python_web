import requests

# GET
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())

# POST
payload = {'name':'Kevin', 'age':30}
response = requests.post("https://httpbin.org/post", json=payload)
print(response.json())

# PUT
response = requests.put("https://httpbin.org/put", json={'update':'data'})
print(response.json())