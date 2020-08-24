from Controller.Main import *

def show():

    return print('''
        ******  Options  ******
        1 - ADD New Route
        2 - Search Route
        0 - Exit
        **********************
        ''')

def createRoute(api):
    print('Input new route: Origin,Destiny,Amount')
    origin, destiny, amount = input().split(',')
    if api.dataFile.writeFile(origin, destiny, amount):
        print('New route successfully created')
    else:
        print('Error updating the file')



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
        option = int(input('Enter with option'))
        
        if(option == 1):
            createRoute(api)
        elif option == 2:
            print('under development')
        elif option == 0:
            print('Exit')
        else :
            print('Invalid')