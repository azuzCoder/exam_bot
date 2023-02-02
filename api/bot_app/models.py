from django.db import models


class BotUser(models.Model):
    from_id = models.BigIntegerField()
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    passport_number = models.CharField(max_length=255)
    passport_image = models.CharField(max_length=255)
    solution = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.full_name


class BotAdmin(models.Model):
    from_id = models.BigIntegerField(unique=True)
