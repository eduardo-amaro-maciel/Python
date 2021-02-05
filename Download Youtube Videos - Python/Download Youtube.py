# Download Youtube videos with python

import webbrowser

# ENTER URL HERE
url = 'https://www.youtube.com/watch?v=7m5TKzP2Y8s'

dowload = url[:12] + 'ss' + url[12:]
webbrowser.open(url)
# print(dowload)
