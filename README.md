# Pour demarrer app
docker compose up --build -d

# Pour voir si les conteneurs ont bien demarrés
docker compose ps

#Tester l'app
http://localhost/

# Arreter ou demarrer un serveur 
docker compose stop web1
docker compose start web1

# Voir les logs
docker log
docker compose logs -f

# Voir logs d’un service :
docker compose logs -f web1

# Arreter les conteneurs
docker compose down

# supprimer une image 
 docker compose down --rmi local

# Stopper un conteneur
docker stop monconteneur

# Supprimer un conteneur
docker rm monconteneur

# Arrêter tous les conteneurs
docker stop $(docker ps -a -q)

# Supprimer tous les conteneurs
docker rm $(docker ps -a -q)

# Se connecter au conteneur (alpine sh)
docker exec -it monconteneur bash

# Inspecter un conteneur
docker inspect monconteneur
