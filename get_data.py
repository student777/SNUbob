import os
import sys
import django


if __name__ == '__main__':
    # setup django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'snubob.settings')
    django.setup()

    from data import crawl_data  # should be placed after django.setup()

    # cron_job: get week menu from today
    if len(sys.argv) == 1:
        print('today/day/week/year is required')

    elif sys.argv[1] == 'today':
        crawl_data.get_menu_today()

    elif sys.argv[1] == 'week':
        crawl_data.update_week_menu()

    elif sys.argv[1] == 'year':
        try:
            year = int(sys.argv[2])
        except IndexError:
            print('year required')
            exit()
        crawl_data.get_menu_year(year)

    elif sys.argv[1] == 'day':
        try:
            year, month, date = list(map(int, sys.argv[2:]))
        except IndexError:
            print('year, month, day required')
            exit()
        crawl_data.get_menu(year, month, date)

    elif sys.argv[1] == 'initialize':
        from data.setup_data import make_place
        make_place()

    else:
        print('week or year or day is required')
