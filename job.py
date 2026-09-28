import os

a = 2 
print("coucou", a)

# Récupérer le secret depuis la variable d'environnement
secret_token = os.getenv('SECRET_API_TOKEN')
print(f"Token reçu : {secret_token}")