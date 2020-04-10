from task1.douban_book_reviews import DoubanBookReviews
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='week05 - task1')
    try:
        parser.add_argument('-o', '--output', dest='fileName', type=str,
                            help='the image file you want to output for the wordcloud.')
        arguments = parser.parse_args()
        doubanReview = DoubanBookReviews()
        doubanReview.generate_word_cloud(fileName=arguments.fileName)
    except:
        parser.print_help()