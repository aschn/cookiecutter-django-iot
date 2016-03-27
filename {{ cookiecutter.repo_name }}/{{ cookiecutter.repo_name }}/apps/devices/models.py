from django.db import models


class Device(models.Model):
    # created and updated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # device name
    name = models.CharField(max_length=100)

    # manufacturer's id
    # most brands will have some sort of id you'll want to track
    manufacturer_id = models.CharField(max_length=100, unique=True)

    # type, brand name, etc
    # you may want to add choices to this
    device_type = models.CharField(max_length=100)

    # location
    # you may want to add choices to this
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
