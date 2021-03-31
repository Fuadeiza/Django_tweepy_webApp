from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pyTip.views import tweet_list


class TestUrls(SimpleTestCase):

    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, tweet_list)
