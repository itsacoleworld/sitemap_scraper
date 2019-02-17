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
def get_soup(request):
    request = get_request(url, headers)
    if request:
        soup = BeautifulSoup(request.text, "html.parser")
    return soup


# gets request and flags unsuccesful requests
def get_request(url, headers):
    headers = {
        'user-agent': 'f{headers}'}
    try:
        request = requests.get(url, headers=headers, timeout=10)
        request_response = request.status_code
        return request
    except Exception as ex:
        print(str(ex))


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
