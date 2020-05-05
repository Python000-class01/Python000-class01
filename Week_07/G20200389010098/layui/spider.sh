#!/bin/sh
cd /home/wwwroot/python/flask/layui/spider/$1
scrapy crawl $2 -a url_id=$3 --nolog