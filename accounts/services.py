import os
from typing import Optional

from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.conf import settings
from accounts.models import CustomUser
from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string
from django.utils.timezone import now


def send_sign_in_email(user: CustomUser) -> None:
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    # verification_link = f"{os.environ['EMAIL_VERIFICATION_URL']}/{uid}/{token}/"
    # verification_link = f"{settings.EMAIL_VERIFICATION_URL}/{uid}/{token}/"
    verification_link = f"http://localhost:8000/accounts/verify-email/{uid}/{token}/"

    subject = 'Verify your email address 🚀'
    message = (
        'Hi there 🙂\n'
        'Please click '
        f'<a href="{verification_link}" target="_blank">here</a> '
        'to verify your email address'
    )
    # NEWWWWWWWWWWWWWWWWWWWW
    # print("Direct getenv:", os.getenv("EMAIL_VERIFICATION_URL"))
    # print("Using verification link:", verification_link)
    # print("ENV VERIFICATION URL:", repr(settings.EMAIL_VERIFICATION_URL))
    # message_id = f"<{get_random_string(12)}@{settings.EMAIL_HOST}>"

    # email = EmailMessage(
    #     subject=subject,
    #     body=message,
    #     from_email=settings.EMAIL_HOST_USER,
    #     to=[user.email],
    #     headers={'Message-ID': message_id}
    # )
    # email.content_subtype = 'html'
    # email.send()
    #IT KEEPS SENDING REMINDER MAILS IN THE SAME THREAD WHEN SIGNING IN WITH GMAIL.COM
    ###################################
    send_mail(subject, '', settings.EMAIL_HOST_USER, [user.email], html_message=message)

def decode_uid(uidb64: str) -> Optional[str]:
    """Decode the base64 encoded UID."""
    try:
        return urlsafe_base64_decode(uidb64).decode()
    except (TypeError, ValueError, OverflowError) as e:
        print(f'{e = }')
        return None

def get_user_by_uid(uid: str) -> Optional[CustomUser]:
    """Retrieve user object using UID."""
    try:
        return CustomUser.objects.get(pk=uid)
    except CustomUser.DoesNotExist as e:
        print(f'{e = }')
        return None