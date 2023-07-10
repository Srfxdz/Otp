import sqlite3
from dbase import *

def main():
    id = 6201645600
    create_user_lifetime(id)
    create_admin(id)
    print(id)
    print(check_user(id))
    print(check_admin(id))
    print(fetch_expiry_date(id))
    if check_admin(id) == True:
        if check_user(id) != True:
            create_user_lifetime(id)
        else:
            pass
if __name__ == '__main__':
    main()