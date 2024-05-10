from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    num = request.json['phoneNumber']
    n = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6UXpRekpFTlVNeE16aEdOemcwUlRjeVF6VXdRVEkyTWpoRlJEZEROVE0xTVVNM1F6TTJPUSJ9.eyJodHRwczovL21hZi5ncmF2dHkuYXV0aC9kZXYvYXBpL2VtYWlsIjoiZ2RmZ2Zzc2Z0Z2NmeGZmQGpnZ3V1LmNvbSIsImh0dHBzOi8vbWFmLmlkZW50aXR5LmF1dGgvZGV2L2FwaS9lbWFpbCI6ImdkZmdmc3NmdGdjZnhmZkBqZ2d1dS5jb20iLCJodHRwczovL21hZi5pZGVudGl0eS5hdXRoL2Rldi9hcGkvcmlkIjoiNWZhNzQ2M2UtOTQxZi00YmZmLTg1M2QtYmU2MTBhNTc4NDdmIiwiaHR0cHM6Ly9tYWYuaWRlbnRpdHkuYXV0aC9kZXYvYXBpL21pcmFrbF9zaG9wX2lkIjpudWxsLCJodHRwczovL21hZi5pZGVudGl0eS5hdXRoL2Rldi9hcGkvdGltZSI6IjIwMjQtMDQtMjlUMTc6NTU6MDIuNjAzWiIsImh0dHBzOi8vbWFmLmdyYXZ0eS5hdXRoL2Rldi9hcGkvdXVpZCI6IjY3MGFhY2I2LTU4YjktNGEyNS1hMmVlLWRjNWJjYjk2ODk3OSIsImh0dHBzOi8vbWFmLmlkZW50aXR5LmF1dGgvZGV2L2FwaS91dWlkIjoiNjcwYWFjYjYtNThiOS00YTI1LWEyZWUtZGM1YmNiOTY4OTc5IiwiaHR0cHM6Ly9tYWYuaWRlbnRpdHkuYXV0aC9kZXYvYXBpL2VtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiaXNzIjoiaHR0cHM6Ly9wcm9kdWN0aW9uLm1hZi5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjYyZmRlZjYyMDMxZjU4MGQ3YzhmZDVhIiwiYXVkIjpbImh0dHBzOi8vcHJvZHVjdGlvbi5tYWYuYXV0aDAuY29tL2FwaS92Mi8iLCJodHRwczovL3Byb2R1Y3Rpb24ubWFmLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE3MTQ0MTMzMDIsImV4cCI6MTcxNzAwNTMwMiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCByZWFkOmN1cnJlbnRfdXNlciB1cGRhdGU6Y3VycmVudF91c2VyX21ldGFkYXRhIGRlbGV0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgY3JlYXRlOmN1cnJlbnRfdXNlcl9tZXRhZGF0YSBjcmVhdGU6Y3VycmVudF91c2VyX2RldmljZV9jcmVkZW50aWFscyBkZWxldGU6Y3VycmVudF91c2VyX2RldmljZV9jcmVkZW50aWFscyB1cGRhdGU6Y3VycmVudF91c2VyX2lkZW50aXRpZXMgb2ZmbGluZV9hY2Nlc3MiLCJndHkiOiJwYXNzd29yZCIsImF6cCI6ImNGdlJQMmN1QnhiM2l2Q0hkY1B5VGVYZmdUS3ZIV01hIn0.IszxGn-Lk6IaSprUAc8NFc6TmZas1vS7G_jkhcRHkI8gc8XcBeQnU4n2X6AcB6SEg1Gr8gGJIboV23cVj6Iul3aU8DaN8qF1KEpRwb7KkP6tCFAloJgv8QHuBP_1NV2_bgUBBXykJmhY6-8PnJKNHE3MHK1rD2q1Mk1f7c863oz-UJQWwcoZlGZHFAgZYrEpDQx3Ox0J5Pu2LXnMBafwYqxoWL4BueN-rfWhdN7Z3xgsd1ZFxUJkqkn5asXU5XFs6BgKengxIbduUJzy6JXRwpWXkVxro8uEkhScHjw7ojlW8GXG6_eSTmXi8SsYpziU_DWy0FsCTDBhBx9hnyUp3A"
    if num.startswith("0"):
        nu = num[1:]
        
    else:
        nu = num

    url = "https://api-prod.retailsso.com/v1/users/mafegy/en/contacts"

    payload = json.dumps({
      "number": nu
    })

    headers = {
      'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
      'Accept-Encoding': "gzip, deflate, br, zstd",
      'Content-Type': "application/json",
      'sec-ch-ua': "\"Chromium\";v=\"124\", \"Google Chrome\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
      'sec-ch-ua-mobile': "?1",
      'env': "prod",
      'langcode': "en",
      'lang': "en",
      'userid': "gdfgfssftgcfxff@jgguu.com",
      'x-requested-with': "XMLHttpRequest",
      'posinfo': "food=201_Zone03,nonfood=299_Zone09,express=700_Zone01",
      'appid': "Reactweb",
      'token': n,
      'storeid': "mafegy",
      'sec-ch-ua-platform': "\"Android\"",
      'origin': "https://www.carrefouregypt.com",
      'sec-fetch-site': "cross-site",
      'sec-fetch-mode': "cors",
      'sec-fetch-dest': "empty",
      'referer': "https://www.carrefouregypt.com/",
      'accept-language': "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
      'priority': "u=1, i",
      'Cookie': "_abck=356A020906C97C299DAC0725AF9101CD~-1~YAAQZuoWAh2bzDSPAQAAjOnoPwvZK4DWXZXHCUxBVfThaWn9w1btkSMy8jJotrN2snipFY7DfMldn2CJGW34qS9TcmATr4h+U1kzA89mcFOZIqP2D4OFjn1mzNgA7Gc+stGVbi98J3nv8UfmNQ2PBpKz0HfdNlq/hAmWkCdF/+A7NK+CjxN0aLyzTwlbL0WrrIBYTTLnDO7U70LB+60gsYspPqqmev1KtZ0BlZMWXvvhz7uQjZud9Ln6QVMfbkPTtND/Uda7lEvhNxQtzDdR5UZ2UHikIJd9jgApKwIsboZZtR7bGW4sLKAJZ3sabLozeXp4/djPnamquNOEWAU6MOLThzcRItf9+AvRtIduJX45/oF/H+dJp0DoEuYceVb05gVJdBlZSNKgJWjgeRI=~-1~-1~-1; bm_sz=214ADBADAE1D27941765B81FF2671BDE~YAAQZuoWAh6bzDSPAQAAjOnoPxeJ4WVOTskbGSlYNPBc8eV6fqTaw7Re8sYo762akIZwoc6spHT49XuET2YAVgk8jARgKkDfn0B0ZhrYqRXQ5ifVWXAWCkihrcW4201p1YV/prxq4oIFd9yPVwZspVV2A7zRiiCpIKkbdSXNP3Cb1f4aJm4Ef4LNJFbaL3oNWq2i5d1YOalcfiavqfGuroU+zhZSMJBnH4MI8HChzyWw5elsO4u7Ho+pvC8PRMK4Ij2XMwSt237uTppUcl5/9h1UklJZSSsbeCOh+MdnfJ/PtRSPGZsYiq6oGWoI+zXYeV1whyheYy9NibZmSIjpv73b8ZxS6qnKHcX2+0k4yQtkoM4Tf7Zqdar8QdE=~3420468~3622212"
    }

    response = requests.patch(url, data=payload, headers=headers)

    url1 = "https://www.carrefouregypt.com/v2/customers/otp/voice-call"

    payload1 = json.dumps({
      "mode": "voice",
      "action": "PHONE_VERIFICATION",
      "email": "gdfgfssftgcfxff@jgguu.com",
      "phoneNumber": f"+2{num}",
      "uuid": "40586333-46f6-43e3-9f34-7f23654f8f42",
      "locale": "en"
    })

    response1 = requests.post(url1, data=payload1, headers=headers)

    return jsonify({"message": "Verification request sent successfully."})

if __name__ == '__main__':
    app.run(debug=True)
