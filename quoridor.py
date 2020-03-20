import argparse


def analyser_commande():
    parser = argparse.ArgumentParser(description="Jeu quoridor - Phase 1")
    parser.add_argument("-l", "--lister", action="store_true",help="Lister les identifiants de vos 20 dernieres parties.")
    parser.add_argument("idul", metavar="idul", type=str, help="IDUL du joueur")
    return parser.parse_args()

def ligne(i):
    r = []
    if (((i+1) // 2) + 1) < 10:
        r = ["{} |".format(((i + 1) // 2) + 1)]
    else:
        r = ["{} |".format(((i + 1) // 2) + 1)]
    return r

def afficher_damier_ascii(grille):
    #fonction permettant dafficher letat du damier et qui ne recoit aucun argument en entree
    grille = {
        "joueurs": [
            {"nom": "idul", "mur": 7, "pos": [5, 5]},
            {"nom": "automate", "murs": 3, "pos": [8, 6]}
        ],
        "mur": {
            "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 8]],
            "verticaux": [[6, 2], [4, 4], [2, 6], [7, 5], [7, 7]]
        }
    }
    board_positions = 9
    espace_horizontal = ((board_positions * 4) - 1)
    jeu_position_x = range(1, (board_positions * 4), 4)
    jeu_position_y = range(((board_positions - 1) * 2), -1, -2)
    legende = "legende: "
    board = [legende]
    for i in reversed(range((board_positions * 2) -1)):
        if (i % 2) == 0:
            board += ligne(i)
            board += [" ", "."]
            board += ([" ", " ", " ", "."] * (board_positions - 1))
            board += [" ", "|\n"]
        else:
            board += ["  |"]
            board += ([" "] * espace_horizontal)
            board += ["|\n"]
