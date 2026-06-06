import requests
from pyspark.sql import SparkSession

def load_users_api(spark: SparkSession):

    url = "https://jsonplaceholder.typicode.com/users"
    data = requests.get(url).json()

    cleaned = []

    for u in data:
        cleaned.append({
            "user_id": u["id"],
            "name": u["name"],
            "username": u["username"],
            "email": u["email"],
            "phone": u["phone"],
            "website": u["website"],
            "city": u["address"]["city"],
            "zipcode": u["address"]["zipcode"],
            "company_name": u["company"]["name"]
        })

    return spark.createDataFrame(cleaned)