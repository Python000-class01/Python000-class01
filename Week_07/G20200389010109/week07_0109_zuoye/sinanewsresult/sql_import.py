import csv

with open('/tmp/result.csv') as f:
    with open('result.sql','w',encoding='utf8') as g:    
        reader = csv.reader(f)
        for row in reader:
            g.write(f"INSERT INTO t1 (n_star, short, sentiment) values ({row[0]}, '{row[1]}', {row[2]});\n")

