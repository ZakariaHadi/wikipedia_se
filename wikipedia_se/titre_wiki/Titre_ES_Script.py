from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch


# creation de la connextion avec le serveur elasticSearch
connections.create_connection()

# ElasticSearch "model"
class TitreIndex(Document):
    titre = Text()

    class Meta:
        index = 'titre-index'

# Bulk indexing function
def bulk_indexing():
    TitreIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in Titre.objects.all().iterator()))

# Simple search function
def search(titre):
    newSearch = Search().filter('term', titre=titre)
    response = newSearch.execute()
    return response

