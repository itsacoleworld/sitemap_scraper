"""
posts

Responsible for retrieving list of urls from sub sitemaps
Responsible for methods used to extract info from post list

"""

from bs4 import BeautifulSoup
import requests
import csv
import support

# set headers in get_request
headers = {''}

sitemap_post_list_csv = csv.writer(open('generated_files/sitemap_post_list.csv', 'w'))
sitemap_post_list_csv.writerow(['Sitemap URL', 'Post URL'])

# generate post list
def get_post_list(sub_sitemap_list):

    # create a blank post list array
    post_list = []

    # create a blank sitemap and post list array
    sitemap_post_list_body = []


    for sub_sitemap in sub_sitemap_list:

        print(f'Processing Sitemap: {sub_sitemap}')

        # gets request for sub_sitemap url
        request = support.get_request(sub_sitemap, headers)
        # creates sub_sitemap_soup
        sub_sitemap_soup = BeautifulSoup(request.text, "html.parser")

        # creates array of all links on sub sitemap page
        sub_sitemap_links = support.find_links(sub_sitemap_soup)

        # loops through sub sitemap if true and appends links to new array
        for post in sub_sitemap_links:

            # creates new candidate from sub_sitemap
            candidate = post

            # create sitemap post row
            sitemap_post_list_row = [sub_sitemap, candidate]

            # append sitemap post row to body
            sitemap_post_list_body.append(sitemap_post_list_row)

            # append sitemap url and post url array
            post_list.append(candidate)

    # writes sub sitemap and post url to csv
    write_sitemap_post_list_csv(sitemap_post_list_body)

    # returns sub sitemap list
    return post_list

# write sub sitemap and list to csv
def write_sitemap_post_list_csv(sitemap_post_list):
    for i in sitemap_post_list:
        sitemap_post_list_csv.writerow(i)


post_list_info_csv = csv.writer(open('generated_files/post_list_info.csv', 'w'))
post_list_info_csv.writerow(['Post URL', 'Post Title', 'Thrive Editor'])

# get post info
def get_post_info(post_list):

    post_info = []

    post_info_body = []


    for post in post_list:

        print(f'Processing Post: {post}')

        # gets request for post url
        request = support.get_request(post, headers)

        # creates post soup
        post_soup = BeautifulSoup(request.text, "html.parser")

        # search post soup for post title
        post_title = get_post_title(post_soup)

        # returns true or false if post uses thrive editor
        is_thrive = is_thrive_editor(post_soup)

        # creates new row with post info
        post_info_row = [post, post_title, is_thrive]

        # appends post info row to body
        post_info_body.append(post_info_row)


        #internal_links = get_post_links(post_soup, post)

    # writes sub sitemap and post url to csv
    write_post_list_info_csv(post_info_body)

    return post_info_body


post_list_internal_links_csv = csv.writer(open('generated_files/post_list_internal_links.csv', 'w'))
post_list_internal_links_csv.writerow(['Post URL', 'Internal Link', 'Link Anchor',])

def get_post_links(soup_text, post):

    # create empty array for internal links
    post_internal_links = []

    # get post body
    post_body = soup_text.find("div", {"class": "stm_post_unit"})

    # look for internal links in post body
    post_links = post_body.find_all("a", href=lambda href: href and "//lendedu.com" in href)

    # create a row containing post, internal link, and internal link anchor
    for post_link in post_links:
        try:
            internal_link_href = post_link['href']
            internal_link_anchor = post_link.text
            #internal_link_rel = post_link['rel'] if post_link['rel'] else 'None'
            post_internal_links_row = [post, internal_link_href, internal_link_anchor]
            post_internal_links.append(post_internal_links_row)
        except KeyError:
            pass

    # writes sub sitemap and post url to csv
    write_post_internal_links_csv(post_internal_links)

    return post_internal_links

# get post title
def get_post_title(soup_text):
    post_title = soup_text.title.string
    return post_title

# check to see if post contains thrive editor
def is_thrive_editor(soup_text):
    if (soup_text.find("div", {"id": "tve_flt"})):
        return True
    else:
        return False


# write post list to csv
def write_post_list_info_csv(post_info):
    for i in post_info:
        post_list_info_csv.writerow(i)


# write post internal links to csv
def write_post_internal_links_csv(post_internal_links):
    for i in post_internal_links:
        post_list_internal_links_csv.writerow(i)
