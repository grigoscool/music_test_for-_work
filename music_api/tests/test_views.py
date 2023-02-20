from django.test import TestCase

from music_api.models import Musician
from music_api.serializers import MusicianSerializers


class GetListMusician(TestCase):
    """
    Testing get list of musicians.
    """
    def setUp(self):
        self.mus = Musician.objects.create(name='Dory')

    def test_valid_get_list(self):
        # testing status 200 and custom serializer work.
        response = self.client.get('/api/v1/musician-list/')
        response.render()
        serialized = MusicianSerializers(self.mus)
        self.assertEqual(200, response.status_code)
        expected_data = {'id': 1, 'name': 'Dory'}
        self.assertEqual(serialized.data, expected_data)
