import urclib.request
from bs4 import BeautifulSoup
import datetime
from bobshow.models import Bob, Place, Date


def get_menu(year, month, day):
    dt = datetime.date(year, month, day)
    add_menu(dt)


def update_week_menu():
    dt = datetime.date.today()
    td = datetime.timedelta(days=1)
    for i in range(0, 7):
        add_menu(dt + i * td)


def get_menu_today():
    dt = datetime.date.today()
    add_menu(dt)


def get_menu_year(year):
    dt = datetime.date(year, 1, 1)
    td = datetime.timedelta(days=1)
    for i in range(0, 365):
        add_menu(dt + i * td)


def add_menu(date):
    try:
        f = urllib.request.urlopen("http://mini.snu.kr/cafe/set/" + date.isoformat())
    except ConnectionResetError as e:
        raise e
    data = f.read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    a = soup.select("#main")[0].table.select(".bg_menu2")
    b = soup.select("#main")[0].table.select(".menu")
    parse_and_save_menu(a, b)


def parse_and_save_menu(a, b):
    length = len(a)
    for i in range(0, length):
        place = a[i].text
        bobs = b[i].contents
        if len(bobs) == 1:
            continue
        if place.startswith('두레') or place.startswith('공깡') or place.startswith('상아') or place.startswith('예술'):
            continue
        j = 1
        while j <= len(bobs):
            if bobs[j - 1].contents[0] == '??':
                break
            name = bobs[j].replace("(*)", "")
            name = name.replace(" ", '')
            name = name.replace("\n", '')
            if name.startswith('돈까스3종') or name.startswith('돈까스3종') or name.startswith('돈까스3종'):
                break
            if place.startswith('서당'):
                if j > 7:
                    break
                name = name.replace("2층스낵:", "")
                name = name.replace("2층스넥:", "")
                name = name.replace("뚝)", "")
            elif place.startswith('301'):
                if j > 4:
                    break
            elif place.startswith('감골') and name.startswith('채식'):
                break
            add_or_pass(place, name)
            j += 3


def add_or_pass(place, name):
    place_assigned = assign_place(place)
    if place_assigned is None:
        return

    bob = Bob.objects.get_or_create(place=place_assigned, name=name)[0s]    today = datetime.date.today()
    date = Date.objects.get_or_create(time=today)[0]
    bob.date.add(date)
    bob.save()


def assign_place(place):
    if place.startswith('학생회관'):
        return Place.objects.get(id=1)
    elif place.startswith('전망대'):
        return Place.objects.get(id=2)
    elif place.startswith('자하연'):
        return Place.objects.get(id=3)
    elif place.startswith('감골'):
        return Place.objects.get(id=4)
    elif place.startswith('서당골'):
        return Place.objects.get(id=5)
    elif place.startswith('동원관'):
        return Place.objects.get(id=6)
    elif place.startswith('220동'):
        return Place.objects.get(id=7)
    elif place.startswith('301'):
        return Place.objects.get(id=8)
    elif place.startswith('302'):
        return Place.objects.get(id=9)
    elif place.find('901') != -1:
        return Place.objects.get(id=10)
    elif place.find('919') != -1:
        return Place.objects.get(id=11)
    else:
        return None
