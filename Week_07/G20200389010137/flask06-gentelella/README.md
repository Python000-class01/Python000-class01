# README

1. 爬取数据

    cd /Volumes/S1-Document/Flask-Train/News && scrapy crawl weitoutiao

    保存到 sqlite，解决唯一性约束，利用唯一性约束解决重复数据

2. 语意分析

   cd /Volumes/S1-Document/Flask-Train/flask06-gentelella

   python ds.py

   pandas 从 sqlite 中读取数据，使用 sqlachemy

   语意分析完，pandas 再存入另一张表，由 content_id 进行关联

3. 数据展示
