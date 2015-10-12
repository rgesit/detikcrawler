import requests
from bs4 import BeautifulSoup


def web_crawler(url):
    global source
    try:
        source = requests.get(url)
    except NameError:
        print 'cannot resolve', url, "\n"

    return source


def image_detect(url):
    if url.startswith('http'):
        return url
    elif url.startswith('//'):
        return 'http:' + url
    elif url.startswith('images/'):
        return 'http://www.detik.com/' + url
    elif url.startswith('/images'):
        return 'http://www.detik.com' + url
    else:
        return url


def image_size(image_url):
    size = web_crawler(image_detect(image_url)).headers['Content-Length']
    return int(size)


def tag_op(tag, url):
    find = BeautifulSoup(web_crawler(url).content, "html.parser").find_all(tag)

    count_tag = len(find)
    i = 0
    image = 0
    for daftar in find:
        i += 1
        image += image_size(daftar.get('src'))
        print i, daftar.get('src'), image_size(daftar.get('src'))

    # total_size = (image)
    print "\nJumlah %s =" % tag, count_tag
    print "Total Ukuran All %s =" % tag, image

# tag_op("img", "http://localhost/slcs")
tag_op("img", "http://www.detik.com")
