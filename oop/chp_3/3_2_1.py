from random import shuffle, randint

class RandomPassword:

    def __init__(self, psw_chars, min_lenght, max_lenght):
        self.psw_chars = psw_chars
        self.min_lenght = min_lenght
        self.max_lenght = max_lenght

    def __call__(self, *args, **kwargs) -> str:
        chars = (list(self.psw_chars))
        shuffle(chars)
        lenght = randint(self.min_lenght, self.max_lenght)
        return ''.join(chars[:lenght])
    
min_length = 5
max_length = 20
psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"

rnd = RandomPassword(psw_chars, min_length, max_length)

lst_pass = [rnd() for _ in range(3)]
print(lst_pass)