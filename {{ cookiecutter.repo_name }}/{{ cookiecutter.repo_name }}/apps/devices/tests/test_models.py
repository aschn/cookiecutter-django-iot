from django.test import TestCase
from {{ cookiecutter.repo_name }}.apps.devices.models import Device


class TestDevice(TestCase):
    def setUp(self):
        self.device = Device.objects.create(name='my toi',
                                            device_type='TOI',
                                            location='robohome',
                                            manufacturer_id='0101')

    def test_dates(self):
        self.assertGreater(self.device.updated_at,
                           self.device.created_at)

    def test_str(self):
        self.assertEqual(str(self.device), self.device.name)
