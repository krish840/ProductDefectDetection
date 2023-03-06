import pymongo
import random

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["switchon"]
collection = db["products"]

# generate random product entries
good_count = 90  # 90% good products
bad_count = 10   # 10% bad products
total_count = good_count + bad_count

for i in range(1, total_count+1):
    if i <= bad_count:
        status = "Bad"
    else:
        status = "Good"

    product = {
        "sku_id": "SKU001",
        "unit_id": str(i),
        "status": status,
    }

    # insert product entry into database
    collection.insert_one(product)