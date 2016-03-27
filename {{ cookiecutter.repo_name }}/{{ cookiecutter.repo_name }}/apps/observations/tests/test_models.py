from django.test import TestCase
from django.utils import timezone
from {{ cookiecutter.repo_name }}.apps.devices.models import Device
from {{ cookiecutter.repo_name }}.apps.observations.models import Attribute, PowerStatus
from datetime import timedelta


class TestAttribute(TestCase):
    def setUp(self):
        # set up device
        self.device = Device.objects.create(name='my toi',
                                            device_type='TOI',
                                            location='robohome')

    def test_dates(self):
        # create observation in future
        obs = Attribute.objects.create(
            valid_at=timezone.now()+timedelta(hours=5),
            device=self.device,
            value=5,
            units='kW',
        )

        # created and valid are different
        self.assertLess(obs.created_at, obs.valid_at)

    def test_latest_by(self):
        # set up observations going backward in time
        sample_time = timezone.now()
        for ihour in range(10):
            Attribute.objects.create(
                valid_at=sample_time-timedelta(hours=ihour),
                value=ihour*0.5,
                units='kW',
                device=self.device,
            )

        # get latest and earliest
        latest = Attribute.objects.latest()
        earliest = Attribute.objects.earliest()

        # latest should have later valid_at but earlier created_at
        self.assertGreater(latest.valid_at, earliest.valid_at)
        self.assertLess(latest.created_at, earliest.created_at)

    def test_value_numeric(self):
        # raises ValueError when trying to cast string 'badvalue' to float
        self.assertRaises(ValueError, Attribute.objects.create,
                          valid_at=timezone.now(),
                          device=self.device,
                          value='badvalue',
                          units='goodunits')


class TestPowerStatus(TestCase):
    def setUp(self):
        # set up device
        self.device = Device.objects.create(name='my toi',
                                            device_type='TOI',
                                            location='robohome')

    def test_dates(self):
        # create status in future
        status = PowerStatus.objects.create(
            valid_at=timezone.now()+timedelta(hours=5),
            device=self.device,
            is_on=True,
        )

        # created and valid are different
        self.assertLess(status.created_at, status.valid_at)

    def test_latest_by(self):
        # set up status going backward in time
        sample_time = timezone.now()
        for ihour in range(10):
            PowerStatus.objects.create(
                valid_at=sample_time-timedelta(hours=ihour),
                value=ihour*0.5,
                is_on=True,
            )

        # get latest and earliest
        latest = PowerStatus.objects.latest()
        earliest = PowerStatus.objects.earliest()

        # latest should have later valid_at but earlier created_at
        self.assertGreater(latest.valid_at, earliest.valid_at)
        self.assertLess(latest.created_at, earliest.created_at)

    def test_value_bool(self):
        # raises ValueError when trying to cast string 'badvalue' to float
        self.assertRaises(ValueError, PowerStatus.objects.create,
                          valid_at=timezone.now(),
                          device=self.device,
                          is_on='badvalue')
