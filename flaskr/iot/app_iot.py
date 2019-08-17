import wiotp.sdk.application
import wiotp.sdk.device
import json


app_config = {
    "auth": {
        "key": "",
        "token": ""
    }
}

def myEventCallback(e):
    msg = "%s event '%s' received from device [%s]: %s"
    print(msg % (e.format, e.eventId, e.device, json.dumps(e.data)))
    if e.data['pressao'] > 30:
        commandData = { "cmd": "just do it" }
        client.publishCommand("JP", "jp-01", "reboot", "json", commandData)


client =  wiotp.sdk.application.ApplicationClient(config=app_config)
client.connect()
client.subscriveToDeviceEvents()

while True:
    client.deviceEventCallback = myEventCallback
    