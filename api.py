import requests
import json


def lister_parties(idul):
    url_lister = 'https://python.gel.ulaval.ca/quoridor/api/lister/'
    try:
        reponse = requests.get(url_lister, params={'idul': idul})
        if reponse.status_code == 200:
            reponse = reponse.text
            json_var = json.loads(reponse)
            json_str = json.dumps(json_var, indent=2)
            print(json_str)
        else:
            print("Le GET sur '{}' a produit le code d'erreur {}".format(url_lister, donnees.status_code))
    except RuntimeError as erreur:
        print(erreur)
        
def initialiser_partie(idul):    
    url_jouer= 'https://python.gel.ulaval.ca/quoridor/api/initialiser/'
    try:
        reponse = requests.post(url_jouer, data={'idul': idul})
        if reponse.status_code == 200:
            json_reponse = reponse.json()
            return json_reponse['id'], json_reponse['état']
        else:
            print("Le POST sur '{}' a produit le code d'erreur {}".format(
                url_jouer, reponse.status_code
            ))
    except RuntimeError as erreur:
        print(erreur)
