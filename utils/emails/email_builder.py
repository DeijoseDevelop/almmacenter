import os

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from apps.importer_scrapper.tasks import send_email_task


class EmailBuilder(object):

    def __init__(self):
        self.template = None
        self.context = None
        self.subject = None
        self.emails = []

    def set_template(self, template: str):
        self.template = template
        return self

    def add_email(self, email: str):
        self.emails.append(email)
        return self

    def set_context(self, context: dict):
        self.context = context
        return self

    def set_subject(self, subject: str):
        self.subject = subject
        return self

    def build(self):
        if not self.template or not self.context or not self.subject:
            raise ValueError("Template, context, and subject must be set.")

        html_message = render_to_string(self.template, self.context)
        plain_message = strip_tags(html_message)
        from_email = os.getenv("EMAIL_HOST_USER")
        email = EmailMultiAlternatives(
            self.subject,
            plain_message,
            from_email,
            self.emails,
        )
        email.content_subtype = 'html'
        email.attach_alternative(html_message, "text/html")

        return email

    def send(self):
        email = self.build()
        send_email_task.delay(
            email.subject,
            email.from_email,
            email.to,
            email.body,
            email.alternatives[0][0]
        )
        self.emails.clear()
