'''
Goal: Create dictionaries and access values.
'''

from typing import Union

# Create a 'config' dictionary with the following pairs:
Config: dict[str, Union[str, int]] = {
    "Host" : "192.168.1.1",
    "Port" : 8080,
    "Ssl" : True,
    "Timeout" : 30,
}

# Print the value of "Host"
host_key = "Host"
host_value = Config[host_key]
print(f"{host_key}: {host_value}")

# Modify "Port" to 443
Config["Port"] = 443

# Add a new key "Protocol" with value "https"
Config["Protocol"] = "https"

# Print the complete dictionary
print(Config)