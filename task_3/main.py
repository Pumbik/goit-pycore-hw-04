import sys
from pathlib import Path
from colorama import init, Fore, Style

# автоскидання кольорів
init(autoreset=True)

def display_directory_structure(path_to_scan: Path, indent: str = ""):
    try:
        # 1. Перебираємо всі елементи в 'path_to_scan'
        for item in path_to_scan.iterdir():
            
            # 2. Якщо елемент - це директорія 
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}")
                
                # Рекурсивно викликаємо цю ж функцію для вмісту цієї папки
                display_directory_structure(item, indent + "  ")
            
            # 3. Якщо елемент - це файл
            elif item.is_file():
                print(f"{indent}{Fore.GREEN}{item.name}")

    except PermissionError:
        print(f"{indent}{Fore.RED}Permission denied to access {path_to_scan.name}")


def main():
    try:
        # 1. Перевірка, чи достатньо аргументів 
        if len(sys.argv) != 2:
            print(Fore.YELLOW + "Usage: <directory_path>")
            sys.exit(1)

        # 2. Отримаемо шлях --> об'єкт Path
        directory_path = Path(sys.argv[1])

        # 3. Перевірка --> шлях існує 
        if not directory_path.exists():
            print(Fore.RED + "Error: Path does not exist.")
            sys.exit(1)

        # 4. Перевірка --> директорія 
        if not directory_path.is_dir():
            print(Fore.RED + "Error: Path is not a directory.")
            sys.exit(1)

        # 5. коренева папка
        print(f"\n{Fore.BLUE}{directory_path.name}") 
        
        # 6.запускаємо рекурсивну функцію
        display_directory_structure(directory_path, indent="  ")

    except Exception as e:
        print(Fore.RED + f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()