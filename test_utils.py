import pytest

from utils import get_server_name, get_video_location


@pytest.fixture()
def common_server():
    return "s1"


@pytest.fixture()
def common_video_location():
    return "/video/1488/xcg2djHckad.m3u8"


@pytest.fixture
def common_url(common_server, common_video_location):
    return f"http://{common_server}.origin-cluster{common_video_location}"


def test_get_server_name_successful(common_url, common_server):
    assert get_server_name(common_url) == common_server


def test_get_server_name_useccessful():
    assert get_server_name("http:") is None
    assert get_server_name("http://onlyzonename") is None


def test_get_video_location_successful(common_url, common_video_location):
    assert get_video_location(common_url) == common_video_location


def test_get_video_location_unsuccessful():
    assert get_video_location("http://server") is None
    assert get_video_location("http://server/") is None
    assert get_video_location("http://server-long-name/") is None
    assert get_video_location("http://server-long-name.zone/") is None
