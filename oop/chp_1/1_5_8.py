import sys

class ListObject:

    def __init__(self, data, next_obj = None):
        self.next_obj = next_obj
        self.data = data

    def link(self, obj):
        self.next_obj = obj

lst_in = list(map(str.strip, sys.stdin.readlines()))
head_obj = ListObject(lst_in[0])
current = head_obj
for data in lst_in[1:]:
    obj = ListObject(data)
    current.link(obj)
    current = obj



    

