# -*- coding: utf-8 -*-
import io
import json
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from image.settings import *
from PIL import Image

class View(View):
    def get_image(self, attribute: str, hash: str):
        req = Request(IMAGE_URL_FORMAT % (attribute, hash))
        with urlopen(req) as res:
            buff = res.read()

        # 画像データ読み込み
        try:
            image = Image.open(io.BytesIO(buff))
        except IOError:
            image = None

        return image

    def get(self, request, idol_id: int, size: str=DEFAULT_IMAGE_SIZE):
        setting = IMAGE_SETTINGS[DEFAULT_IMAGE_SIZE]
        if size in IMAGE_SETTINGS:
            setting = IMAGE_SETTINGS[size]

        # アイドルデータ取得
        req = Request(IDOL_DATA_API_URL_FORMAT % (idol_id))
        with urlopen(req) as res:
            idol = json.load(res)
        if idol is None:
            return HttpResponseNotFound()

        # 画像データ読み込み
        image = self.get_image(setting['attribute'][idol['rarity']], idol['hash'])
        if image is None:
            image = Image.new("RGB", (setting['width'], setting['height']))

        # レスポンス出力
        response = HttpResponse(content_type='image/jpeg')
        response['Access-Control-Allow-Origin'] = '*'
        image.save(response, 'JPEG', optimize=True)
        return response
