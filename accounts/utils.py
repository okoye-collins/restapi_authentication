import random
from django.core.mail import EmailMessage
from django.conf import settings

from .models import User, OneTimePassword


def generate_otp(length=6):
    return "".join(str(random.randint(1, 9)) for _ in range(length))


def send_otp_code(email):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        raise ValueError("User with this email does not exist.")

    otp_code = generate_otp()
    current_site = "auth.com"
    email_body = (
        f"Hi {user.first_name}, thanks for signing up on {current_site}. "
        f"Please verify your email with the one-time passcode: {otp_code}"
    )

    OneTimePassword.objects.create(user=user, code=otp_code)

    email = EmailMessage(
        subject="One-time passcode for Email Verification",
        body=email_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
    )
    email.send(fail_silently=False)
