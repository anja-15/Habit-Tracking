import requests
from datetime import datetime

TOKEN = "nfibio20r39y23bjitfbkjet"
USERNAME = "jauhari"
GRAPH_ID = "graph1"
headers = {
    "X-USER-TOKEN": TOKEN
}

pixela_endpoint = "https://pixe.la/v1/users"
# user_parameters looks like a json file
user_parameters = {
    "token": TOKEN,
    "username": USERNAME ,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

"""PIXEL_CREATION"""
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
# or f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
formatted_today = today.strftime("%Y%m%d")
pixel_config ={
    "date": formatted_today,
    "quantity": input("How many KMs did you cycle today? "),
}
# response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
# print(response.text)

"""UPDATE"""
update_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{formatted_today}"
updated_pixel_config ={
    "quantity": "5",
}
# response = requests.put(url=update_pixel_endpoint, json=updated_pixel_config, headers=headers)
# print(response.text)

"""DELETE"""
today = datetime(2024,6,15)
formatted_today = today.strftime("%Y%m%d")
delete_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}/{formatted_today}"
delete_pixel_config ={
    "quantity": "5",
}
response = requests.delete(url=delete_pixel_endpoint,headers=headers)
print(response.text)
