# Principes de Programmation - API, SOAP et Docker

## Description

Ce dépôt regroupe plusieurs travaux pratiques et démonstrations autour des architectures logicielles, des services web (REST et SOAP), de l'accès aux données (DAO) et de la conteneurisation. 

L’objectif principal est de mettre en œuvre différentes approches de communication entre applications et d'organiser le code selon des principes de conception clairs, dans un cadre d’apprentissage.

---

## Objectifs pédagogiques

Ce dépôt permet de pratiquer plusieurs notions vues en cours, notamment :

- la création d’API REST en Python en utilisant le patron de conception DAO (Data Access Object) ;
- la consommation d’API depuis des scripts et des clients PHP ;
- la mise en place de services web SOAP en Java ;
- l’initialisation et la connexion à une base de données relationnelle via des scripts SQL ;
- la conteneurisation des environnements d'exécution à l'aide de Docker.

---

## Organisation du dépôt

Le dépôt est structuré en plusieurs parties distinctes couvrant différentes technologies et architectures :

- **API + DAO (Python)**
  - implémentation d'une API avec séparation des responsabilités (DAO) ;
  - gestion de la configuration, de la base de données et des requêtes (`app.py`, `db.py`, `repository.py`) ;
  - script SQL d'initialisation (`db.sql`).

- **Services SOAP (Java)**
  - création d'un service web SOAP (`MyService.java`) gérant une entité `Etudiant` ;
  - application serveur pour exposer le service (`Application.java`).

- **Client Étudiant (PHP)**
  - interface web client complète pour interagir avec les services (`student_client/`) ;
  - structuration avec des vues, un service métier (`StudentService.php`) et des styles (`style.css`).

- **Tests d'API (PHP)**
  - ensemble de scripts PHP indépendants (`test_api1.php` à `test_api7.php`) permettant de tester différentes méthodes de requêtage d'API.

- **Conteneurisation (Docker)**
  - présence d'un `dockerfile` pour le déploiement ou l'exécution isolée des services.

---

## Modules disponibles

- `API+DAO/`
  - implémentation d’une API Python avec un accès structuré aux données (Pattern Repository).
  
- `SOAP/`
  - implémentation d'un service web basé sur le protocole SOAP avec Java.

- `student_client/`
  - application client PHP "front-end" avec son propre routage et ses vues.

- `PHP/`
  - bac à sable contenant divers tests de consommation d'API en PHP.

- `docker/`
  - fichiers de configuration pour créer des conteneurs Docker.

---

## Technologies utilisées

- Python (API, Scripting avec `demo1.py`)
- Java (Web Services SOAP)
- PHP (Client web, requêtage HTTP)
- SQL (Base de données)
- Docker
- HTML / CSS (Interface utilisateur)

---

## Remarques

- Ce dépôt a une finalité pédagogique.
- Les dépendances Python nécessaires au projet sont listées dans le fichier `requirements.txt` à la racine.
- Les différentes parties peuvent être exécutées et étudiées séparément.

---

## Auteur

Ayoub HAKIM
