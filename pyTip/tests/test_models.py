from django.test import TestCase
import datetime
from pyTip.models import PyTip
from django.utils import timezone


class TestModels(TestCase):

    def setUp(self):
        self.pytip1 = PyTip.objects.create(
            tweet_id=16463, timestamp=datetime.datetime(2015, 10, 10, 10), tweet_text='I am a pyton tip', like=34, retweet=6)
    # timestamp=' 2020/11/13 06:34pm' failed time format,It must be in YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ] format.']

    def test_pytip_is_ok(self):
        self.assertEquals(self.pytip1.tweet_id, 16463)
