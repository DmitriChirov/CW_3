import os
from utils import get_data, select_data, sort_data, format_data

PATH_TO_OPERATIONS = "operations.json"


def main():
    if not os.path.exists(PATH_TO_OPERATIONS):
        print('''The file with the list of operations was not found. 
Check the availability and format of the file. 
It should be called "operations.json"''')
        exit()

    data = get_data(PATH_TO_OPERATIONS)
    data = select_data(data)
    data = sort_data(data)
    data = format_data(data)
    print(*data)


if __name__ == "__main__":
    main()