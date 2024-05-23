import requests
import time

url = "https://moakt.com/ar/inbox/extend"

payload = "getJson=true"

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36",
  'Accept': "application/json, text/javascript, */*; q=0.01",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'sec-ch-ua': "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
  'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
  'x-requested-with': "XMLHttpRequest",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'origin': "https://moakt.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://moakt.com/ar/inbox",
  'accept-language': "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,tr;q=0.6",
  'priority': "u=1, i",
  'Cookie': "__gads=ID=1d223ca717efeadc:T=1709239555:RT=1716226450:S=ALNI_Ma6Cp3tFOzfUR0cdX4GXo4XCL1A8g; __gpi=UID=00000d373df316dc:T=1709239555:RT=1716226450:S=ALNI_MZechVD-lq-3ECTKieSVLaJTEFDuQ; __eoi=ID=8b881da4c3755c5f:T=1709239555:RT=1716226450:S=AA-Afjbgz9J7pBxKE5yRxVDSEARl; __utmz=213295240.1716310207.25.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=213295240.1559448545.1709239546.1716310207.1716314768.26; tm_session=dee6bdd57854f3fd7a4afb696bf717d3"
}
while True:
 response = requests.post(url, data=payload, headers=headers)

 print(response.text)
 time.sleep(30*60)
