######################################################################################
# https://docs.microsoft.com/en-us/rest/api/power-bi/
#https://stackoverflow.com/questions/62442327/using-python-to-retrieve-access-token-for-power-bis-rest-api?fbclid=IwAR18DAh9-jtg1MegF3FQ0XfpTndQUSAQCqCEmNmsvmmte9pIKi5n1VNzHDE
#https://www.youtube.com/watch?fbclid=IwAR33kHRPTJ3Npcmi7ABP_p2rLcZgeXeQggSKWPLWqRK3vuOkqaDoCbJx8mo&v=dogIABwpL4I&feature=youtu.be
#https://www.youtube.com/watch?fbclid=IwAR33kHRPTJ3Npcmi7ABP_p2rLcZgeXeQggSKWPLWqRK3vuOkqaDoCbJx8mo&v=_2eGAjm1I4w&feature=youtu.be
#https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.datalineo.com%2Fpost%2Fpower-bi-rest-api-with-python-and-microsoft-authentication-library-msal%3Ffbclid%3DIwAR3-TmVAOfX3WbQ-sgmCKQlS34tJjtJki0rltsFWkEsfhoGc8iE4UlwuyZ8&h=AT2EjZiNz0FdM0PS1ttHornKZIWt9Ld6VLs_9auvfN7XZbO4qObRHbRP-tfq9ENk1DqwGrkKfAmFQHtzmZvart91kT7_JL_BcowIuBKnVsfFp32rhKmrVS3-nhxBzKffJZuxm9U_w0Oq
#https://l.facebook.com/l.php?u=https%3A%2F%2Fpivotalbi.com%2Fautomate-your-power-bi-dataset-refresh-with-python%2F%3Ffbclid%3DIwAR3PSO5D2ZOx3iL9H2O-yk0wFb1L9ocesHXqFT-XSUVqvr1FmWdOIhoASwg&h=AT3lPmuNCgtiMEZnBGUkGch7CkaE6J3_JXqr2iWKUpIpMeIK8maw_h8jn1bZzAQLmPzVD-qTTbRYcvfkAHqzbByjqvXNGPvn1X8qouSbylbLYLsGhCkRdvutSzwhOLIuGy-Sdd_8tGV6
#https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.antmanbi.com%2Fpost%2Fusing-python-to-execute-dax-queries-in-power-bi-ssas-tabular-part-1%3Ffbclid%3DIwAR1ONXOTZ7FCJlp83Qz__Fy-BGft1R4jXe7XVwSyl1iBqZbeKwXdRVOP5rk&h=AT1tYatiyCXBJYamD-Ml7EkuJXaD-YMQ6FkFFecW4blsrcpaiRWmd0U4L-V5tMPxwhm54vG480Hv1FD7R4WicdMUyEqrz8X3Jjs-QtVYGwJbySltl1MxKi9oEbsyN3jOUnh1vyPuQ5CZ
######################################3
def power_bi_api_call(url):
  # This should stay the same always
  token = get_access_token("{client_id}","*****@stryker.com","*****")
    
  # format token for proper request with Bearer token
  token_formatted = "Bearer {token}"
  token_final = token_formatted.format(token=token)
  
  payload={}
  headers = {
  'Authorization':token_final,
  'Content-Type': 'application/json'
  }
  
  # Actual request
  response = requests.request("GET", url, headers=headers, data=payload)
  
  # load response content into json
  json_object = json.loads(response._content)
  
  return json_object

# Go to his website to get this url 
#https://docs.microsoft.com/en-us/rest/api/power-bi/datasets/get-refresh-history-in-group

# this api url is checking 
api_data = power_bi_api_call("https://api.powerbi.com/v1.0/myorg/groups/{workspaceid}/datasets/{datasetid}/refreshes?$top=2")

# the way to subset it!
api_data['value']

# see the request id
api_data['value'][0]["requestId"]

# see the start of the last refresh
api_data['value'][0]["startTime"]

# see when it finished
api_data['value'][0]["endTime"]

# see the status
api_data['value'][0]["status"]


##########################################################################################
 

all_reports = power_bi_api_call("https://api.powerbi.com/v1.0/myorg/groups/{workspaceid}/reports")
all_reports



def power_bi_api_call2(url):
  # This should stay the same always
  token = get_access_token("{client-id}","*********@stryker.com","*****")
    
  # format token for proper request with Bearer token
  token_formatted = "Bearer {token}"
  token_final = token_formatted.format(token=token)
  
  payload={}
  headers = {
  'Authorization':token_final,
  'Content-Type': 'application/json'
  }
  
  # Actual request
  response = requests.request("GET", url, headers=headers, data=payload)
  
  # load response content into json
  json_object = json.loads(response.content)
  
  return json_object



all_reports = power_bi_api_call2("https://api.powerbi.com/v1.0/myorg/groups/{workspaceid}/reports")

# check to see how this is subscriptable
all_reports.keys()

# how many reports do we have! 
len(all_reports['value'])

# Grab the OI score card 
all_reports['value'][190]

all_reports['value'][190]['id']
all_reports['value'][190]['name']
all_reports['value'][190]['embedUrl']
all_reports['value'][190]['datasetId']
all_reports['value'][190]['datasetWorkspaceId']
all_reports['value'][190]['webUrl']
all_reports['value'][190]['reportType']


############################################################################################################################################
############################################################################################################################################
############################################################################################################################################
############################################################################################################################################

# This code commented out is the power bi api connection not functionalized.
# 
# import requests
# import json
# def get_access_token(client_id, username, password):
#     data = {
#         'grant_type': 'password',
#         'scope': 'openid',
#         'resource': r'https://analysis.windows.net/powerbi/api',
#         'client_id': client_id,
#         'username': username,
#         'password': password
#     }
#     token = requests.post('https://login.microsoftonline.com/common/oauth2/token', data=data)
#     assert token.status_code == 200, "Fail to retrieve token: {}".format(token.text)
#     return token.json().get('access_token')
#   
#   
# # type in client id in this case in azure active directory the client id is (PowerBIEmbeddedSP) which we set up with power bi embedded set up
# token = get_access_token("{client-id}","******@stryker.com","*******")
# 
# token_formatted = "Bearer {token}"
# 
# token_final = token_formatted.format(token=token)
# 
# 
# url = "https://api.powerbi.com/v1.0/myorg/groups/{workspaceid}/datasets/{datasetid}/refreshes?$top=2"
# 
# payload={}
# headers = {
#   'Authorization':token_final,
#   'Content-Type': 'application/json'
# }
# 
# response = requests.request("GET", url, headers=headers, data=payload)
# 
# print(response.text)
# 

