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
    url_lister = 'https://python.gel.ulaval.ca/quoridor/api/lister/'
    response = requests.post(url_lister, data={'idul': idul})
    if response.status_code == 200:
        response = response.text
        json_var = json.loads(response)
        json_str = json.dumps(json_var, indent=2)
        print(json_str)
    else:
        print("Le POST sur '{}' a produit le code d'erreur {}.".format(
            url_lister, response.status_code)
        )
