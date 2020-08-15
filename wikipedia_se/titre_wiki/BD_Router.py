
"""
    Definition d'un 'router' pour orienter toutes les operations read/write de l'app titre_wiki vers la BdD db_titre_wiki
"""

class titre_wiki_DBRouter(object):

    def db_for_read(self, model, **hints):

        from django.conf import settings

        """ pour s'assurer que la BdD est bien déclarée dans les confs du projet"""
        if 'db_titre_wiki' not in settings.DATABASES:
            return None

        if model._meta.app_label == 'titre_wiki':
            return 'db_titre_wiki'
        return None

    def db_for_write(self, model, **hints):

        from django.conf import settings
        if 'db_titre_wiki' not in settings.DATABASES:
            return None

        if model._meta.app_label == 'titre_wiki':
            return 'db_titre_wiki'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """ Autoriser (et orienter vers db_titre_wiki) toute relation si un modèle de l'app 'titre_wiki' est concerné """

        from django.conf import settings
        if 'db_titre_wiki' not in settings.DATABASES:
            return None

        if obj1._meta.app_label == 'titre_wiki' or obj2._meta.app_label == 'titre_wiki':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        using = ['titre_wiki']

        print("here => "+app_label)

        if app_label in using:
            return db == 'db_titre_wiki'

        return None



"""
    Definition d'un 'router' pour la BdD default. ca sera pour les operations liées aux (admin,auth,sessions,contentType)
    afin d'eviter les collisions avec les deux autres BdD pendant la creation de superuser.
"""

class AuthRouter(object):
    auth_related = ('auth','admin','contenttypes','sessions',)

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.auth_related:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.auth_related:
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.auth_related or obj2._meta.app_label in self.auth_related:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.auth_related:
            return db == 'default'
        return None
