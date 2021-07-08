#django 3 by ex
# import celery
#from .celery import app as celery_app


# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)
