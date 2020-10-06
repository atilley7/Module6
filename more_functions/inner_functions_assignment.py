def measurements(list):
    def area(a_list):
        if len(a_list) == 2:
            return a_list[0] * a_list[1]
        else:
            return a_list[0] * a_list[0]

    def perimeter(a_list):
        if len(a_list) == 2:
            return a_list[0] * 2 + a_list[1] * 2
        else:
            return a_list[0]*4

    return 'Perimeter = ' + str(perimeter(list)) + ' Area = ' + str(area(list))
