from __future__ import absolute_import, unicode_literals
from celery.decorators import periodic_task, task
from celery.utils.log import get_task_logger
from pyTip.tweepypy import *
from quickcheck_project.celery import app

logger = get_task_logger(__name__)


@app.task
def update_db():
    return save_to_db()
