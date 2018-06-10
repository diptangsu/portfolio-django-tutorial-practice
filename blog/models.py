from django.db import models

'''
create model
add model to settings
create a migration
migrate
add model to admin
'''


class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
