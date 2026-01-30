import pika
from pymongo import MongoClient
from bson.objectid import ObjectId
from typing import TypeVar


T = TypeVar('T')

class Channel:

    def __init__(self, connection: pika.BlockingConnection, queue_name: str) -> pika.channel.Channel:
        self.channel = connection.channel()
        self.channel.queue_declare(queue=queue_name)
        return self.channel
      
    def send(self, id: str) -> None:
        self.channel.basic_publish(exchange='', routing_key=self.queue_name, body=id)
        print(f"Message sent: {id}")

class Chat:

    def __init__(self) -> None:
        self.db = MongoClient('mongodb://admin:admin@localhost:27017/')['chat']

    def insert(self, doc: T) -> T:
        collection = self.db[doc.__class__.__name__.lower()]
        dict = doc.__dict__
        dict.pop('_id', None)
        result = collection.insert_one(dict)
        doc._id = str(result.inserted_id)
        return doc

    def update(self, doc: T) -> T:
        collection = self.db[doc.__class__.__name__.lower()]
        doc._id = ObjectId(doc._id)
        collection.update_one({'_id': doc._id}, {'$set': doc.__dict__})
        return doc

    def retrieve(self, T, id: str) -> T | None:
        collection = self.db[T.__name__.lower()]
        doc = collection.find_one({'_id': ObjectId(id)})
        return self.doc_to_t(doc=doc, T=T)

    def last(self, T) -> T | None:
        collection = self.db[T.__name__.lower()]
        doc = collection.find_one(sort=[('_id', -1)])
        return self.doc_to_t(doc=doc, T=T)

    def doc_to_t(self, doc: object, T) -> T | None:
        if doc:
            doc['_id'] = str(doc['_id'])
            return T(**doc)
        return None
