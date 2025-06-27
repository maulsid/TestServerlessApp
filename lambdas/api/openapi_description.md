## Usage

To use this API, obtain an access token using client credentials flow:

**Token Endpoint:**
POST https://auth.{env}.cdf.otsuka-oph.org/oauth2/token

**Payload:**
```x-www-form-urlencoded
grant_type=client_credentials
client_id=YOUR_CLIENT_ID
client_secret=YOUR_CLIENT_SECRET
```

**Response:**
```json
{'access_token': 'XYZ'}
```
