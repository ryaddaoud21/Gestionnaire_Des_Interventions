# Gestionnaire des Interventions

L'application web "Gestionnaire des Interventions" permet de gérer les interventions (missions) par les techniciens pour les reclamations recus de la part de clients. Elle est conçue pour 3 trois types d'utilisateurs : les administrateurs , les techniciens et les clients .

## Fonctionnalités

### Côté Administrateur

- Authentification
- Inscription
- Gestion des interventions (ajouter, supprimer, modifier)
- Gestion des techniciens (ajouter, supprimer, modifier)
- Gestion des clients (ajouter, supprimer, modifier)
- Ajout d'une intervention avec localisation sur une carte
- Définition d'un calendrier pour les interventions

### Côté Technicien (Utilisateurs)

- Authentification
- Inscription
- Gestion des interventions (modifier)

## Utilisation Côté Client -

Bienvenue dans l'application de gestion des interventions. Cette section explique comment les clients peuvent utiliser l'application pour soumettre des réclamations et suivre leur progression.

### Étape 1 : Accès à l'Application

1. Ouvrez votre navigateur et accédez à l'application en utilisant l'URL suivante : [http://localhost:8000/](http://localhost:8000/).

### Étape 2 : Authentification ou Inscription

1. Si vous êtes déjà inscrit, connectez-vous en utilisant votre nom d'utilisateur et votre mot de passe. Sinon, cliquez sur "S'inscrire" pour créer un compte client.

### Étape 3 : Soumission d'une Réclamation

1. Une fois connecté, vous serez redirigé vers le tableau de bord du client.

2. Cliquez sur "Soumettre une Réclamation" pour accéder au formulaire de soumission de réclamation.

3. Remplissez le formulaire en indiquant le titre de la réclamation, une description détaillée du problème, et toute information nécessaire.

4. Cliquez sur "Soumettre" pour envoyer votre réclamation.

### Étape 4 : Suivi de la Réclamation

1. Retournez au tableau de bord du client pour voir la liste de toutes vos réclamations.

2. Vous pouvez voir le statut de chaque réclamation, par exemple, "En Attente" ou "En Cours de Traitement".

3. À mesure que l'administrateur travaille sur votre réclamation, le statut sera mis à jour pour refléter son état actuel.

### Étape 5 : Notifications

1. Lorsque l'administrateur met à jour le statut de votre réclamation, vous recevrez des notifications pour vous informer des mises à jour.

2. Cliquez sur l'icône de notification dans la barre de navigation pour consulter vos notifications.

3. Vous verrez les détails des mises à jour de réclamation dans la liste des notifications.

### Étape 6 : Suivi des Interventions (le cas échéant)

1. Si l'administrateur crée une intervention en réponse à votre réclamation, vous pouvez également suivre cette intervention depuis le tableau de bord du client.

2. Consultez la liste des interventions pour voir les détails, y compris la date de l'intervention, le technicien attribué, etc.

C'est ainsi que les clients peuvent utiliser l'application pour soumettre des réclamations, suivre leur progression et rester informés des mises à jour. Nous espérons que cette application vous offre une expérience fluide dans la gestion des interventions.


## Installation

Pour déployer cette application localement, suivez les étapes ci-dessous :

1. Clonez le dépôt depuis GitHub :
   ```shell
   git clone https://github.com/ryaddaoud21/Gestionnaire_Des_Interventions
   cd Gestionnaire_Des_Interventions


2. Installez les dépendances requises  :
   ```shell
  pip install -r requirements.txt


3. Configurez la base de données :
   ```shell
   python manage.py makemigrations
   python manage.py migrate
   
4. Créez un superutilisateur pour accéder à la zone d'administration :
   ```shell
   python manage.py createsuperuser

5.Lancez le serveur de développement  :
   ```shell
   python manage.py runserver

## Utilisation

1. Accédez à l'application dans votre navigateur en utilisant l'URL suivante : [http://localhost:8000/](http://localhost:8000/).

2. Connectez-vous en utilisant les identifiants de l'administrateur ou créez un compte pour un technicien.

3. Utilisez les fonctionnalités de l'application selon votre rôle (administrateur ou technicien) comme décrit ci-dessus.

## Contributions

Les contributions à ce projet sont les bienvenues. N'hésitez pas à signaler des problèmes en créant une "Issue" ou à soumettre des demandes de fusion (pull requests) pour améliorer l'application. Nous encourageons la participation de la communauté pour rendre cette application encore meilleure.

## Auteur

Ce projet a été développé par Ryad ((mailto:m.ryaddaoud21@gmail.com)).
