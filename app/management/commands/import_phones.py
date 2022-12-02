from django.core.management.base import BaseCommand
from app.models import Phone
import csv


def create_phone():
    with open('phones.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            phone = Phone(name=row['Name'], price=row['price'], 
            image=row['image'], release_date=row['release_date'], 
            lte_exists=row['lte_exists'], slug='-'.join(row['Name'].split()
            )).save()
            
            
class Command(BaseCommand):
    help = 'Добавление телефона'

    def handle(self, *args, **options):
        create_phone()
        print('Добавление телефонов прошло успешно')

                  