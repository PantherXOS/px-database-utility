import os
import subprocess

from .config import DEFAULT_DATABASE_DUMP_PATH


def check_dependencies():
    try:
        subprocess.run(['pg_dump', '--version'])
        return True
    except:
        print('pg_dump is not installed.')
        return False


def database_backup_destination_exists() -> bool:
    return os.path.isdir(DEFAULT_DATABASE_DUMP_PATH)


def list_files(path=DEFAULT_DATABASE_DUMP_PATH) -> 'list[str]':
    '''Get a list of files'''
    if database_backup_destination_exists():
        filenames = [
            f for f in os.listdir(
                path
            ) if os.path.isfile(os.path.join(path, f))
        ]
        return filenames

    else:
        print('The database has not been backed-up yet.')
        return []


def remove_old_backups(database: str, number_of_backups_to_keep: int):
    list_of_files = list_files()
    if len(list_of_files) > 0:
        list_of_database_dumps = []
        for filename in list_of_files:
            split_file_extention = filename.split('.')
            split_filename = split_file_extention[0].split('_', 1)
            backup_time = round(int(split_filename[0]))
            database_name = split_filename[1]

            path = '{}/{}'.format(DEFAULT_DATABASE_DUMP_PATH, filename)

            if database_name == database:
                list_of_database_dumps.append({
                    'path': path,
                    'time': backup_time
                })

        if len(list_of_database_dumps) > number_of_backups_to_keep:
            print('Found {} older backups for database {}.'.format(
                len(list_of_database_dumps), database)
            )
            items_to_remove = len(list_of_database_dumps) - \
                number_of_backups_to_keep
            sorted_list = sorted(
                list_of_database_dumps, key=lambda i: i['time']
            )
            index = 0
            for _ in range(items_to_remove):
                item = sorted_list[index]
                print('Deleting {}'.format(item['path']))
                os.remove(item['path'])
                index += 1
