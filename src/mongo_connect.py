import pymongo

# Create a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select a database
db = client["mydatabase"]

# Select a collection
collection = db["image_data"]

# Retrieve all the documents in the collection
documents = collection.find()

# Iterate over each document and extract the required fields
for document in documents:
    sku_id = document["SKU Id"]
    unit_id = document["Unit Id"]
    status = document["Status"]
    
    # Do something with the retrieved data, e.g. display it on the UI