# GDGE-MongoDB
Gestion de données à grande échelle - MongoDB Assignment

### Démarrer le serveur MongoDB
```
mkdir dbmongo
mongod --shardsvr --dbpath dbmongo --port 27021 &
```

### Peupler la base de donnée
Lancer le script `populate_db.py`

### Connexion à la base de donnée depuis le terminal
```
mongo --host localhost:27021
```

### Arrêter le serveur MongoDB
```
mongod --shutdown --dbpath dbmongo
```
