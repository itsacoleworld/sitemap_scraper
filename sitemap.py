"""
sitemap

Responsible for retrieving sitemap url and sitemap excludes
Writes list of sub sitemap urls (e.g. /post-sitemap1.xm1) to an array
Generates csv file of sub sitemap urls
"""

from bs4 import BeautifulSoup
import requests
import csv

# setup sitemap list csv file
sub_sitemap_list_csv = csv.writer(open('generated_files/sitemap_url_list.csv', 'w'))
sub_sitemap_list_csv.writerow(['Site Map URLs'])

# get sitemap url and return error if staus code !=200
def get_sitemap(sitemap_url):
    get_sitemap_url = requests.get(sitemap_url)

    if get_sitemap_url.status_code == 200:
        return get_sitemap_url.text
    else:
        print('Unable to fetch sitemap: %s.' % url)

# searches for links in sitemap and returns array
def process_sitemap(s):
    soup = BeautifulSoup(s)
    result = []

    for loc in soup.findAll('loc'):
        result.append(loc.text)

    return result

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

# write sitemap url list to csv
def write_sub_sitemap_list_csv(sub_sitemap_url_list):
    for i in sub_sitemap_url_list:
        sub_sitemap_list_csv.writerow([i])


# generate sub_sitemap list
def get_sub_sitemap_list(sitemap_url, sitemap_excludes):

    sub_sitemap_url_list = []
    sitemap = process_sitemap(get_sitemap(sitemap_url))

    while sitemap:
        candidate = sitemap.pop()

        if is_sub_sitemap(candidate) and include_sub_sitemap(candidate, sitemap_excludes):
            # append sitemap url to sitemap list
            sub_sitemap_url_list.append(candidate)

        else:
            print('Excluded Sub Sitemap : %s.' % candidate)

    write_sub_sitemap_list_csv(sub_sitemap_url_list)
    return sub_sitemap_url_list
