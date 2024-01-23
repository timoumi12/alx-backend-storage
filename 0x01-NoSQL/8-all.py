#!/usr/bin/env python3
"""lists all docs"""


def list_all(mongo_collection):
  '''Return an empty list if no document in the collection'''
  return mongo_collection.find()
