from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'This Command tells me he loves me'

    def add_arguments(self, parser):
        parser.add_argument(
            "--times", help="How many Times do you want me to tell you that i love you")

    def handle(self, *args, **options):
        times = options.get("time")
        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("I love you"))
