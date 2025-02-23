import configparser

# Initialize the ConfigParser
config = configparser.ConfigParser()

# Read the config.ini file
config.read('config.ini')

# Get the access token from the config file
access_token = config['TELEGRAM']['ACCESS_TOKEN']

# Print the access token to verify (optional)
print(access_token)
     