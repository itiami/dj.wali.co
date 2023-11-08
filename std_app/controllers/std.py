
class Student:

    def __init__(self, lst=[]):
        self.lst = lst

    def addtolist(self):
        self.lst = ["item_1", "item_2", "item_3", "item_4"]
        self.lst.append("item_5")
        return self.lst
