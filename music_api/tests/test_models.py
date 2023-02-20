from django.test import TestCase

from music_api.models import Musician


class MusicianTest(TestCase):
    """
    Testing musician model fields.
    """
    @classmethod
    def setUpTestData(cls):
        cls.mus_1 = Musician.objects.create(name='Garfield')

    def setUp(self) -> None:
        pass

    def test_max_length(self):
        # testing max length of name field.
        length = self.mus_1._meta.get_field('name').max_length
        self.assertEqual(100, length)
