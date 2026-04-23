#!/usr/bin/env python3
"""Return all schools that teach a given topic."""


def schools_by_topic(mongo_collection, topic):
    """Return a list of schools whose topics array contains topic."""
    return list(mongo_collection.find({"topics": topic}))
