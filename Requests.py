#To know more about requests
import  requests

response = requests.get('https://github.com/')
response_status = response.status_code
response_json = response.json
print(response.text)
