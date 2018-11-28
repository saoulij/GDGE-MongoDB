#!/usr/bin/env python3

"""
Script to populate db
"""

from pymongo import MongoClient, ASCENDING, DESCENDING, TEXT
import customers, products, sellingads, purchases, reviews


def create_indexes(db):
    db.products.create_index([
        ('product_type', TEXT),
        ('type', TEXT),
    ], default_language='french')

    db.sellingads.create_index([('date', DESCENDING)])
    db.sellingads.create_index([('seller_id', ASCENDING)])

    db.purchases.create_index([
        ('payment.date', DESCENDING),
        ('buyer_id', ASCENDING),
    ])

    db.reviews.create_index([('date', DESCENDING)])


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

    create_indexes(db)

    client.close()

main()
