
import threading
import time
import wikipedia

from schedule import Scheduler

from .models import Article
from titre_wiki.models import Titre

from titre_wiki.init_titres_db import remplir_BD
from titre_wiki.init_titres_db import vider_BD


allTitres = Titre.objects.values_list('id','titre',named=True)

indx_currentTitre = 0


def addArticle():
    try:

        global indx_currentTitre
        print('# 1 min => Adding article')
        titreToAdd = allTitres[indx_currentTitre]
        indx_currentTitre += 1
        ArticleToAdd = wikipedia.summary(titreToAdd.titre,6)

        newArticle = Article(titre= titreToAdd,corps = ArticleToAdd)
        newArticle.id = titreToAdd.id

        newArticle.save()
        return True
    except wikipedia.exceptions.DisambiguationError as e:
        #in this case the wikipedia api returns exception about the disamiguations of the title
        # so we pass this one and continue adding others
        return True

    return True


def run_continuously(self, interval=1):
    """Continuously run, while executing pending jobs at each elapsed
    time interval.
    @return cease_continuous_run: threading.Event which can be set to
    cease continuous run.
    Please note that it is *intended behavior that run_continuously()
    does not run missed jobs*. For example, if you've registered a job
    that should run every minute and you set a continuous run interval
    of one hour then your job won't be run 60 times at each interval but
    only once.
    """

    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):

        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                self.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()
    return cease_continuous_run

Scheduler.run_continuously = run_continuously

def start_scheduler():

    # Initialisation de la BdD en premier (suppression (vider la bdd) & insertion 100 titres)
    vider_BD()
    remplir_BD()

    # Executer le scheduler asyn
    scheduler = Scheduler()
    scheduler.every(10).seconds.do(addArticle)
    scheduler.run_continuously()
    print('ok')