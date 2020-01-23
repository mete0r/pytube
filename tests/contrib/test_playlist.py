# -*- coding: utf-8 -*-
from unittest.mock import MagicMock

from pytube import Playlist



def test_title():
    list_key = "PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3"
    url = "https://www.fakeurl.com/playlist?list=" + list_key
    pl = Playlist(url)
    pl_title = pl.title()
    assert pl_title == "Python Tutorial for Beginners"
