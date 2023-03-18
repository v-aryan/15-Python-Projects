# import urllib
# use urllib.request to get the data from the url
# write a function that takes url
# and returns a response

import urllib.request as urllib

def main(url):
    print("Checking Connectivity")

    response = urllib.urlopen(url)
    print("connected to", url, "successfully")
    print("The response code was:", response.getcode())


print("This is a site connectivity checker program")
input_url = input("Input the url of the site")
main(input_url)
