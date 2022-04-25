import requests
import time
import json
import pandas

file_path = str(input('please Enter The File Path: '))

domain_CSV = pandas.read_csv((file_path))
Urls = domain_CSV['URL'].tolist()

API_key = '  '      # Your API key  
url = 'https://www.virustotal.com/vtapi/v2/url/report'


parameters = {'apikey': API_key, 'resource': Urls}

for i in Urls:
    parameters = {'apikey': API_key, 'resource': i}

    response= requests.get(url=url, params=parameters)
    json_response= json.loads(response.text)
    positives = int(json_response.get('positives'))
    if json_response['response_code'] <= 0:
        with open('not Found result.txt', 'a')  as notfound:
            notfound.write(i) and notfound.write("\tNOT found please Scan it manually\n")
    elif json_response['response_code'] >= 1:

        if json_response['positives'] <= 0:
            with open('Virustotal Clean result.csv', 'a')  as clean:
                clean.write(i) and clean.write("\t\t\t NOT Malicious \n")
        else:
            with open('Virustotal Malicious result.csv', 'a')  as malicious:
                malicious.write(i) and malicious.write("\t\t\t\t Malicious") and malicious.write("\t\t\t\t This Domains Detected by   "+ str(json_response['positives']) + "  Solutions\n")

    time.sleep(15)