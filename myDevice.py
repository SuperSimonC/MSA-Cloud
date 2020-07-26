import random
import time
import math

from azure.iot.device import IoTHubDeviceClient, Message

# The device connection string to authenticate the device
CONNECTION_STRING = "HostName=msa-myhub.azure-devices.net;DeviceId=SimulatedDevice;SharedAccessKey=QY82Cbyfk87YJyYiOwtN9qye1LvusnWQIwI7+Gf9TaQ="

