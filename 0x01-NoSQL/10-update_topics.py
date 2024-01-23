#!/usr/bin/env python3
"""updates the document"""


def update_topics(mongo_collection, name, topics):
    """update topics of a school document based on the name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
