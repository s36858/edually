from django.core.mail import send_mail
from django.conf import settings


settings.configure()

send_mail('test', 'hallo ich bin ein test', settings.EMAIL_HOST_USER, [
          'brillancy@web.de'], fail_silently=False)
