import requests
from datetime import datetime

PIXEL_ENDPOINT = "https://pixe.la/v1/users"
TOKEN ="hsaldjiuw013sjd09xcu8zs"
USER = "alirezaizadi"
GRAPH_ID = "graph1"

#---------------------------------CREATE USER-------------------------------#
user_config = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# create_user = requests.post(url= PIXEL_ENDPOINT, json=user_config)
# print(create_user.text)
#---------------------------CREATE GRAPH----------------------------#
graph_config = {
    "id": GRAPH_ID,
    "name": "Alireza's Healthy Habbit Tracker",
    "unit": "kg",
    "type": "float",
    "color": "sora",

}
headers = {
    "X-USER-TOKEN": TOKEN
}
# create_graph = requests.post(url=f"{PIXEL_ENDPOINT}/{USER}/graphs", json=graph_config, headers=headers)
# print(create_graph.text)

#------------------------------------CREATE PIXEL------------------------------------#
today = datetime.today()
day = today.strftime("%Y%m%d")
pixel_config = {
    "date": day,
    "quantity": "1.5"
}
# create_pixel = requests.post(url=f"{PIXEL_ENDPOINT}/{USER}/graphs/{GRAPH_ID}", json=pixel_config, headers=headers)
# print(create_pixel.text)


#-------------------------------------UPDATE PIXEL------------------------------------#
new_day = datetime(year=2023, month=4, day=9)
update_day = new_day.strftime("%Y%m%d")

update_config = {
    "quantity": "2"
}
# update_pixel = requests.put(url=f"{PIXEL_ENDPOINT}/{USER}/graphs/{GRAPH_ID}/{update_day}", json=update_config, headers=headers)
# print(update_pixel.text)



#-----------------------------------DELETE PIXEL---------------------------------------#

# delete_pixel = requests.delete(url = f"{PIXEL_ENDPOINT}/{USER}/graphs/{GRAPH_ID}/{day}", headers=headers)
# print(delete_pixel.text)