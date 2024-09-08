# Import necessary packages
from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


# Create class that will edit and create the database
class Database:
    def __init__(self):
        load_dotenv()
        self.database = MongoClient(getenv('DB_URL'), tlsCAFile=where())["Collection"]
        self.collection = self.database.get_collection('Monsters')

# Insert any amount of moonsters into data
    def seed(self, amount=1000):
        monsters = []
        for _ in range(amount):
            monsters.append(Monster().to_dict())
        self.collection.insert_many(monsters)
        return f"{amount} Monsters created"

# Erase all previous monsters from collection
    def reset(self):
        self.collection.delete_many({})
        return "Monsters Reset"

# Count amount of monsters in collection
    def count(self) -> str:
        number_of_monsters = self.collection.count_documents({})
        return f"You have {number_of_monsters} Monsters"

# Convert collection into a dataframe
    def dataframe(self) -> DataFrame:
        return DataFrame(self.collection.find({}, {"_id":False}))

# Convert collection into html format
    def html_table(self) -> str:
        return self.dataframe().to_html(index=False)

# First call to create the database
if __name__ == '__main__':
    db = Database()
    db.reset()
    db.seed()
    print(db.count())

