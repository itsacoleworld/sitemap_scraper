"""
posts

Responsible for retrieving list of urls from sub sitemaps

"""

from bs4 import BeautifulSoup
import requests
import csv
import support

sitemap_post_list_csv = csv.writer(open('generated_files/sitemap_post_list.csv', 'w'))
sitemap_post_list_csv.writerow(['Sitemap URL', 'Post URL'])

post_list_csv = csv.writer(open('generated_files/post_list.csv', 'w'))
post_list_csv.writerow(['Post URL'])

# generate post list
def get_post_list(sub_sitemap_list):

    # create a blank post list array
    post_list = []

    # create a blank sitemap and post list array
    sitemap_post_list_body = []


    for sub_sitemap in  sub_sitemap_list:

        # gets sub sitemap soup
        sub_sitemap_soup = support.get_soup(sub_sitemap)

        # creates array of all links on sub sitemap page
        sub_sitemap_links = support.find_links(sub_sitemap_soup)

        # loops through sub sitemap if true and appends links to new array
        while sub_sitemap_links:

            # sets candidate to last array item
            candidate = sub_sitemap_links.pop()

            #TODO: logic for link filtering


            # create sitemap post row
            sitemap_post_list_row = [sub_sitemap, candidate]

            # append sitemap post row to body
            sitemap_post_list_body.append(sitemap_post_list_row)

            # append sitemap url and post url array
            post_list.append(candidate)

    # writes sub sitemap and post url to csv
    write_sitemap_post_list_csv(sitemap_post_list_body)

    # writes post list to csv
    write_post_list_csv(post_list)

    # returns sub sitemap list
    return post_list

# write sub sitemap and list to csv
def write_sitemap_post_list_csv(sitemap_post_list):
    for i in sitemap_post_list:
        sitemap_post_list_csv.writerow(i)


# write post list to csv
def write_post_list_csv(post_list):
    for i in post_list:
        post_list_csv.writerow([i])
