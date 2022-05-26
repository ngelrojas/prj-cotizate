from django.core.management.base import BaseCommand
from django.db import transaction
from core.user import User


class Command(BaseCommand):
    help = "provider user name and password"

    def success(self, message):
        return self.stdout.write(self.style.SUCCESS(message))

    def warning(self, message):
        return self.stdout.write(self.style.WARNING(message))

    def error(self, message):
        return self.stdout.write(self.style.ERROR(message))

    def handle(self, *args, **options):
        self.warning(
            "if something goes wrong after installations, \n"
            "please user develop environment: \n"
            "docker-compose exec api python3 manage.py flush \n"
        )
        with transaction.atomic():
            try:
                # create superuser
                User.objects.create_superuser("admin@cotizate.com", "admin2021")
                self.success("admin user created.")

                # create user one
                User.objects.create_user(
                    email="jhon@yopmail.com",
                    password="me123456",
                    first_name="jhon",
                    last_name="doe",
                    type_user=1,
                    is_activate=True,
                )
                # create user two
                User.objects.create_user(
                    email="mery@yopmail.com",
                    password="me123456",
                    first_name="mery",
                    last_name="doe",
                    type_user=2,
                    is_activate=True,
                )
                # create user three
                User.objects.create_user(
                    email="azumi@yopmail.com",
                    password="me123456",
                    first_name="jhon",
                    last_name="doe",
                    type_user=1,
                    is_activate=True,
                )

                self.success("users created.")
            except Exception as err:
                self.error(f"{err}")
