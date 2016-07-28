import os
import csv
from django.core.management import BaseCommand
from testapp.models import *


file_path = os.path.dirname(__file__)
csv_file = file_path+'\index.csv'
print csv_file

KEYS = [
    'number',
    'volume',
    'page',
    'images'
]
class Command(BaseCommand):
    def handle(self, *args, **options):
        with open(csv_file) as f:
            reader = csv.DictReader(f, delimiter="|")
            datalist = [{key: row[key] for key in KEYS} for row in reader]
            print row['images']
            for i in datalist:
                doc, created = TexasDoc.objects.get_or_create(**i)
                if created:
                    self.stdout.write("Object created")
                else:
                    self.stdout.write("Object exists already")
        
        '''
        self.stdout.write("You're running custom command")
        f = open(csv_file,'rb')
        dataReader = csv.reader(f, delimiter='|')
        for row in dataReader:
            if row[0] != 'number': # Ignore the header row, import everything else
                number = row[0]
                volume = row[1]
                page = row[2]
                imagedata = [e for e in row[3].strip('[]').split(',')]
                
                doc, created = TexasDoc.objects.get_or_create(number=number,volume=volume,page=page,images=imagedata)
                if created:
                    self.stdout.write("Object created")
                else:
                    self.stdout.write("Object exists already")
        '''