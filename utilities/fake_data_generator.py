from faker import Faker
import re


class FakeDataGenerator:
    def __init__(self, locale='ru_RU'):
        self.fake = Faker(locale)

    def random_name(self):
        return self.fake.first_name()

    def random_surname(self):
        return self.fake.last_name()

    def random_phone(self):
        return self.fake.phone_number()

    def random_email(self):
        return self.fake.email()

    def random_address(self):
        return self.fake.address()