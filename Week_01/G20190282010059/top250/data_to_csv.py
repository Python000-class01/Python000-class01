import csv

def data_to_csv(movies):
    print(movies)
    with open('movie_data.csv', 'w', encoding='utf_8_sig', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, ['title', 'rating', 'comment_count', 'comment_top5'])
        csv_writer.writeheader()
        csv_writer.writerows(movies)
