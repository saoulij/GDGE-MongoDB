"""
Generate 'reviews' collection
"""

from random import random, randint
from datetime import datetime

from products import generate_date
from sellingads import generate_lorem

def generate(db, purchases_ids, customers_ids):
    reviews = db.reviews
    reviews.drop()

    reviews_list = []
    for purchase_id in purchases_ids:
        if random() < 0.25:
            continue
        buyer_id = customers_ids[randint(1, len(customers_ids)-1)]
        purchase = db.purchases.find_one({"_id": purchase_id})
        sellingad_id = purchase["sellingad_id"]
        payment_date = purchase["payment"]["date"]
        seller_id = db.sellingads.find_one({"_id": sellingad_id})["seller_id"]
        review = {
            "purchase_id": purchase_id,
            "seller_id": seller_id,
            "buyer_id": buyer_id,
            "grade": random() * 5,
            "comment": generate_lorem(randint(2, 10)),
            "date": generate_date(payment_date),
        }
        reviews_list.append(review)

    return reviews.insert_many(reviews_list)
