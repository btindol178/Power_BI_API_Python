# Query power bi dataset 
import requests
import json
def get_access_token(client_id, username, password):
    data = {
        'grant_type': 'password',
        'scope': 'openid',
        'resource': r'https://analysis.windows.net/powerbi/api',
        'client_id': client_id,
        'username': username,
        'password': password
    }
    token = requests.post('https://login.microsoftonline.com/common/oauth2/token', data=data)
    assert token.status_code == 200, "Fail to retrieve token: {}".format(token.text)
    return token.json().get('access_token')


# type in client id in this case in azure active directory the client id is (PowerBIEmbeddedSP) which we set up with power bi embedded set up
access_token = get_access_token("{client-id}","********@stryker.com","**********")

##########################################################################################################

post_query = 'https://api.powerbi.com/v1.0/myorg/datasets/{dataset-id}/executeQueries'
header = {'Authorization': f'Bearer {access_token}','Content-Type' : 'application/json'}
header = header.format(access_token=access_token)
body = '''{
  "queries": [
    {
      "query": "EVALUATE Division"
}
  ],
  "serializerSettings": {
    "includeNulls": "true"
  }
}'''

post_r = requests.post(url=post_query,data=body, headers=header)
post_r.raise_for_status()

# query the division table content
post_r._content
