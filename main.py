from data_preparation import load_data
from menu import menu


def main(*args, **kwargs):
    data = load_data()
    
    while(True):
        menu(data)


main()
