from sanic import Sanic
from sanic.response import json, redirect
from dotenv import load_dotenv

import os
import multiprocessing
import aioredis
import redis

from utils import get_server_name, get_video_location

load_dotenv()

REDIS_COUNT_TO_CDN_KEY = "count"
MAX_COUNT_TO_CDN = 9
CDN_HOST = os.getenv("CDN_HOST")

redis_client = redis.Redis().from_url(os.getenv("REDIS"))

# Initial value of counter
if redis_client.get(REDIS_COUNT_TO_CDN_KEY) is None:
    redis_client.set(REDIS_COUNT_TO_CDN_KEY, 0)

async_redis_client = aioredis.from_url(os.getenv("REDIS"))

app = Sanic("Balancer")


@app.route("/")
async def balancer(request):
    if "video" not in request.args:
        return json({"status": "empty video param"})

    video_url = request.args["video"][0]

    count_to_cdn = int(await async_redis_client.get(REDIS_COUNT_TO_CDN_KEY))
    if count_to_cdn >= MAX_COUNT_TO_CDN:
        # It's time to redirect to origin url and set count to zero
        await async_redis_client.set(REDIS_COUNT_TO_CDN_KEY, 0)
        return redirect(to=video_url, status=301)

    # Redirect to CDN with increasing counter
    await async_redis_client.set(REDIS_COUNT_TO_CDN_KEY, count_to_cdn + 1)
    server_name = get_server_name(video_url)
    video_location = get_video_location(video_url)

    target_cdn_url = f"http://{CDN_HOST}/{server_name}{video_location}"
    return redirect(to=target_cdn_url, status=301)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, workers=multiprocessing.cpu_count())
