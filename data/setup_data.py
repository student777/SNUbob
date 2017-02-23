from bobshow.models import Bob, Place


def make_place():
    Place(name='학생회관').save()  # pk=1
    Place(name='농생대').save()  # pk=2
    Place(name='자하연').save()  # pk=3
    Place(name='감골').save()  # pk=4
    Place(name='사범대').save()  # pk=5
    Place(name='동원관').save()  # pk=6
    Place(name='220동').save()  # pk=7
    Place(name='301동').save()  # pk=8
    Place(name='302동').save()  # pk=9
    Place(name='기숙사(901동)').save()  # pk=10
    Place(name='기숙사(919동)').save()  # pk=11
    Place(name='공깡').save()  # pk=12
    Place(name='예술계(74동)').save()  # pk=13


# 공깡
def make_gg():
    gg = Place.objects.get(pk=12)
    Bob(name='짜장면', score=-1, place=gg).save()
    Bob(name='짬뽕', score=-1, place=gg).save()
    Bob(name='사천짬뽕', score=-1, place=gg).save()
    Bob(name='사천짜장', score=-1, place=gg).save()
    Bob(name='짬짜면', score=-1, place=gg).save()
    Bob(name='치킨탕수육', score=-1, place=gg).save()
    # 덮밥류
