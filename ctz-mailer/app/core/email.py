from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class CotizateSendEmail(EmailMultiAlternatives):

    def __init__(
            self, subject='', body='', from_email=None, to=None,
            bcc=None, connection=None, attachments=None, headers=None,
            cc=None, reply_to=None):
        """initialize parent class with the defautls attrs"""
        super().__init__(
            subject, body, from_email, to, bcc,
            connection, attachments, headers, cc,
            reply_to)

    def send_email_with_custom_template(
            self, template_name: str, context: dict):
        """set up send email with custom template"""
        email_html_message = render_to_string(template_name, context)
        self.attach_alternative(email_html_message, 'text/html')
        self.send(fail_silently=False)
        return self
