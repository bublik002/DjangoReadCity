from celery import shared_task
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from ReadCity.celery import app
from .models import ViewedModel
from datetime import timedelta
from django.utils import timezone
from ReadCity import settings

@app.task
def send_verification_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            'Verify your  account',
            'Follow this link to verify your account: '
            'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        print("Tried to send verification email to non-existing user '%s'" % user_id)


@shared_task
def clean_viewed():
    ViewedModel.objects.filter(date_viewed__lt=timezone.now() - timedelta(days=7)).delete()
