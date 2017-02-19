import os
import django
import minisnu
import datetime

django.setup()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snubob.settings')


def main():
    minisnu.update_menu()
    f = open("update_log", 'a')
    f.write(datetime.date.today().isoformat())
    f.write('\n')
    f.close()


if __name__ == '__main__':
    main()
