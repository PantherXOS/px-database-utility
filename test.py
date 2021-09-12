import subprocess


def check_dependencies():
    try:
        subprocess.run(['pg_dump', '--version'])
        return True
    except Exception as err:
        print(err)
        return False


check_dependencies()
