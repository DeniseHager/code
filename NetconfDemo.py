"""
This script automates the code found in the 'Breaking down NETCONF communictions in the Cisco DevNet lab
Please use the env_lab file provided by your instructor.
"""
from ncclient import manager
import env_lab
NCManager=manager.connect(
    host=env_lab.IOS_XE_1["host"],
    port=env_lab.IOS_XE_1["netconf_port"],
    username=env_lab.IOS_XE_1["username"],
    password=env_lab.IOS_XE_1["password"],
    hostkey_verify=False
)

for capability in NCManager.server_capabilities:
    print(capability)

NCManager.close_session()
