# imas_cg_image

カードのIDから画像を取得

## 必要ミドルウェア・ライブラリ

* Python >= 3.7

## 必要Pythonライブラリ

* Django >= 2.2.2
* django-cors-headers >= 3.0.2
* django-redis >= 4.10.0
* Pillow >= 6.0.0

## ローカル環境での起動手順

1. docker-compose up
1. 「http://localhost:8000/l/1000101」にアクセスして画像が表示できるか確認する
