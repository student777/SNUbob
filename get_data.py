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
        crawl_data.update_week_menu()

    # TODO: Make interpreter: get year menu, today menu..
