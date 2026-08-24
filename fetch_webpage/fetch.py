import urllib.request

# # Create an OpenerDirector with support for Basic HTTP Authentication...
# auth_handler = urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='PDQ Application',
#                           uri='https://mahler:8092/site-updates.py',
#                           user='klem',
#                           passwd='kadidd!ehopper')
# opener = urllib.request.build_opener(auth_handler)
# # ...and install it globally so it can be used with urlopen.
# urllib.request.install_opener(opener)

with urllib.request.urlopen('https://api.api-ninjas.com/v1/horoscope?zodiac=virgo') as page:
    print(page.headers.get('Content-Encoding'))
    data = page.read()
    if page.headers.get('Content-Encoding') == 'gzip':
        import gzip
        data = gzip.decompress(data)
    # print(data[:300].decode('utf-8', errors='replace'))
    print(data.decode('utf-8', errors='replace'))
