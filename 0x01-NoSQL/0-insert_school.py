#!/usr/bin/env python3
"""inserts a doc"""


def insert_school(mongo_collection, **kwargs):
  """Returns the new _id"""
  new_documents = mongo_collection.insert_one(kwargs)
  return new_documents.inserted_id
