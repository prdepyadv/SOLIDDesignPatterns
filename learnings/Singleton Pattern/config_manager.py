'''
Create a singleton class for a configuration manager that reads and stores configuration settings for an application.
Configuration settings are typically read once and shared across the application, so using a singleton pattern 
ensures that there is only one instance responsible for managing configurations.

Here are additional itemized steps for this exercise:
1. Create a Class Named ConfigManager: This class will manage the application's configuration settings.
2. Implement the Singleton Pattern: Ensure that only one instance of the ConfigManager class can exist 
at any time in the application.
3. Add a Method load_config: This method should read a configuration file in JSON format. The settings from this 
file should be stored in a dictionary within the ConfigManager class. It's important to store these settings in an 
attribute named .config for consistency with our testing framework.
4. Add a Method get_setting: This method should accept a key as an argument and return the corresponding setting 
value from the configuration data stored in the .config attribute.
5. Test the Singleton Behavior: Write tests to ensure that the ConfigManager class exhibits singleton behavior, 
meaning that only one instance can exist.

Note on Implementation: When implementing the load_config method, make sure to store the configuration data read 
from the JSON file in an attribute named .config. This is a specific requirement for this exercise, as our test 
cases will check for this attribute to validate your implementation.
'''

import json

class ConfigManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Implement the singleton pattern
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            
        return cls._instance

    def __init__(self):
        # Initialize an empty dictionary to store the configuration settings
        self.config = {}

    def load_config(self, config_file):
        # Read the configuration file (assuming JSON) and store the settings in the dictionary
        with open(config_file, 'r') as file:
            config_data = json.load(file)
        
        # Update the config dictionary with new settings from the config_data
        self.config.update(config_data)

    def get_setting(self, key):
        # Retrieve the setting value by key
        return self.config.get(key, None)

# Create a sample JSON configuration file named 'config.json'
sample_config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "password": "password"
    },
    "api": {
        "host": "0.0.0.0",
        "port": 8000
    }
}

with open("config.json", "w") as f:
    json.dump(sample_config, f)

# Testing the singleton behavior and config management
config1 = ConfigManager()
config2 = ConfigManager()

print(f"config1: {id(config1)}")
print(f"config2: {id(config2)}")

config1.load_config("config.json")
print(config1.get_setting("database"))
print(config2.get_setting("api"))
