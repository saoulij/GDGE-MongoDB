# GDGE-MongoDB
Gestion de données à grande échelle - MongoDB Assignment

### Démarrer le serveur MongoDB
```
mkdir dbmongo
mongod --shardsvr --dbpath dbmongo --port 27021 &
```

### Peupler la base de donnée et créer les indexes
Lancer le script `populate_db.py` du répertoire `populate/`.

La librairie PyMongo est nécessaire et peut être installée via la commande `pip install pymongo --user`.

### Connexion à la base de donnée depuis le terminal
```
mongo --host localhost:27021
```

### Exécuter les requêtes
Les requêtes sont disponibles dans leurs fichiers respectifs dans le répertoire `queries/`.

### Arrêter le serveur MongoDB
```
mongod --shutdown --dbpath dbmongo
```
