from typing import Optional
import re
from urllib.parse import urlparse


def get_server_name(url_str: str) -> Optional[str]:
    """
    returns s1 if get
    http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8
    or None if not match
    """
    netloc = urlparse(url_str).netloc
    if not netloc:
        return None

    result = re.search(r"^([A-Za-z_0-9-]+)(?:\.[A-Za-z_0-9-]+)$", netloc)
    if result:
        result = result.group(1)
    return result


def get_video_location(url_str) -> str:
    """
    returns /video/1488/xcg2djHckad.m3u8 if get
    http://s1.origin-cluster/video/1488/xcg2djHckad.m3u8
    or None if
    """
    result = urlparse(url_str).path
    if result == "" or result == "/":
        result = None
    return result
