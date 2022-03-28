from typing import Optional, Text

from pymongo import MongoClient, errors as ex

# Creating a pymongo client
client = MongoClient('MONGODB_CLIENT')

db = client['apps_db']
collection = db['apps']


def is_new_update(current_version, *args, **kwargs):
    try:
        result = collection.find_one({'name': 'IG Downloader'})
    except ex.ConnectionFailure:
        return False
    else:
        version = result.get('version')
        description = result.get('description')
        url = result.get('url')
        if version > current_version:
            return url, description
        else:
            return False


