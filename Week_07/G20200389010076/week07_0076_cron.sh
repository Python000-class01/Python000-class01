#! /bin/bash
export PATH=$PATH:/bin
echo -n "开始爬虫"
source /root/www/venv/bin/activate
cd /root/www/tencentscrapy && scrapy crawl tencentspider