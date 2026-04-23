# NoSQL

Introduction to MongoDB — basic shell scripts and Python functions using PyMongo.

## MongoDB Shell Scripts (0–7)

These files are piped directly into the `mongo` shell.

| File | Description |
|---|---|
| `0-list_databases` | List all databases |
| `1-use_or_create_database` | Switch to (or create) `my_db` |
| `2-insert` | Insert `{ name: "Holberton school" }` into `school` |
| `3-all` | List all documents in `school` |
| `4-match` | List documents where `name = "Holberton school"` |
| `5-count` | Count documents in `school` |
| `6-update` | Add `address: "972 Mission street"` to all matching documents |
| `7-delete` | Delete all documents where `name = "Holberton school"` |

Usage example:
```bash
cat 0-list_databases | mongo
cat 2-insert | mongo my_db
```

## Python Functions (8–11)

These use the **PyMongo** driver. The `mongo_collection` argument is always a `pymongo` collection object.

| File | Function | Description |
|---|---|---|
| `8-all.py` | `list_all(mongo_collection)` | Return all documents as a list (empty list if none) |
| `9-insert_school.py` | `insert_school(mongo_collection, **kwargs)` | Insert a document from kwargs, return its `_id` |
| `10-update_topics.py` | `update_topics(mongo_collection, name, topics)` | Replace the `topics` list for all schools matching `name` |
| `11-schools_by_topic.py` | `schools_by_topic(mongo_collection, topic)` | Return all schools whose `topics` array contains `topic` |

## Log Stats Script (12)

`12-log_stats.py` connects to the local MongoDB instance and prints statistics about Nginx logs stored in the `logs.nginx` collection:

```
94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
```

Run it directly:
```bash
./12-log_stats.py
```

To load the sample data:
```bash
curl -o dump.zip -s "<dump_url>"
unzip dump.zip
mongorestore dump
```

## Requirements

- MongoDB 3.6+
- Python 3.x
- `pymongo` library (`pip install pymongo`)
