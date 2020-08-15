
"""
    Definition d'un 'router' pour orienter toutes les operations read/write de l'app article_wiki vers la BdD db_article_wiki
"""

class article_wiki_DBRouter(object):

    def db_for_read(self, model, **hints):

        from django.conf import settings
        """ pour s'assurer que la BdD est bien déclarée dans les confs du projet"""
        if 'db_article_wiki' not in settings.DATABASES:
            return None

        if model._meta.app_label == 'article_wiki':
            return 'db_article_wiki'
        return None

    def db_for_write(self, model, **hints):

        from django.conf import settings
        if 'db_article_wiki' not in settings.DATABASES:
            return None

        if model._meta.app_label == 'article_wiki':
            return 'db_article_wiki'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """ Autoriser (et orienter vers db_article_wiki) toute relation si un modèle de l'app 'article_wiki' est concerné """

        from django.conf import settings
        if 'db_article_wiki' not in settings.DATABASES:
            return None

        if obj1._meta.app_label == 'article_wiki' or obj2._meta.app_label == 'article_wiki':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):


        using = ['article_wiki']

        print("here => "+app_label)

        if app_label in using:
            return db == 'db_article_wiki'

        return None