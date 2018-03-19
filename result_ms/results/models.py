# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Result(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    monto = models.IntegerField()
    fecha = models.DateTimeField(default=timezone.now)
    gol_1 = models.IntegerField(default=0)
    gol_2 = models.IntegerField(default=0)
    winner = models.BooleanField(default=False)
    partido_id = models.IntegerField()
    wallet_id = models.IntegerField()

    #def __str__(self):
    #    return self.id
    def __unicode__(self):
        return unicode(self.id) or u''
