from django.core.exceptions import ValidationError
from django.test import TestCase

from music_api.models import Musician


class ValidatorsTest(TestCase):
    """
    Testing custom validators.
    """
    def test_validator_musician_name(self):
        # testing musician name starts with capitalize.
        item_1 = Musician(name='doodd')
        self.assertRaises(ValidationError, item_1.full_clean)
        item_1 = Musician(name='dDd')
        self.assertRaises(ValidationError, item_1.full_clean)
