from django.conf import settings
from django.core.mail import send_mail

from celery import shared_task


@shared_task
def sendEmailInSnippetCreation(snippet_name, snippet_description, user_mail):
    subject = 'Snippet "' + snippet_name + '" created successfully'
    body = (
        'The snippet "' + snippet_name + '" was created with the following description: \n'
        + snippet_description
    )
    try:
        if user_mail:
            send_mail(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [user_mail],
                fail_silently=False,
            )
        print("Email enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el email: {e}")
