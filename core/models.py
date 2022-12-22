from django.db import models


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True


class Task(Timestamp):
    pass

class Organization(Timestamp):
    pass

class Group(Timestamp):
    pass

class Realization(Timestamp):
    pass
