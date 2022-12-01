from sys import argv
from urllib.request import urlopen
from urllib.error import *

try:
    user_link = argv[1]
    link = urlopen(user_link)

except IndexError as i:
    print("No url Provided and", i)

except HTTPError as h:
    print("HTTP error", h)

except URLError as u:
    print("Opps ! Page not found!", u)

else:
    print("Yeah ! Page found")