from packages.menu import show_menu
from packages.interface import register, delete_user, get_list_of_users, login, delete_database


def main() -> None:
    
    MENU = {
    1 : register,
    2 : delete_user,
    3 : get_list_of_users,
    4 : login,
    5 : delete_database
}
    show_menu(menu_options=MENU)

if __name__ == '__main__':
    main()