from Controllers.Main import *
from Models.SearchRoute import *

def show():

    return print('''
        ******  Options  ******
        1 - ADD New Route
        2 - Search Route
        0 - Exit
        **********************
        ''')

def createRoute():
    print('Input new route: Origin,Destiny,Amount')
    origin, destiny, amount = input().split(',')
    if api.dataFile.writeFile(origin, destiny, amount):
        print('New route successfully created')
    else:
        print('Error updating the file')

def searchRoute():

    print('Input Origin-Destiny: ')

    search = Search()
    better_route = search.better_price_travel(input(),dataRoutes= api.dataFile.dataInput)

    print(f'best route: {better_route[0]} > ${better_route[1]}')



if __name__ == '__main__':
    args = []

    for param in sys.argv:
        args.append(param)
        
    fileInput = args[1]

    api = Main(fileInput)
    api.openningFile()

    option = 3

    while option != 0:
        
        show()
        option = int(input('Enter with option: '))
        
        if(option == 1):
            createRoute()
        elif option == 2:
            searchRoute()
        elif option == 0:
            print('Exit')
        else :
            print('Invalid')