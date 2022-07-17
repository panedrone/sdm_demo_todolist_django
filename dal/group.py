"""
This code was generated by a tool. Don't modify it manually.
http://sqldalmaker.sourceforge.net
"""

from django.db import models


class Group(models.Model):
    g_id = models.AutoField(db_column='g_id', primary_key=True)
    g_name = models.CharField(db_column='g_name', max_length=65535, db_index=True, unique=True)
    g_comments = models.CharField(db_column='g_comments', max_length=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'