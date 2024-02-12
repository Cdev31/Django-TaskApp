from django.db import models
from django.db.models import CharField,BooleanField ,TextField, ForeignKey, CASCADE, DateTimeField
from django.contrib.auth.models import User



class Category (models.Model):
    category_name = CharField()
    description = TextField(  max_length=80 )
    user = ForeignKey( User, on_delete=CASCADE )
    

class Task (models.Model):
    title = CharField( max_length=70 )
    description = TextField(  max_length=130 )
    image = TextField()
    important_level = CharField()
    done = BooleanField( default=False )
    date_completed = DateTimeField( null=False )
    created = DateTimeField( auto_now_add=True )
    user = ForeignKey( User, on_delete=CASCADE )
    category = ForeignKey( Category, on_delete=CASCADE )
