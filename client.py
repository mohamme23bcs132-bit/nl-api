import json 
import requests

data={'features':[1,2,3,4,5]}

url='http://localhost:8000/predict'
data_json=json.dumps(data)
response=requests.post(url,data=data_json)
print(response.json())