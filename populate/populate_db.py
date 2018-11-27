#!/usr/bin/env python3

"""
Script to populate db
"""

from pymongo import MongoClient
import customers, products, sellingads, purchases, reviews

def main():
    client = MongoClient('localhost', 27021)
    db = client.dbmongo
    print(db)

    products_res = products.generate(db)
    customers_res = customers.generate(db, products_res.inserted_ids)
    sellingads_res = sellingads.generate(
        db, products_res.inserted_ids, customers_res.inserted_ids)
    purchases_res = purchases.generate(
        db, sellingads_res.inserted_ids, customers_res.inserted_ids)
    reviews.generate(
        db, purchases_res.inserted_ids, customers_res.inserted_ids)

    client.close()

main()
