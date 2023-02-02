import requests

BASE_URL = 'http://127.0.0.1:8000/api/'

get_admin_by_from_id = 'admin/'
add_admin = 'admin/add'
list_admins = 'admin/list'

add_user = 'user/add'
get_user_by_from_id = 'user/fromid/'
get_user_by_passport_number = 'user/passport/'
update_user = 'user/'


def get(pk: int = None, addr: str = None):
    res = requests.get(get_url(pk, addr))
    print(res)
    return result(res)


def post(addr: str, data: dict):
    res = requests.post(get_url(addr=addr), data)
    return result(res)


def put(pk: int, addr: str, data: dict):
    res = requests.put(get_url(pk, addr), data)
    return result(res)


def result(res):
    if res.ok:
        return res.json()
    print(res)
    return None


def get_url(pk: int = None, addr: str = None):
    url = BASE_URL + addr
    if pk is None:
        return url
    return url + str(pk)