from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Snippet
from .tasks import sendEmailInSnippetCreation


@receiver(post_save, sender=Snippet)
def send_creation_email(sender, instance=None, created=False, **kwargs):
    if created:
        sendEmailInSnippetCreation.delay(
            instance.name, instance.description, "almarazmartin13@gmail.com"
        )