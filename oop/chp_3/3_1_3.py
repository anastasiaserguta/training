class Course:
    
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        del self.modules[indx]

class Module:

    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        del self.lessons[indx]

class LessonItem:

    title: str
    practices: int
    duration: int

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, name, value):
        if not isinstance(value, self.__annotations__[name]):
            raise TypeError('Неверный тип присваиваемых данных.')
        elif name in ('practices', 'duration') and value < 0:
            raise TypeError('Неверный тип присваиваемых данных.')

        object.__setattr__(self, name, value)

    def __getattr__(self, name):
        return False
    
    def __delattr__(self, name):
        if name in self.__annotations__.keys():
            raise AttributeError()
        
        super.__delattr__(name)
        

course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)

