import csv

with open('../commentsData.csv') as f:
    with open('result.sql','w',encoding='utf8') as g:    
        reader = csv.reader(f)
        for row in reader:
            g.write(f"INSERT INTO comments (uid, nick, area, pub_time, content, crawl_time, sentiment) values ({row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}});\n")

