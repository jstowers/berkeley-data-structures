class Box:
    def __init__(self):
        self.i_lo = None
        self.i_hi = None
        self.j_lo = None
        self.j_hi = None
        self.ht = self.__create_ht()

    def __create_ht(self):
        return 
    
    # Get_box_value receives a Cell i and j values 
    # and returns the Box value
    def box_value(self, cell):
        i = cell.i
        j = cell.j

        return self.ht[i][j]


# TODO
    
