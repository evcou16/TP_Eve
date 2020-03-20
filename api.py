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

        def jouer_coup(id_partie, type_coup, position):
    url_jouer = 'https://python.gel.ulaval.ca/quoridor/api/jouer/'
    try:
        reponse = requests.post(url_jouer, data={'id': id_partie,
        'type': type_coup, 'pos': position})
        if reponse.status_code == 200:
            json_reponse = reponse.json()
            if 'gagnant' in json_reponse:
                raise StopIteration(json_reponse['gagnant'])
            elif 'message' in json_reponse:
                print(json_reponse['message'])
            else:
                return json_reponse
        else:
            print("Le POST sur '{}' a produit le code d'erreur {}.".format(
                url_jouer, reponse.status_code
            ))
    except RuntimeError as erreur:
        print(erreur)
