# -*- coding: UTF-8 -*-
import sys,os
import csv

from testapp.models import TexasDoc
from django.http import HttpResponse

#sys.path.append(djangoproject_home)
#os.environ['DJANGO_SETTINGS_MODULE'] = 'texasFile.settings'


def import_db(request):

    csv_filepathname="C:/Users/Gayathri Palanimuthu/texasFile/index.csv"
    djangoproject_home="C:/Users/Gayathri Palanimuthu/texasFile"
    dataReader = csv.reader(open(csv_filepathname), delimiter='|')
    for row in dataReader:
        print "!!!!!!!!!!!!!!!!", row
        if row[0] != 'number': # Ignore the header row, import everything else
            doc = TexasDoc()
            doc.number = row[0]
            print "Number!!!",doc.number
            doc.volume = row[1]
            doc.page = row[2]
            print "Page!!!",doc.page
            doc.images = row[3]
            print "Images!!!!", doc.images
            doc.save()
    return HttpResponse("Imported successfully")