"""
Post Check

Check post for a specific keyword, list of words, and rates.
"""

from bs4 import BeautifulSoup
import requests
import csv
import sitemap
import posts
import support


# variables

## sitemap url
sitemap_url = 'https://lendedu.com/sitemap_index.xml'

## sitemap excludes
sitemap_excludes = ['author', 'lightbox', 'news']

## needs selenium
needs_selenium = False


def main():
    sub_sitemap_list = sitemap.get_sub_sitemap_list(sitemap_url, sitemap_excludes)
    post_list = posts.get_post_list(sub_sitemap_list)


if __name__ == '__main__':
    main()
