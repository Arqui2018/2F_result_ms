# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Result(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    amount = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    g_local = models.IntegerField(default=0)
    g_visit = models.IntegerField(default=0)
    winner = models.BooleanField(default=False, blank=True)
    match_id = models.IntegerField()
    wallet_id = models.IntegerField()

    #def __str__(self):
    #    return self.id
    def __unicode__(self):
        return unicode(self.id) or u''
