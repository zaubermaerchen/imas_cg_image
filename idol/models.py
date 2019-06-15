# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
# アイドル情報管理テーブル
class Idol(models.Model):
    idol_id = models.IntegerField(db_column='id', primary_key=True)
    name = models.CharField(max_length=255)
    type = models.IntegerField(default=0)
    rarity = models.IntegerField(default=0)
    cost = models.IntegerField(default=1)
    offense = models.IntegerField(default=0)
    defense = models.IntegerField(default=0)
    max_offense = models.IntegerField(default=0)
    max_defense = models.IntegerField(default=0)
    skill_name = models.CharField(max_length=255)
    skill_id = models.IntegerField(default=0)
    hash = models.CharField(max_length=32)

    class Meta:
        db_table = 'idol'
        ordering = ['idol_id']

