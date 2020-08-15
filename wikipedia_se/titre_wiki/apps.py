from django.apps import AppConfig


class TitreWikiConfig(AppConfig):
    name = 'titre_wiki'

def ready(self):
    import titre_wiki.django_Signals
