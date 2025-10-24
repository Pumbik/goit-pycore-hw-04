def get_cats_info(path):

    cats_info = []
    try:
        with open(path, 'r', encoding ='utf-8') as file:
            for line in file:
                # cleared_line = line.strip()
                # parts = cleared_line.split(',')
                parts = line.strip().split(',')

                if len(parts) == 3:
                    cat_dict = {
                        'id':   parts[0],
                        'name': parts[1],
                        'age':  parts[2]
                    }

                    cats_info.append(cat_dict)
                else:
                    print(f"Попередження: рядок '{line.strip()}' має неправильний формат і буде пропущений.")
    
    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")

    return cats_info
