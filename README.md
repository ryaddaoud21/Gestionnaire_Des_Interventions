

# C'est une application web pour la gestion des interventions , avec deux acteurs ( Administrateurs et techniciens ) 
ou l'administrateur définit des interventions ( missions ) pour les techniciens pour les réaliser.
Coté Administrateur : 
Authentification 
-Registration
-gestion des interventions ( ajouter -supprimer -modifier ) 
-gestion des Technicien( ajouter -supprimer -modifier ) 
-gestion des Client( ajouter -supprimer -modifier ) 
-L’ajout d’une intervention à la base de localisation ( maps )
-Définition d’une calendrie pour les interventions
	

Coté Technicien ( utilisateurs): 
-Authentification 
-Registration
-gestion des interventions (  modifier ) 



# git clone https://github.com/ryaddaoud21/Gestionnaire_Des_Interventions
# cd index
# python3 -m venv venv
# source env/bin/activate
//pour l'installation des exigences 

# pip install -r requirements.txt
//pour la configuration de BDD 

# python manage.py makemigrations
# python manage.py migrate

//pour la création de super utilisateur 

# python manage.py createsuperuser
//pour le lancement de serveur 
# python manage.py runserver

