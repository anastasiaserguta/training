TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"

class Dialog:

    def __new__(cls, *args, **kwargs):
        os_obj = super().__new__(DialogWindows) if TYPE_OS == 1 else super().__new__(DialogLinux)
        os_obj.name = args[0]
        return os_obj

obj = Dialog('hello')
print(obj.name, obj.name_class)