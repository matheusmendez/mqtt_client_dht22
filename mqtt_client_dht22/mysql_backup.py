import os
import ftplib
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

password = os.getenv('_PASSWORD_MYSQL')
user = os.getenv('_USER_MYSQL')
backup_dir = os.getenv('_BACKUP_DIR')
backup_name = (
    os.getenv('_BACKUP_NAME')
    + datetime.now().strftime('%Y%m%d%H%M%S')
    + '.sql'
)
backup_path = os.path.join(backup_dir, backup_name)
command = f'mysqldump -u{user} -p{password} --all-databases > {backup_path}'


def backup():
    file_path = os.path.join(backup_dir, '.last_backup.txt')
    os.system(command)
    print('Backup concluido')
    print(f'file:{backup_name}')

    with open(file_path, 'w') as f:
        f.write(datetime.now().strftime('%Y%m%d%H%M%S'))


def remove_file(file):
    try:
        os.remove(file)
        print(f'sucess:{file}')
    except OSError as error:
        print(error)
        print(f'fail:{file}')


def check_old_file(file, days=90):
    c_datetime = datetime.fromtimestamp(os.path.getctime(file))
    if (datetime.now() - c_datetime).days >= days:
        return True
    return False


def clean_old_backups():
    for root, dirs, files in os.walk(backup_dir, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            if check_old_file(file_path, 0):
                remove_file(file_path)


def check_last_backup():
    file_path = os.path.join(backup_dir, '.last_backup.txt')
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            try:
                last_backup = datetime.strptime(f.read(), '%Y%m%d%H%M%S')
                dif = (datetime.now() - last_backup).days
                if dif >= 7:
                    run()
                else:
                    # print(f'Faltam {7-dif} dias para o proximo backup')
                    pass
            except:
                run()
    else:
        run()


def run():
    clean_old_backups()
    backup()


if __name__ == '__main__':
    check_last_backup()
