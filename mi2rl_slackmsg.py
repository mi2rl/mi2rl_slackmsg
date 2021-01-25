import requests
def sendMsg(email, msg):
    url = "http://192.168.45.109/webhook/"
    payload = { "email" : email, "msg" : msg }
    res = requests.post(url, data=payload)
    return res
