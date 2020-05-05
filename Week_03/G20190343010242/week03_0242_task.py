from task2.scanner import Scanner
import argparse

###
# To run task1, in command line, run
# cd task1/web_crawler
# scrapy crawl rrys
###

# This is for task2
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='scanner')
    try:
        parser.add_argument('-n', '--num_threads', dest='threads', type=int,
                            help='max number of threads for scanning')
        parser.add_argument('-m', '--mode', dest='mode', type=str,
                            help='ping for ip addresses scanning, tcp for ports scanning')
        parser.add_argument('-t', '--targets', dest='targets', type=str,
                            help='ip or port range to scan. e.g 192.168.1.1-192.168.1.50; 192.168.1.5:1024-10000')
        parser.add_argument('-o', '--output', dest='output', type=str,
                            help='output file, support json file only')
        arguments = parser.parse_args()
        threads = arguments.threads
        mode = arguments.mode
        targets = arguments.targets
        output = arguments.output
        scanner = Scanner(threads, mode, targets, output)
        scan = getattr(scanner, mode)
        scan()
    except Exception:
        parser.print_help()

