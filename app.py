import streamlit as st
import requests
import time
import threading

# Function to make the requests in a loop
def keep_awake():
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
        'Cookie': "__gads=ID=1d223ca717efeadc:T=1709239555:RT=1716226450:S=ALNI_Ma6Cp3tFOzfUR0cdX4GXo4XCL1A8g; __gpi=UID=00000d373df316dc:T=1709239555:RT=1716226450:S=ALNI_MZechVD-lq-3ECTKieSVLaJTEFDuQ; __eoi=ID=8b881da4c3755c5f:T=1709239555:RT=1716226450:S=AA-Afjbgz9J7pBxKE5yRxVDSEARl; __utmz=213295240.1716310207.25.7.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utma=213295240.1559448545.1709239546.1716549903.1716629676.29; __utmc=213295240; __utmt=1; __utmb=213295240.1.10.1716629676; tm_session=4d15fa8ffeaf6063fa628ce7ec92643f"
    }
    while True:
        response = requests.post(url, data=payload, headers=headers)
        print(response.text)  # Print the response to the console (useful for debugging)
        time.sleep(30 * 60)  # Wait for 30 minutes before sending the next request

# Streamlit app layout
st.title("Keep Awake Script")

# Button to start the script
if st.button('Start Script'):
    st.write("Script started. It will run in the background and keep sending requests every 30 minutes.")
    threading.Thread(target=keep_awake).start()
