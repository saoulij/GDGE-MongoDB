"""
Generate 'products' collection
"""

from random import random, randint
from datetime import datetime
from customers import generate_name


NB_PRODUCTS_BY_TYPE = 100

CLOTHES = ["Pantalon", "Costume", "T-shirt", "Chaussure", "Robe", "Jupe",
           "Chemise", "Pull", "Sweat"]
MAT_CLOTH = ["Coton", "Laine", "Cachemire", "Synthetique", "Soie", "Jean",
             "Cuir", "Nubuck", "Lin", "Elasthanne", "Polyester", "Viscose"]
COLOR = ["Bleu", "Rouge", "Vert", "Jaune", "Rose", "Noir", "Rouge", "Gris",
         "Orange", "Violet", "Blanc", "Magenta", "Cyan", "Marron", "Beige"]
SIZE = ["XS", "S", "M", "L", "XL"]

BRAND = ["Fantasy", "Lamb", "Crazy", "Cobra", "Rooster", "Control", "Horse",
         "Firesaga", "Sun", "Fantasy", "Proworks", "Sapphire", "Amazing", "Lux",
         "Premium", "Freesoft", "Intermagine", "Fier", "Foret", "Luminous",
         "Grumpy Deer", "Harmony", "Aspect", "Orange", "Aqua", "Foo", "Nox",
         "Yellow", "Smile", "Blade", "Rice", "Flame", "Argent", "Golden",
         "Uodo", "Dibought", "Domp", "Dhadance", "Illould", "Contrast", "Time",
         "Monovoo", "Iri", "Overite", "Aain", "Abhe", "Charlang", "River",
         "Arts", "Pixy", "Ice", "Squid", "Alpite", "Sunlight", "Crow", "Search",
         "Blue", "Happy", "Wizard", "Fairy", "Orangation", "Neroduction", "Bar"]

STUDIO_N = ["Entartainement", "Studio", "Interactive", "Works", "Studios",
            "Productions", "Media", "Company", "Production"]
TITLE_1 = ["Guerriers", "Etrangers", "Corps", "Infortune", "Lunaire", "Solaire",
           "Question", "Réponse", "Ocean", "Famille", "Mage", "Protecteur",
           "Dieux", "Enfants", "Sorcières", "Géant", "Hello", "Hi", "Shield",
           "Sourire", "Manger", "Saigner", "Se cacher", "Acheter", "Vendre",
           "Tuer", "Voler", "Murmures", "Mordre", "Supernova", "Concept",
           "Lit", "Neuf", "Cabinet", "Total", "Extreme", "Around", "Just",
           "Once", "No", "Yes", "Grains", "Crazy", "Sad", "Miss", "Reves",
           "Lady", "Animal", "Doubt", "Trouble", "Expert", "Opinion", "Life",
           "High", "Cercle", "Triangle", "Carre", "Pineapple", "Dream"]
TITLE_2 = ["de l'univers", "de l'eau", "dans le brouillard", "de la lune",
           "du soleil", "du matin", "du soir", "du passé", "du présent",
           "du futur", "et voleurs", "sans but", "sans réponse", "du bois",
           "de la terre", "de la lune", "du soleil", "des étoiles", "feelings",
           "avec force", "sans peur", "de la grandeur", "we go", "dans le sud",
           "dans le nord", "memoires", "atmos", "memories", "for one", "I do",
           "for two", "for you", "story", "storm", "the bus", "bubble", "zero",
           "one", "stories", "dead", "death", "light", "horror", "pie"]
GENRE = ["Fantasy", "Scifi", "Fantastique", "Drame", "Romance", "Musical",
         "Action", "Comedie", "Aventure", "Thriller", "Policier", "Horreur"]
BOOK_TYPE = ["Roman", "BD", "Revue", "Livre illustre"]
MOVIE_TYPE = ["DVD", "Blu-ray"]
MUSIC_TYPE = ["Album", "Single", "EP", "Live", "Reprise", "Vinyl"]
MUSIC_GENRE = ["Pop", "Rock", "Jazz", "Classique", "Rap", "Rnb", "Metal",
               "Disco", "Soul", "Gospel", "Reggae"]

FURNITURE = ["Canape", "Chaise", "Bureau", "Table", "Fauteuil", "Armoire",
             "Cuisine", "Porte", "Fauteuil", "Etagere", "Lampe", "Lit",
             "Television", "Ordinateur", "Tablette", "Telephone", "Baladeur",
             "Cafetiere", "Imprimante", "Micro-onde", "Refregirateur",
             "Aspirateur", "Grille-pain", "Mixer", "Lave-linge", "Seche-linge"]
MAT_FURN = ["Plastique", "Cuir", "Bois", "Verre", "Tissu", "Aluminum", "Acier"]


def generate_title():
    length = randint(1, 2)
    title = TITLE_1[randint(0, len(TITLE_1)-1)]
    if length > 1:
        title += " " + TITLE_2[randint(0, len(TITLE_2)-1)]
    return title

def generate_date(start=datetime(1900, 1, 1)):
    end = datetime(2018, 12, 31)
    return start + (end - start) * random()


def generate_clothes(products, number):
    for _ in range(number):
        cloth_type = CLOTHES[randint(0, len(CLOTHES)-1)]
        materials = []
        material_nb = randint(1, 4)
        for _ in range(material_nb):
            percent = 100 / material_nb
            materials.append({
                "name": MAT_CLOTH[randint(0, len(MAT_CLOTH)-1)],
                "percent": percent,
            })
        colors = []
        for _ in range(randint(1, 4)):
            colors.append(COLOR[randint(0, len(COLOR)-1)])
        size = SIZE[randint(0, len(SIZE)-1)]
        brand = BRAND[randint(0, len(BRAND)-1)]
        date = generate_date()
        cloth = {
            "product_type": "vetement",
            "type": cloth_type,
            "materials": materials,
            "colors": colors,
            "size": size,
            "brand": brand,
            "release_date": date,
        }
        products.append(cloth)

def generate_music(products, number):
    for _ in range(number):
        title = generate_title()
        music_type = MUSIC_TYPE[randint(0, len(MUSIC_TYPE)-1)]
        genre = MUSIC_GENRE[randint(0, len(MUSIC_GENRE)-1)]
        artist = generate_name()
        editor = (BRAND[randint(0, len(BRAND)-1)] + ""
                  + STUDIO_N[randint(0, len(STUDIO_N)-1)])
        date = generate_date()
        music = {
            "product_type": "musique",
            "title": title,
            "type": music_type,
            "genre": genre,
            "artist": artist,
            "editor": editor,
            "release_date": date,
        }
        products.append(music)

def generate_movies(products, number):
    for _ in range(number):
        title = generate_title()
        movie_type = MOVIE_TYPE[randint(0, len(MOVIE_TYPE)-1)]
        genres = []
        for _ in range(randint(1, 5)):
            genres.append(GENRE[randint(0, len(GENRE)-1)])
        productor = (BRAND[randint(0, len(BRAND)-1)] + ""
                     + STUDIO_N[randint(0, len(STUDIO_N)-1)])
        realisator = generate_name()
        actors = []
        for _ in range(randint(1, 4)):
            actors.append(generate_name())
        duration = randint(20, 240)
        movie = {
            "product_type": "film",
            "title": title,
            "type": movie_type,
            "genres": genres,
            "productor": productor,
            "realisator": realisator,
            "actors": actors,
            "duration": duration,
            "release_date": generate_date(),
        }
        products.append(movie)

def generate_books(products, number):
    for _ in range(number):
        title = generate_title()
        authors = []
        for _ in range(randint(1, 3)):
            authors.append(generate_name())
        book_type = BOOK_TYPE[randint(0, len(BOOK_TYPE)-1)]
        genres = []
        for _ in range(randint(1, 5)):
            genres.append(GENRE[randint(0, len(GENRE)-1)])
        editor = (BRAND[randint(0, len(BRAND)-1)] + ""
                  + STUDIO_N[randint(0, len(STUDIO_N)-1)])
        pages = randint(20, 2000)
        date = generate_date()
        book = {
            "product_type": "livre",
            "title": title,
            "type": book_type,
            "authors": authors,
            "editor": editor,
            "pages": pages,
            "release_date": date,
        }
        products.append(book)

def generate_furniture(products, number):
    for _ in range(number):
        furniture_type = FURNITURE[randint(0, len(FURNITURE)-1)]
        date = generate_date()
        constructor = BRAND[randint(0, len(BRAND)-1)]
        colors = []
        for _ in range(randint(1, 3)):
            colors.append(COLOR[randint(0, len(COLOR)-1)])
        material = MAT_FURN[randint(0, len(MAT_FURN)-1)]
        date = generate_date()
        furniture = {
            "product_type": "ameublement",
            "type": furniture_type,
            "constructor": constructor,
            "colors": colors,
            "material": material,
            "release_date": date,
        }
        products.append(furniture)

def generate(db):
    products = db.products
    products.drop()

    products_list = []
    generate_clothes(products_list, NB_PRODUCTS_BY_TYPE)
    generate_music(products_list, NB_PRODUCTS_BY_TYPE)
    generate_movies(products_list, NB_PRODUCTS_BY_TYPE)
    generate_books(products_list, NB_PRODUCTS_BY_TYPE)
    generate_furniture(products_list, NB_PRODUCTS_BY_TYPE)

    return products.insert_many(products_list)
