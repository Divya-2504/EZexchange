from django.core.mail import send_mail
from django.conf import settings

def send_buy_email(queryset_buyer_mail,queryset_seller_mail,title):
    subject = "About your product on EZexchange"
    message = f"Hello Sellers, One of your product with {title} is ready for getting bought by a user with email {queryset_buyer_mail}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [queryset_seller_mail]
    send_mail(subject,
            message,
            from_email,
            recipient_list)