import httpx


payload = {
  "email": "test@example.com",
  "password": "test"
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=payload)
login_response_data = login_response.json()
access_token = login_response_data['token']['accessToken']

headers = {'Authorization': f'Bearer {access_token}'}

client = httpx.Client(headers=headers)

me_response = client.get('http://localhost:8000/api/v1/users/me')
me_response_data = me_response.json()

print(me_response_data)
print(me_response.status_code)