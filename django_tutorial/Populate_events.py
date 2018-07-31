import os

# configure the setting for the project before you call any code

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tutorial.settings')

import django

django.setup()

import random
from Music.models import Album
from faker import Faker

# fake populating script


# create an instance
fake_gen = Faker()

album = ['Culture II', 'Scorpion', 'Golden Hour', 'Camilla', 'Black Panther', 'Voicenotes', 'Bad Witch', 'Mania',
         'Sweetener', 'You\'re not alone']


# create function to add the topics
# without foreign keys and with one entry field
def add_album():
    t = Album.objects.get_or_create(album_title=random.choice(album))[0]
    t.save()
    return t


# with foreign keys
def populate(N=5):
    for entry in range(N):
        # get the customer for the entry
        # add_customer()
        album = add_album()

        # create fake data
        fake_name = fake_gen.name()


        # create a new entry
        webpg = Album.objects.get_or_create(artist=fake_name)[0]


if __name__ == '__main__':
    print('Populating my script')
