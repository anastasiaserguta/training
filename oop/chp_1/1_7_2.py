from string import ascii_lowercase, digits

class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])
    
class Input:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        flag = all([let in cls.CHARS_CORRECT for let in name])
        if type(name) != str or 3 > len(name) or len(name) > 50:
            raise ValueError('некорректное поле name')
        if not flag:
            raise ValueError('некорректное поле name')

    def __init__(self, name, size = 10):
        self.check_name(name)
        self.name = name 
        self.size = size



class TextInput(Input):

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput(Input):
    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"


login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()

try:
    a = TextInput('aa')
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"