class Prediction:

    def __init__(self, filt):
        self.__filters = tuple(filt)
        self.__price = 0

    def street(self):
        return self.__filters[0]

    def room(self):
        return self.__filters[1]

    def distr(self):
        return self.__filters[2]

    def t_area(self):
        return self.__filters[3]

    def l_area(self):
        return self.__filters[4]

    def  residence(self):
        return self.__filters[5]

    def set_cost(self, cst):
        self.__price=cst

    def return_cost(self):
        return self.__price

