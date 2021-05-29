import time
from flask import jsonify
from firebase_db import db
from scraping_tools import scrape
import base64


# specify here or in the README what the event['data'] parameter contains
# this is used to divide scraping tasks up
# scrapes and uploads tweets to the raw_data collection
def scrape_tweets(event, context):
    start_time = time.time()
    datatype = "name the datatype here"
    target = base64.b64decode(event['data']).decode('utf-8')

    posts = scrape(target)

    for post in posts:
        id = post["id"]
        db().collection('raw_data').document(f'{datatype}{id}').set({
            "type": datatype,
            "timestamp": time.time(),
            "created": post["timestamp"],
            "content": post["content"]
        })

    return jsonify({
        "success": True,
        "quantity": len(posts),
        "time_taken": time.time() - start_time
    })
