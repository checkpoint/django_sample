# 概要

このソースコードは、[みんなのPython勉強会#7](http://startpython.connpass.com/event/22661/)で発表した<br>
[「PythonによるWebアプリケーション入門 〜Django編〜」](http://www.slideshare.net/checkpoint77/pythonweb-django)の書籍管理アプリケーションのサンプルソースです。


## インストール

```
pip install -r requirements.txt
```

## 起動

```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 確認

### Django管理画面

* http://localhost:8000/admin/

### サンプルアプリケーション画面

管理画面にてBlogを作成後

* http://localhost:8000/blog/#blog_id#
