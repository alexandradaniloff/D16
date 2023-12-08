from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from django.conf import settings
from .models import Post
from django.contrib.auth.models import User


def send_notifications(pk, title, content, subscribes):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': content[0:50],
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email='alexandradaniloff@mail.ru',
        to=subscribes,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=Post.categories.through)
def notify_about_new_post(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categories.all()
        subscribers_emails = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        send_notifications(instance.pk, instance.title, instance.content, subscribers_emails)
