from django.core.mail import send_mail
from django.contrib.auth.models import User

def admin_emails():
    return User.objects.filter(is_staff=True).values_list('email', flat=True)

def product_update_email(pk, changed_fields):
  return send_mail(
          'Product {} updated'.format(pk),
          '''Product {} has been updated.
          The following fields where changed: {}'''
          .format(pk, changed_fields),
          'admin@zebrands.com',
          admin_emails(),
          fail_silently=False,
          )