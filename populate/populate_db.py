#!/usr/bin/env python3

"""
script de peuplement
"""

from pymongo import MongoClient
import customers, products, sellingads, purchases

def main():
    client = MongoClient('localhost', 27021)
    db = client.dbmongo
    print(db)

    products_res = products.generate(db)
    customers_res = customers.generate(db, products_res.inserted_ids)
    sellingads_res = sellingads.generate(
        db, products_res.inserted_ids, customers_res.inserted_ids)
    purchases.generate(
        db, sellingads_res.inserted_ids, customers_res.inserted_ids)

    client.close()

main()
