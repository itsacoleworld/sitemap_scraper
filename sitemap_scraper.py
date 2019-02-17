from bs4 import BeautifulSoup
import requests
import csv

# setup sitemap csv
sitemap_csv = csv.writer(open('sitemap_url_list', 'w'))
sitemap_csv.writerow(['Site Map URLs'])

# variables

## needs selenium
needs_selenium = true

## site url
sitemap_url = 'https://lendedu.com/sitemap_index.xml'

# gets sitemap url and returns error is staus code !=200
def get_sitemap(url):
    get_url = requests.get(url)

    if get_url.status_code == 200:
        return get_url.text
    else:
        print 'Unable to fetch sitemap: %s.' % url

# finds all links in sitemap and appends them to an array
def process_sitemap(s):
    soup = BeautifulSoup(s)
    result = []

    for loc in soup.findAll('loc'):
        result.append(loc.text)

    return result

# checks to see if file is a sub sitemap
def is_sub_sitemap(s):
    if s.endswith('.xml') and 'sitemap' in s:
        return True
    else:
        return False

#
def parse_sitemap(s):
    sitemap = process_sitemap(s)
    result = []

    while sitemap:
        candidate = sitemap.pop()

        if is_sub_sitemap(candidate):
            sub_sitemap = get_sitemap(candidate)
            for i in process_sitemap(sub_sitemap):
                sitemap.append(i)
                sitemap_csv([sitemap[i]])
        else:
            result.append(candidate)

    return result

def main():
    sitemap = get_sitemap('sitemap_url')
    print '\n'.join(parse_sitemap(sitemap))


if __name__ == '__main__':
    main()
