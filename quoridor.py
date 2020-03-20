import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description="Jeu quoridor - Phase 1")
    parser.add_argument("-l", "--lister", action="store_true",help="Lister les identifiants de vos 20 dernieres parties.")
    parser.add_argument("idul", metavar="idul", type=str, help="IDUL du joueur")
    #parser.add_argument("nom_du_joueur", metavar="nom_du_joueur", type=str, help="nom du joueur")
    return parser.parse_args()
