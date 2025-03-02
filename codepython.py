import random

def nombre_aleatoire(minimum: int, maximum: int) -> int:
    """
    Génère un nombre entier aléatoire entre minimum et maximum (inclus).
    """
    return random.randint(minimum, maximum)

# Exemple d'utilisation
print(nombre_aleatoire(1, 100))
