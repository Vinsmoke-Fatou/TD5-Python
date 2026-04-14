from maths.operations import addition, soustraction, multiplication
from maths.statistiques import moyenne, maximum, minimum
from utils.string_utils import inverser_chaine, compter_mots
import requests

print("=== Opérations mathématiques ===")
print(f"addition(8, 3)       = {addition(8, 3)}")
print(f"soustraction(15, 6)  = {soustraction(15, 6)}")
print(f"multiplication(4, 7) = {multiplication(4, 7)}")

print("\n=== Statistiques sur [10, 20, 30, 40, 50] ===")
nombres = [10, 20, 30, 40, 50]
print(f"Moyenne  : {moyenne(nombres)}")
print(f"Maximum  : {maximum(nombres)}")
print(f"Minimum  : {minimum(nombres)}")

print("\n=== Manipulation de chaînes ===")
phrase = "Bonjour tout le monde"
print(f"Originale : {phrase}")
print(f"Inversée  : {inverser_chaine(phrase)}")
print(f"Nb mots   : {compter_mots(phrase)}")

def tester_requete(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("Requête réussie !")
            print(response.text[:300])
        else:
            print(f"Erreur HTTP : {response.status_code}")
    except Exception as e:
        print(f"Erreur de connexion : {e}")

print("\n=== Test requête HTTP ===")
tester_requete("https://httpbin.org/get")