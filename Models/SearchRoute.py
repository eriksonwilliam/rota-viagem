import sys
from Controllers.Main import *

class Search():

    def better_price_travel(self, route:str, dataRoutes):
        
        arr_copy = dataRoutes
        
        route_arr = route.split('-')
        start = route_arr[0]
        finish = route_arr[1]

        routes = []

        start_arr = [s for s in dataRoutes if s[0] == start]

        for finish_item in arr_copy:
            if finish_item[0] == start and finish_item[1] == finish:
                routes.append([f'{finish_item[0]}-{finish_item[1]}', finish_item[2]])
                start_arr.remove(finish_item)
                arr_copy.remove(finish_item)
        
        for i_start in start_arr:
            arr_copy.remove(i_start)
            
        for start in start_arr:
            s_arr = []
            r = f'{start[0]}'
            price = int(start[2])
            o_item = start[1]
            x = 0
            while x < len(arr_copy):
                if arr_copy[x][0] == o_item:
                    r = r + f'-{o_item}'
                    price += int(arr_copy[x][2])
                    if arr_copy[x][1] == finish:
                        r = r + f'-{arr_copy[x][1]}'
                        s_arr.append(r)
                        s_arr.append(price)
                        break
                    else:
                        o_item = arr_copy[x][1]
                        x = -1
                x += 1
            if len(s_arr) != 0:
                routes.append(s_arr)
        
        better_value = sys.maxsize
        better_route = None

        if(len(routes) != 0):
            for r in routes:
                if int(r[1]) < better_value:
                    better_value = int(r[1])
                    better_route = r
                    
        return better_route