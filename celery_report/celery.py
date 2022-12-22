import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_report.settings")
app = Celery("celery_report")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()