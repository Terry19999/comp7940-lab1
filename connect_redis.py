"""Basic connection example.
"""
import configparser
import redis

config = configparser.ConfigParser()
config.read('config.ini')

r = redis.Redis(
    host='redis-15081.crce178.ap-east-1-1.ec2.redns.redis-cloud.com',
    port=15081,
    decode_responses=True,
    username="default",
    password="dYdqrabqzRGCuKkay3BhVHCfDMh1yCa6",
)

# Set new key-value pair
r.set("my_name", "xuyu")
print(r.get("my_name"))  # Output: xuyu

# Get the value of the given key
value = r.get("my_name")
print(f"The value of 'my_name' is: {value}")  # Output: The value of 'my_name' is: xuyu

# Check whether a particular key exists
key_exists = r.exists("my_name")
print(f"Does 'my_name' exist? {key_exists}")  # Output: 1 (True) if exists, 0 (False) if not

random_key_exists = r.exists("random123")
print(f"Does 'random123' exist? {random_key_exists}")  # Output: 0 (False) if not

# Delete a key
r.delete("my_name")
deleted_key_exists = r.exists("my_name")
print(f"Does 'my_name' exist after deletion? {deleted_key_exists}")  # Output: 0 (False) if deleted

