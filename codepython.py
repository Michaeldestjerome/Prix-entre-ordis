import random

def nombre_aleatoire(minimum: int, maximum: int) -> int:
    """
    Génère un nombre entier aléatoire entre minimum et maximum (inclus).
    """
    return random.randint(minimum, maximum)

def liste_nombres_aleatoires(taille: int, minimum: int, maximum: int) -> list:
    """
    Génère une liste de nombres aléatoires de taille donnée entre minimum et maximum.
    """
    return [nombre_aleatoire(minimum, maximum) for _ in range(taille)]

def moyenne_nombres_aleatoires(taille: int, minimum: int, maximum: int) -> float:
    """
    Génère une liste de nombres aléatoires et retourne leur moyenne.
    """
    nombres = liste_nombres_aleatoires(taille, minimum, maximum)
    return sum(nombres) / len(nombres) if nombres else 0

# Exemple d'utilisation
print(nombre_aleatoire(1, 100))
print(liste_nombres_aleatoires(5, 1, 100))
print(moyenne_nombres_aleatoires(5, 1, 100))
