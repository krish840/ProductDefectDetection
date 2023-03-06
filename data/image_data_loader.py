from pymongo import MongoClient
from PIL import Image
import os

# Connect to MongoDB
client = MongoClient()
db = client.mydatabase
collection = db.mydatabase

# Load images from folder and insert into database
for filename in os.listdir('images'):
    if filename.endswith('.jpg'):
        # Load image
        image = Image.open(os.path.join('images', filename))

        # Determine status of image (good or bad)
        if int(filename.split('.')[0]) % 10 == 0:
            status = 'bad'
        else:
            status = 'good'

        # Insert image into database
        collection.insert_one({'filename': filename, 'status': status})

print('Images loaded into database.')