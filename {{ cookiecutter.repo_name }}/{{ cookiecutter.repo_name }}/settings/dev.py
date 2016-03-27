from .common import *
import os


DEBUG = True

# Skip integration tests by default. Usage:
# from unittest import skipIf
# @skipIf(settings.SKIP_INTEGRATION_TESTS)
if os.environ.get('SKIP_INTEGRATION_TESTS', True):
    SKIP_INTEGRATION_TESTS = True
else:
    SKIP_INTEGRATION_TESTS = False
