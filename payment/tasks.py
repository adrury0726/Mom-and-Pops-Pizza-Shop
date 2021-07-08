from io import BytesIO
from celery import task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order
#import xhtml2pdf
#from xhtml2pdf import pisa
@task
def payment_completed(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    # create invoice e-mail
    subject = f'My Shop - EE Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject,
                         message,
                         'admin@myshop.com',
                         [order.email])
#THIS IS FOR XHTML2PDF
####    # generate PDF
####    html = render_to_string('orders/order/pdf.html', {'order': order})
####    out = BytesIO()
####    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
####    weasyprint.HTML(string=html).write_pdf(out,
####                                          stylesheets=stylesheets)
##    # attach PDF file
##    email.attach(f'order_{order.id}.pdf',
##                 out.getvalue(),
##                 'application/pdf')
##    # send e-mail
##    email.send()

#works for views.py in orders
##    template_path = 'orders/order/pdf.html'
##    order = get_object_or_404(Order, id=order_id)
##    context = {'order': order}
##    response = HttpResponse(content_type='application/pdf')
##    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
##    template = get_template(template_path)
##    html = render_to_string('orders/order/pdf.html', context)
##    pdf = open('order.pdf', "w+b")
##    #creating the pdf
##    pisa_status = pisa.CreatePDF(html, dest=response)
##    if pisa_status.err:
##      return HttpResponse('We had some errors <pre>' + html + '</pre>')
##    return response

#THIS IS FOR WEASYPRINT
    # generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out,
                                          stylesheets=stylesheets)
    # attach PDF file
    email.attach(f'order_{order.id}.pdf',
                 out.getvalue(),
                 'application/pdf')
    # send e-mail
    email.send()


