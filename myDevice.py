import random
import time
import math

from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device
CONNECTION_STRING = "HostName=msa-myhub.azure-devices.net;DeviceId=SimulatedDevice;SharedAccessKey=QY82Cbyfk87YJyYiOwtN9qye1LvusnWQIwI7+Gf9TaQ="

# Define the JSON message to send to IoT Hub.

MSG_TXT = '{{"Altitude": {Altitude}, "Speed": {Speed}}}'
Altitude_default = 10000
Speed_default = 200

def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def generate():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            
            # Build the message with simulated telemetry values.
            Altitude = Altitude_default + (random.random() * 100)
            Speed = Speed_default + (random.random() * 20)
            msg_txt_formatted = MSG_TXT.format(Altitude=Altitude, Speed = Speed)
            message = Message(msg_txt_formatted)

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(1)

    except KeyboardInterrupt:
        print ( "IoTHubClient stopped" )


if __name__ == '__main__':
    generate()
