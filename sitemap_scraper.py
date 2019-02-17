from bs4 import BeautifulSoup
import requests
import csv
import sitemap


# setup extracted urls csv
post_list_csv = csv.writer(open('generated_files/post_url_list.csv', 'w'))
post_list_csv.writerow(['Site Map URL', 'Post URL'])

# variables

## sitemap url
sitemap_url = 'https://lendedu.com/sitemap_index.xml'

## sitemap excludes
sitemap_excludes = ['author', 'lightbox']

## needs selenium
needs_selenium = False


def parse_sitemap(s, sitemap_excludes):
    sitemap_list = get_sub_sitemap_list(s, sitemap_excludes)


def main():
    sub_sitemap_url_list = sitemap.get_sub_sitemap_list(sitemap_url, sitemap_excludes)

if __name__ == '__main__':
    main()
