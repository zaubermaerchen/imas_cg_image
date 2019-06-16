# -*- coding: utf-8 -*-
import io
import json
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from django_redis import get_redis_connection
from image.settings import *
from PIL import Image

class View(View):
    def get_redis(self):
        con = None
        try:
            con = get_redis_connection('redis')
        finally:
            return con

    def get_image(self, idol_id: int, attribute: str, hash: str):
        key = IMAGE_REDIS_KEY_FORMAT % (attribute, idol_id)
        redis = self.get_redis()
        if redis is not None and redis.exists(key):
            # Redisから取得
            buff = redis.get(key)
        else:
            # リモートから取得
            url = IMAGE_URL_FORMAT % (attribute, hash)
            data = urlencode({'url': url})
            req = Request(MOBAGE_URL, data.encode('utf-8'))
            with urlopen(req) as res:
                buff = res.read()
                if redis is not None:
                    redis.set(key, buff)
                    redis.expire(key, 604800)
        
        # 画像データ読み込み
        try:
            image = Image.open(io.BytesIO(buff))
        except IOError:
            image = None
            if redis is not None and redis.exists(key):
                redis.delete(key)

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
        image = self.get_image(idol_id, setting['attribute'][idol['rarity']], idol['hash'])
        if image is None:
            image = Image.new("RGB", (setting['width'], setting['height']))

        # レスポンス出力
        response = HttpResponse(content_type='image/jpeg')
        response['Access-Control-Allow-Origin'] = '*'
        image.save(response, 'JPEG', optimize=True)
        return response