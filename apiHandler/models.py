from django.db import models
import string
import random

    
def uid_gen():
    while True:     
        code = ''.join(random.choices(string.ascii_uppercase, k=8))
        if PartyRoom.objects.filter(code=code).count() == 0:
            break
    return code

# Create your models here.
class PartyRoom(models.Model):
    uid = models.CharField(max_length=8, unique=True)
    host = models.CharField(max_length=64, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False,default=1)
    created_at = models.DateTimeField(auto_now=True)

