from django.db import models


class BaseAttribute(models.Model):
    # created
    created_at = models.DateTimeField(auto_now_add=True)

    # time that the attribute is valid
    # may be different than the time it was created
    # adding the index is important because it's used for sorting
    valid_at = models.DateTimeField(db_index=True)

    # device that's the source of the attribute
    device = models.ForeignKey('devices.Device')

    class Meta:
        abstract = True
        get_latest_by = 'valid_at'


class Attribute(BaseAttribute):
    # numerical value of the attribute
    value = models.FloatField()

    # units of the numerical value
    # you may want to add choices to this
    # adding the index is important because it's used for filtering
    units = models.CharField(max_length=10, db_index=True)


class PowerStatus(BaseAttribute):
    # true if on, false if off
    is_on = models.BooleanField()
