from maths import *

print(addition(5, 3))
print(moyenne([10, 20, 30]))

try:
    print(somme_des_carres([1, 2, 3]))
except NameError as e:
    print(f"Erreur attendue : {e}")
    print("=> somme_des_carres n'est pas dans __all__")