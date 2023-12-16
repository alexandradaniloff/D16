import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_monday_8am':{
        'task': 'news.tasks.weekly_send_email_task',
        #'schedule': crontab(),
        #срабатывание 1 раз в минуту
        #'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        'schedule': crontab(hour=11, minute=50, day_of_week='saturday'),
        'args':()
    }
}
app.conf.timezone = 'UTC'
# реальное время (UTC 3) больше на 3часа , чем (UTC)
app.autodiscover_tasks()