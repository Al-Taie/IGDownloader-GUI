from dataclasses import dataclass

from pymongo import MongoClient, errors as ex

# Creating a pymongo client
client = MongoClient('MONGO_CLIENT')

db = client['Apps']
collection = db['app']


@dataclass
class Update:
    url: str
    version: str
    description: str


def is_new_update(current_version, *args, **kwargs) -> Update | bool:
    try:
        result = collection.find_one({'name': 'IG Downloader'})
    except ex.ConnectionFailure:
        return False
    else:
        version = result.get('version')
        description = result.get('description')
        url = result.get('url')
        if version > current_version:
            return Update(url=url, version=version, description=description)
        return False
