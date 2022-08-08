# from celery import task
from celery import shared_task
from django.core.mail import send_mail
from  .models import Order


@shared_task
def order_created(order_id):
    """
    task to send email notfication when a order is successfully placed
    """
    order = Order.objects.get(id=order_id) 
    subject = f'Order nr. {order.id} successfully placed in Xahan shop'
    message = f'Dear {order.first_name},\n\n' \
                f'You have successfully placed an order.' \
                f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject, message, 'admin@xahanshop.com', [order.email,])
    return mail_sent
