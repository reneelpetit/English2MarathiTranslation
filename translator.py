import requests
import config

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = {
    'q' : '',
    'target' : 'mr',
    'source' : 'en'}
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-key': config.api_key,
    'x-rapidapi-host': "google-translate1.p.rapidapi.com"
    }

payload['q'] = input("Type what you want translated: ")

response = requests.request("POST", url, data=payload, headers=headers)

json_object = response.json()
translated_text = json_object['data']['translations'][0]
print("The translation is: ", translated_text.get('translatedText'))