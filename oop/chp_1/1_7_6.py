class Viber:
    _messages = []

    @classmethod
    def add_message(cls, msg):
        cls._messages.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls._messages.remove(msg)

    @classmethod
    def set_like(cls, msg):
        msg_indx = cls._messages.index(msg)
        cls._messages[msg_indx].fl_like = True if cls._messages[msg_indx].fl_like == False else False

    @classmethod
    def show_last_message(cls, num):
        print(*[msg.text for msg in cls._messages[-1 * num:]], sep='\n')

    @classmethod
    def total_messages(cls):
        return len(cls._messages)

class Message:

    def __init__(self, text):
        self.text = text
        self.fl_like = False

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.show_last_message(3)
print(Viber.total_messages())
Viber.remove_message(msg)
print(Viber.total_messages())
