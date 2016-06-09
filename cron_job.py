import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snubob.settings')
import django
django.setup()
import minisnu
import datetime

def main():
    minisnu.update_menu()
    f = open("update_log", 'a')
    f.write(datetime.date.today().isoformat())
    f.write('\n')
    f.close()


if __name__ == '__main__':
    main()
