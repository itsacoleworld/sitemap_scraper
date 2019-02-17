"""
Support

Support modules for requests, BeautifulSoup, and csv

"""

from bs4 import BeautifulSoup
import requests
import csv


# find links on page
def find_links(soup_text):
    links = []
    for loc in soup_text.findAll('loc'):
        links.append(loc.text)
    return links

# get soup text of url
def get_soup(url):
    request = get_request(url)
    if request:
        soup = BeautifulSoup(request.text, "html.parser")
    return soup


# gets request and flags unsuccesful requests
def get_request(url):
    request = requests.get(url)
    if check_request_status(request) == 200:
        return request
    else:
        print(f'Could not access {url}: {request}')

# check status code and return error
def check_request_status(url):
    status = url.status_code
    return status

# replace: write_sub_sitemap_list_csv
def generate_csv(csv_name, csv_path, header_array, body_array):
    csv_file = create_csv(csv_name, csv_path)
    for header in header_array:
        csv_file.writerows([header])

    for body in body_array:
        csv_file.writerows([body])


def create_csv_file(csv_name, csv_path):
    csv_full_path = f'{csv_path}/{csv_name}.csv'
    return csv.writer(open(csv_full_path, 'w'))
