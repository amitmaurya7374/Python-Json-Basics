""""In this file we will practice json """
"""SCALA"""
import json
import random

website = ["amazon", "yahoo", "google", "apple"]
email = ["amitm@yahoo.com", "amit@gmail.com", "amit@apple.com", "amit@amazon.com"]
password = ["123", "234", "456", "134"]
data = {
    random.choice(website): {
        "email": random.choice(email),
        "password": random.choice(password)
    }
}

# Create a json file
# with open("web.json", "a") as file:
#     json.dump(data, file, indent=4)

# Reading a file also step 1 of updating
with open("web.json", "r") as file:
    json_data = json.load(file)
    print(json_data)

json_data.update(data)

with open("web.json", "w") as update_file:
    json.dump(json_data, update_file, indent=4)
