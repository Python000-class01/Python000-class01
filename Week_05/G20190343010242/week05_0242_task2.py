from task2.douban_book_comments import DoubanBookComments
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='week05 - task2')
    try:
        parser.add_argument('-s', '--store', dest='store', type=bool,
                            help='flag if needs to store the data to database.')
        arguments = parser.parse_args()
        doubanComment = DoubanBookComments()
        doubanComment.sentiment()
        if arguments.store:
            doubanComment.store()
    except:
        parser.print_help()
