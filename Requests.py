#To know more about requests
import  requests

response = requests.get('https://www.goodreturns.in/gold-rates/') #Specify the URL you want to scrape and Send a HTTP request to the specified URL and save the response from server in a response object called response.
response_json = response.json
print(response.text)
