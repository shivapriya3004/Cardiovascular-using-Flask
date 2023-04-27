import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':3,'gender':1,'height':3,'weight':5,'ap_hi':3,'ap_lo':3})

print(r.json())
