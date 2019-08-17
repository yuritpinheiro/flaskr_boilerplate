import wiotp.sdk.device
import random
import time

dev_config = {
    "identy": {
        "orgId": "",
        "typeId": "",
        "deviceId": ""
    }
    "auth": {
        "token": ""
    }
}

def myCommandCallBack(cmd):
    print("Command received: %s" % cmd.data)

client = wiotp.sdk.device.DeviceClient(config=dev_config)

client.connect()

while True:
    myData = { "tag": random.randint(20, 50) }
    client.publishEvent(eventId="tag", msgFormat="json", data=myData, qos=0, onPublish=None)
    client.commandCallback = myCommandCallBack
    time.sleep(2)
