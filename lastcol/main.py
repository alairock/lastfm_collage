from aiohttp import web
import os
from pathlib import Path
import base64
from . import lastcol


async def handle(request):
    username = request.match_info.get('name', "alairock")
    cols = request.GET.get('cols', 3)
    rows = request.GET.get('rows', 3)
    try:
        collage = lastcol.LastFMImage(username, cols, rows)
        # return send_file(collage.path, mimetype='image/gif')
        contents = open(collage.path, "rb").read()
        return web.Response(body=contents, content_type='image/jpeg')
    except lastcol.LastFMError as e:
        return web.Response(text=str(e))


def run():
    app = web.Application()
    app.router.add_get('/{name}', handle)

    web.run_app(app)

