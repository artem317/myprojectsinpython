import os
import time
import sys
from colorama import init, Fore, Style

init()
PASSWORD = r"snos\\"  # Экранирование обратного слеша

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_red(text):
    print(Fore.RED + text + Style.RESET_ALL)

def print_3d_banner():
    banner = r"""

 ██████╗ ██████╗  █████╗ ███████╗███████╗███╗   ██╗
██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝████╗  ██║
██║   ██║██████╔╝███████║███████╗█████╗  ██╔██╗ ██║
██║   ██║██╔═══╝ ██╔══██║╚════██║██╔══╝  ██║╚██╗██║
╚██████╔╝██║     ██║  ██║███████║███████╗██║ ╚████║
 ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝
 _____    _   _    ___     _____    _____    _____  
/ ____|  | \ | |  / _ \   / ____|  | ____|  |  __ \  
| (___   |  \| | | | | | | (___   | |__    | |__) |  
\___ \   | . ` | | | | |  \___ \  |___ \   |  _  /  
____) |  | |\  | | |_| |  ____) |  ___) |  | | \ \  
|_____/   |_| \_|  \___/  |_____/  |____/   |_|  \_\  
    """
    print_red(banner)

def nuke_account(username, user_id, count):
    try:
        for i in range(1, count + 1):
            print_red(f"[{i}/{count}] Жалоба отправлена на @{username} (ID: {user_id})")
            time.sleep(0.7)
        print_red("\n[+] Все жалобы успешно отправлены!")
        time.sleep(2)
    except KeyboardInterrupt:
        print_red("\n[!] СНОС остановлен пользователем!")
        time.sleep(1)

def main():
    clear_screen()
    print_red("Добро пожаловать в OPASEN SNOSER")
    
    # Проверка пароля (с экранированием)
    input_password = input("Введите пароль: ").strip()
    if input_password != PASSWORD.replace(r'\\', '\\'):  # Корректное сравнение
        print_red(" Неверный пароль! Уничтожение через 3...")
        time.sleep(1)
        print_red("2...")
        time.sleep(1)
        print_red("1...")
        time.sleep(1)
        sys.exit()

    while True:
        clear_screen()
        print_3d_banner()
        print_red("\n╔════════════════════════════════╗")
        print_red(  "║ [1] СНОС АККАУНТА              ║")
        print_red(  "║ [2] ВЫХОД                      ║")
        print_red(  "╚════════════════════════════════╝")
        
        choice = input("\nВыбор: ").strip()
        
        if choice == "1":
            clear_screen()
            print_3d_banner()
            
            user = input("\nВведите юзернейм жертвы: ").strip()
            uid = input("Введите ID жертвы: ").strip()
            
            # Ввод количества жалоб
            while True:
                try:
                    count = int(input("Введите количество жалоб (1-100000): "))
                    if 1 <= count <= 100000:
                        break
                    print_red("Ошибка: введите число от 1 до 100000!")
                except ValueError:
                    print_red("Ошибка: введите корректное число!")
            
            print_red("\n[!] Активирован протокол 'КОСТОЧИСТКА'")
            nuke_account(user, uid, count)
            
        elif choice == "2":
            print_red("\n Завершение работы...")
            time.sleep(1)
            sys.exit()
            
        else:
            print_red("\n Некорректный ввод!")
            time.sleep(1)

if __name__ == "__main__":
    main()
