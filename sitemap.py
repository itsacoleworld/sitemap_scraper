"""
sitemap

Responsible for retrieving sitemap url and sitemap excludes
Writes list of sub sitemap urls (e.g. /post-sitemap1.xm1) to an array
Generates csv file of sub sitemap urls
"""

from bs4 import BeautifulSoup
import requests
import csv

import support

# set headers in get_request
headers = {''}


# setup sitemap list csv file
sub_sitemap_list_csv = csv.writer(open('generated_files/sub_sitemap_list.csv', 'w'))
sub_sitemap_list_csv.writerow(['Site Map URLs'])

# generate sub sitemap list
def get_sub_sitemap_list(sitemap_url, sitemap_excludes):

    # create a blank sitemap list array
    sub_sitemap_list = []

    # gets request for sitemap
    request = support.get_request(sitemap_url, headers)

    # creates post soup
    sitemap_soup = BeautifulSoup(request.text, "html.parser")

    # creates array of all links on sub sitemap page
    sitemap_links = support.find_links(sitemap_soup)

    # processing
    print('Processing Sitemap')

    # loops through sub sitemap if true and appends links to new array
    for sub_sitemap in sitemap_links:

        # sets candidate to last array item
        candidate = sub_sitemap

        # verifies url is a sitemap and is not excluded
        if is_sub_sitemap(candidate) and include_sub_sitemap(candidate, sitemap_excludes):

            # append sitemap url to sub sitemap list
            sub_sitemap_list.append(candidate)

        else:
            print(f'Excluded Sub Sitemap: {candidate}')

    # writes complete sub sitemap list to csv
    write_sub_sitemap_list_csv(sub_sitemap_list)

    # returns sub sitemap list
    return sub_sitemap_list

# check to see if url is a sub sitemap
def is_sub_sitemap(s):
    if s.endswith('.xml') and 'sitemap' in s:
        return True
    else:
        return False

# checks to see if sitemap has been excluded
def include_sub_sitemap(s, sitemap_excludes):
    if any(x in s for x in sitemap_excludes):
        return False
    else:
        return True

# write sub sitemap url list to csv
def write_sub_sitemap_list_csv(sub_sitemap_list):
    for i in sub_sitemap_list:
        sub_sitemap_list_csv.writerow([i])
