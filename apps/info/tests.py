from django.test import TestCase
from apps.info.models import Info


class InfoTestCase(TestCase):
    def setUp(self):
        Info.objects.create(first_name="name",
                            last_name='surname',
                            birthdate='1993-05-25',
                            bio='test_bio',
                            contacts='091235412',
                            )

    def test(self):
        info = Info.objects.get(first_name='name')
        self.assertEqual(info.last_name, 'surname')
        self.assertEqual(info.bio, 'test_bio')
