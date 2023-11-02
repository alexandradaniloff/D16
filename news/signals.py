from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


from django.conf import settings
from .models import PostCategory

def send_notifications(preview, pk, title, subscribes):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )
    msg = EmailMultiAlternatives(
        subject = title,
        body = '',
        from_email = 'alexandradaniloff@gmail.com',
        to = subscribes,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_post(sender, instans, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instans.category.all()
        subscribers_emails = []

        for cat in categories:
            subscribers = cat.subscribers.all()
            subscribers_emails += [s.email for s in subscribers]

        send_notifications(instans.preview(), instans.pk, instans.title, subscribers_emails)