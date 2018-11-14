"""
Generate 'customers' collection
"""

from random import random, randint, sample


NB_CUSTOMERS = 500

FIRSTNAME = ["Jean", "Pierre", "Michel", "Andre", "Philippe", "Andre", "Louis",
             "Alain", "Jacques", "Paul", "Claude", "Patrick", "Christophe",
             "David", "Stephane", "Olivier", "Thomas", "Charles", "Marc",
             "Didier", "Romain", "Gilbert", "Lucas", "Jules", "Kevin", "Joel",
             "Alexis", "Sylvain", "Benoit", "Ludovic", "Audrey", "Anais",
             "Mathilde", "Beatrice", "Marion", "Delphine", "Emma", "Pauline",
             "Caroline", "Elise", "Madeleine", "Nathalie", "Jeanne", "Marie",
             "Louise", "Sophie", "Stephanie", "Lucie", "Madison", "Sophia",
             "Ashley", "Olivia", "Isabella", "Abigail", "Alexis", "Nicole",
             "Gabriella", "Lily", "William", "James", "John", "Jane", "Jayden",
             "Wyatt", "Owen", "Aiden", "Ethan", "Alexander", "Jacob", "Ryan",
             "Michael", "Raphael", "Noah", "Yannick", "Zoe", "Lea", "Eve",
             "Luis", "Logan", "Mason", "Hunter", "Markel", "Pablo", "Jon",
             "Hugo", "Elias", "Liam", "Luka", "Nikola", "Lewis", "Aimar", "Ali",
             "Sara", "Lena", "Fatima", "Nuray", "Ayan", "Oscar", "Yasmine",
             "Noam", "Ariel", "Yosef", "Hana", "Ren", "Rani", "Amir", "Ellie"]
LASTNAME = ["Martin", "Bernard", "Thomas", "Petit", "Durant", "Dubois",
            "Moreau", "Leroy", "Fournier", "Roux", "Leroy", "Simon", "Mercier",
            "Blanc", "Garnier", "Rousseau", "Henry", "Meunier", "Blanchard",
            "Lucas", "Roche", "Schmitt", "Dumas", "Lacroix", "Leclerc",
            "Lopez", "Dupuy", "Hubert", "Adam", "Klein", "Bailly", "Julien",
            "Bouvier", "Carre", "Prevost", "Besson", "Weber", "Lemaitre",
            "Reynaud", "Carlier", "Jonson", "Taylor", "Green", "Hail", "Wood",
            "Clarke", "Jackson", "Evans", "Robinson", "Brown", "Sato", "Ito",
            "Yamada", "Tanaka", "Watanabe", "Rossi", "Prezzo", "Fortin",
            "Tremblay", "Gonzalez", "Hernandes", "Morales", "Anderson", "Lee",
            "Garcia", "Wilson", "White", "Wright", "King", "Nelson", "Hill",
            "Campbell", "Mitchell", "Roberts", "Carter"]

MAIL = ["@gmail.com", "@grenoble-inp.org", "@free.fr",
        "@hotmail.com", "@yahoo.fr"]

STREET_1 = ["rue", "avenue", "impasse", "ruelle", "voie", "boulevard", "place",
            "allée", "route", "sentier", "chemin", "clos", "passage", "pont"]
STREET_2 = ["de l'eau", "du puit", "de l'etang", "du jardin", "du bois",
            "du four", "de la ferme", "de l'arbre", "de la fleur",
            "de l'epine", "du marechal", "de Paris", "de la ceuillette",
            "des groseilles", "des pommes", "des poires", "de la vache",
            "du mouton", "du moulin", "de la colline", "de la verdure",
            "des boeufs", "de la charrue", "de devant", "de derriere",
            "de l'eglise", "de la croix", "des dunes", "des lilas", "des roses",
            "des hortensias", "de la gare", "du train", "de la piscine",
            "des sciences", "des langues", "des mathématiques", "de la pluie",
            "du beau temps", "de la grisaille", "des petits pois", "des grands",
            "des gros pois", "des haricots", "des bananes", "des ananas",
            "Charles de Gaulle", "Louis Pasteur", "Jean Jaures", "Victor Hugo",
            "General Leclec", "Jules Ferry", "Jean Moulin", "Marechal Foch",
            "des ecoles", "du chateau", "de la fontaine", "du stade"
            "principale", "grande", "petite", "huit-mai", "dix-neuf-mars",
            "quatre-septembre", "onze-novembre", "quatorze-juillet"]
CITY = ["Paris", "Lyon", "Grenoble", "Montpellier", "Brest", "Rennes", "Caen",
        "Reims", "Le Mans", "Lille", "Metz", "Nancy", "Bordeaux", "Nice",
        "Toulouse"]

def rand_number(length):
    return ''.join(sample('0123456789', length))

def generate_name():
    firstname = FIRSTNAME[randint(0, len(FIRSTNAME)-1)]
    lastname = LASTNAME[randint(0, len(LASTNAME)-1)]
    return {
        "first": firstname,
        "last": lastname,
    }

def generate_address():
    street1 = STREET_1[randint(0, len(STREET_1)-1)]
    street2 = STREET_2[randint(0, len(STREET_2)-1)]
    zipcode = rand_number(5)
    city = CITY[randint(0, len(CITY)-1)]
    country = "France"  # add more
    return {
        "street": (street1 + " " + street2),
        "zipcode": zipcode,
        "city": city,
        "country": country,
    }

def generate(db, products_ids):
    customers = db.customers
    customers.drop()

    customers_list = []
    for _ in range(NB_CUSTOMERS):
        name = generate_name()
        email = name["first"] + "." + name["last"] + MAIL[randint(0, len(MAIL)-1)]
        phone = "0" + rand_number(9)
        address = []
        for _ in range(randint(1, 3)):
            address.append(generate_address())
        products = []
        for _ in range(randint(0, 20)):
            products.append(products_ids[randint(0, len(products_ids)-1)])
        customer = {
            "name": name,
            "email": email,
            "phone": phone,
            "addresses": address,
            "followed_products": products,
        }
        customers_list.append(customer)

    return customers.insert_many(customers_list)
