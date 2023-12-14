from django.core.management import BaseCommand, CommandError

# you can use only "Command" name for the class
class Command(BaseCommand):
    help = "This is a test command"
    def handle(self, *args, **options):
        print("Hello World")
