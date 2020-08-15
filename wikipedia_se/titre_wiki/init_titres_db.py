import wikipedia
from .models import Titre
from article_wiki.models import Article

LANGUE = 'fr'
TITRES_NBR = 100


"""
    vider_BD() : appelé au premier lancement du serveur pour vider la BdD avant de commencer les processus.
    remplir_BD(): pour remplir la db_titre_article par 100 random article recuperés par wikipedia api.
    
"""

def vider_BD():
    try:
        Titre.objects.all().delete()
        Article.objects.all().delete()
        return True
    except Exception as e:
        raise Exception('Erreur !! emplacement => #FUNC: remplir_BD #APP: titre_wiki ' + str(e))

def remplir_BD():
    try:
        wikipedia.set_lang(LANGUE)
        titres_bulk = wikipedia.random(TITRES_NBR)

        Titre.objects.bulk_create(Titre(titre=single_titre , taille=len(single_titre)) for single_titre in titres_bulk)
        return True

    except Exception as e:
        raise Exception('Erreur !! emplacement => #FUNC: remplir_BD #APP: titre_wiki ' + str(e))
