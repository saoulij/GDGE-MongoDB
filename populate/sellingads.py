"""
Generate 'sellingads' collection
"""

import os
from random import random, randint
from datetime import datetime
from customers import CITY, rand_number
from products import generate_date


NB_SELLINGADS = 1000

LOREM = []

def init_lorem():
    fn = os.path.join(os.path.dirname(__file__), 'loremipsum.txt')
    with open(fn, 'r') as f:
        for word in f.read().split():
            LOREM.append(word)

def generate_lorem(number):
    text = ""
    for _ in range(number):
        text +=  LOREM[randint(0, len(LOREM)-1)] + " "
    return text


def generate(db, products_ids, customers_ids):
    sellingads = db.sellingads
    sellingads.drop()

    init_lorem()

    sellingads_list = []
    for _ in range(NB_SELLINGADS):
        seller_id = customers_ids[randint(1, len(customers_ids)-1)]
        seller_data = db.customers.find_one({"_id": seller_id})
        seller = {
            "_id": seller_id,
            "name": seller_data["name"],
            "email": seller_data["email"],
            "phone": seller_data["phone"],
        }
        title = generate_lorem(randint(1, 8))
        description = generate_lorem(randint(5, 50))
        products = []
        for _ in range(randint(1, 3)):
            products.append(products_ids[randint(1, len(products_ids)-1)])
        location = {
            "city": CITY[randint(0, len(CITY)-1)],
            "zipcode": rand_number(5)
        }
        price = random() * 1000
        date = generate_date(datetime(2018, 1, 1))
        sellingad = {
            "seller": seller,
            "title": title,
            "description": description,
            "products": products,
            "location": location,
            "date": date,
            "price": price,
        }
        sellingads_list.append(sellingad)

    return sellingads.insert_many(sellingads_list)
