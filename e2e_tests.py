import pytest
import requests
import time

@pytest.fixture()
def url():
    return "http://127.0.0.1/?video=http://s1.cluster-name/path/to/the/video"


def test_alternating(url):
    MAX_COUNT_TO_CDN = 9
    response_list = []
    for _ in range(50):
        response_list.append(requests.get(url, allow_redirects=False).headers['Location'])

    alternating_counter = None
    alternation_frequencies = []

    for i in response_list:
        if i == "http://s1.cluster-name/path/to/the/video" and alternating_counter is None:
            alternating_counter = 0
        elif i == "http://my_cdn.localhost/s1/path/to/the/video" and alternating_counter is not None:
            alternating_counter += 1
        elif i == "http://s1.cluster-name/path/to/the/video" and alternating_counter is not None:
            alternation_frequencies.append(alternating_counter)
            alternating_counter = 0

    assert all(map(lambda x: x == MAX_COUNT_TO_CDN, alternation_frequencies))
