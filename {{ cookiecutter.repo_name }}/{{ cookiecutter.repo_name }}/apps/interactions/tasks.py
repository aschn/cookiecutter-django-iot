from django.utils import timezone
from {{ cookiecutter.repo_name }}.apps.devices.models import Device
from celery import shared_task
import os


@shared_task
def pull_attributes(device_id=None, **kwargs):
    """
    Pulls attribute data from the device vendor's API,
    stores the attributes in the database,
    and returns the pks of the attributes.
    """
    # SAMPLE IMPLEMENTATION
    # # check device exists
    # device = Device.objects.get(pk=device_id)

    # # fetch attributes
    # data = client.get_attributes(device_id)

    # # create observations
    # pks = []
    # for units, value in data.iteritems():
    #     obs = device.attribute_set.create(
    #         valid_at=timezone.now(),
    #         value=value,
    #         units=units,
    #     )
    #     pks.append(obs.pk)

    # # return pk
    # return pks
    raise NotImplementedError


@shared_task
def pull_status(device_id=None, **kwargs):
    """
    Pulls the current device status from the device vendor's API,
    stores the status in the database,
    and returns the pks of the status.
    """
    # SAMPLE IMPLEMENTATION
    # # check device exists
    # device = Device.objects.get(pk=device_id)

    # # fetch status
    # status_message = client.get_status(device_id)

    # # create status
    # if status_message == 'on':
    #     is_on = True
    # else:
    #     is_on = False
    # status = device.powerstatus_set.create(
    #     valid_at=timezone.now(),
    #     is_on=is_on,
    # )

    # # return pk
    # return [status.pk]
    raise NotImplementedError


@shared_task
def refresh_all(**kwargs):
    """
    Refreshes data and status for all devices
    """
    for device in Device.objects.all():
        pull_status(device.pk)
        pull_attributes(device.pk)


@shared_task
def set_status(device_id=None, is_on=True, **kwargs):
    """
    Sets the device status using the device vendor's API,
    stores the new status in the database,
    and returns the pks of the status.
    """
    # SAMPLE IMPLEMENTATION
    # check device exists
    # device = Device.objects.get(pk=device_id)

    # # turn on or off
    # if is_on:
    #     result = client.turn_on(device_id)
    # else:
    #     result = client.turn_off(device_id)

    # # create status
    # if result['status'] == 'ok':
    #     status = device.powerstatus_set.create(
    #         valid_at=timezone.now(),
    #         is_on=is_on,
    #     )

    #     # return pk
    #     return [status.pk]
    # else:
    #     return []
    raise NotImplementedError


@shared_task
def set_attributes(device_id=None, **kwargs):
    """
    Sets the device attributes using the device vendor's API,
    stores the new attributes in the database,
    and returns the pks of the attributes.
    """
    raise NotImplementedError
