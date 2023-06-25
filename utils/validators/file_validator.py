import re
from datetime import datetime

from celery import shared_task
import pandas as pd


class FileValidator:

    def __init__(self, filename):
        self.filename = filename
        file_extension = filename.name.rsplit('.', 1)[-1].lower()

        self.data = pd.read_csv(filename, dtype={'phone': str})
        if file_extension == 'xls' or file_extension == 'xlsx':
            self.data = pd.read_excel(filename, dtype={'phone': str})

        pd.set_option('display.max_columns', None)
        self.errors = []

    def validate_email(self, index: int, email: str):
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if email is None or not isinstance(email, str) or not re.match(email_regex, email):
            self.data.drop(index, inplace=True)
            self.errors.append(
                f"The email {email} is invalid, record deleted."
            )

    def validate_document_number(self, index: int, document_number: int):
        if not pd.isnull(document_number):
            document_number = int(document_number)

        if document_number is None or not isinstance(document_number, int) or document_number <= 0:
            self.data.drop(index, inplace=True)
            self.errors.append(
                f"The document number {document_number} is invalid, record deleted."
            )

    def validate_born_date(self, index: int, born_date: str):
        date_format = "%Y-%m-%d"

        try:
            if born_date is None or not isinstance(born_date, str):
                raise ValueError("Birth date must be a string")

            self._is_past_date(datetime.strptime(born_date, date_format))
        except ValueError:
            self.data.drop(index, inplace=True)
            self.errors.append(f"The date {born_date} is invalid, record deleted.")

    def _is_past_date(self, date):
        current_date = datetime.now().date()
        date = date.date()
        string_date = date.strftime("%Y-%m-%d")
        if date >= current_date:
            self.errors.append(
                f'The date {string_date} cannot be later than the current date, record deleted.'
            )

    def validate_gender(self, index: int, gender: str):
        allowed_genders = ['male', 'female', 'other']

        if gender is None or gender not in allowed_genders:
            self.data.drop(index, inplace=True)
            self.errors.append(
                f"The gender {gender} is invalid, record deleted."
            )

    def validate_phone(self, index: int, phone: str):
        phone_regex = r'^\+?57\d{10}$'
        if not '+' in str(phone):
            phone = "+{}".format(phone)

        if phone is None or not re.match(phone_regex, phone):
            self.data.drop(index, inplace=True)
            self.errors.append(
                f"The phone number {document_number} is invalid, record deleted."
            )

    def validate_file(self):
        for index, row in self.data.iterrows():
            self.validate_row(index, row)

        if len(self.errors) > 0:
            self.errors.insert(0, "File uploaded with errors.")

    def validate_row(self, index: int, row):
        email = str(row['email'])
        document_number = row['document_number']
        born_date = row['born_date']
        gender = row['gender']
        phone = row['phone']

        self.validate_email(index, email)
        self.validate_document_number(index, document_number)
        self.validate_born_date(index, born_date)
        self.validate_gender(index, gender)
        self.validate_phone(index, phone)

    def pd_to_list_of_dict(self):
        return self.data.to_dict('records')