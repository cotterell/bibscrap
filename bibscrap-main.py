import os
import argparse
import requests
from multiprocessing import Process


base_links = ['dl.acm.org', 'ieeexplore.ieee.org']
spiders = ['acmdl', 'ieee']

# ------ define and parse arguments
parser = argparse.ArgumentParser()

# params
parser.add_argument('--doi', type=str, default=None, required=True,
                    help="This is the DOI that bibscrap will look for")

parser.add_argument('--verbose', '--v', action='store_true', default=False,
                    help="Prints the verbose information from scrapy")



args = parser.parse_args()


# ------------------ start of main program
def main():
    global args

    print(args.doi)

    # try to handle the request
    request = requests.get(f'https://dx.doi.org/{args.doi}')
    print(f"request code: {request.status_code}")
    print(f"request url: {request.url}")

    r_code = request.status_code
    if r_code == 404:
        print("Error code 404!")
        return

    # handle request url
    for (base, spider) in zip(base_links, spiders):
        if base in request.url:
            print(f"This is a {base} link!")
            print(f"Corresponding spider: {spider}")

            # determine if verbose was used or not
            no_log = "--nolog" if not args.verbose else ""
            print(f"Corresponding command: $ scrapy crawl {no_log} -a doi={args.doi} {spider}")

            # execute scrapy
            print("Executing scrapy command!")
            os.system(f"scrapy crawl {no_log} -a doi={args.doi} {spider}")
            return


if __name__ == "__main__":
    main()
