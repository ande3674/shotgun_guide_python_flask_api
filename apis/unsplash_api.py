import requests

KEY = 'ef253021d306d26257725b9b255a9e89e7bc781641d78af61609f3097c08526f'
SECRET_KEY = 'bc52f824e8ee27a56adfb9b3df8424620f24ace85cd9e4cd57fa9cfbfaf939c6'
URL = 'https://api.unsplash.com/search/photos?page=1&query={TAG}' \
      '&client_id=ef253021d306d26257725b9b255a9e89e7bc781641d78af61609f3097c08526f'

def search_by_tag_return_link(tag):
    tag = split_up(tag)
    url = URL.format(TAG=tag)
    response = requests.get(url).json()
    photos_array = response['results']
    photo_object = photos_array[0]
    url = photo_object['urls']['small']
    return url


def build_urls(photos):
    url_list = ['' for i in range(10)]

    for i in range(len(photos)):
        display_url = photos[i].url
        url_list[i] = display_url
    return url_list


def split_up(s):
    split = s.split(" ")
    return_string = ''
    for i in range(len(split)):
        if i == len(split)-1:
            return_string += split[i]
        else:
            return_string += (split[i] + '+')
    return return_string