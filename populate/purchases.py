"""
Generate 'purchases' collection
"""

from random import random, randint
from datetime import datetime

from customers import generate_address
from products import generate_date
from sellingads import generate_lorem


NB_PURCHASES = 200

METHOD = ["Colis", "Colissimo", "Recommande", "Courier suivi", "DHL", "Relais",
          "SAL", "Airmail", "Air parcel", "Small parcel", "Chronopost", "EMS",
          "En main propre", "Express"]
PAY = ["Cheque", "Espece", "Virement", "Carte bancaire", "Paypal", "Bitcoin"]


def generate(db, sellingads_ids, customers_ids):
    purchases = db.purchases
    purchases.drop()

    purchases_list = []
    for _ in range(NB_PURCHASES):
        buyer_id = customers_ids[randint(1, len(customers_ids)-1)]
        sellingad_id = sellingads_ids[randint(1, len(sellingads_ids)-1)]
        sellingads_ids.remove(sellingad_id)
        delivery = {
            "method": METHOD[randint(1, len(METHOD)-1)],
            "address": generate_address(),
            "fees": random() * 100,
        }
        payment_date = generate_date(datetime(2018, 1, 1))
        payment = {
            "method": PAY[randint(1, len(PAY)-1)],
            "date": payment_date
        }
        purchase = {
            "buyer_id": buyer_id,
            "sellingad_id": sellingad_id,
            "delivery": delivery,
            "payment": payment,

        }
        if random() > 0.5:
            review = {
                "grade": random() * 5,
                "comment": generate_lorem(randint(2, 10)),
                "date": generate_date(payment_date),
            }
            purchase["review"] = review
        purchases_list.append(purchase)

    return purchases.insert_many(purchases_list)
