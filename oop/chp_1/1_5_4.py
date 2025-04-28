class Graph:

    def __init__(self, data: list, is_show: bool = True):
        self.data = data.copy()
        self.is_show = is_show

    def set_data(self, data):
        self.data = data.copy()

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print('Отображение данных закрыто')

    def show_graph(self):
        if self.is_show:
            print(f'Графическое отображение данных: {" ".join(list(map(str, self.data)))}')
        else:
            print('Отображение данных закрыто')

    def show_bar(self):
        if self.is_show:
            print(f'Столбчатая диаграмма: {" ".join(list(map(str, self.data)))}')
        else:
            print('Отображение данных закрыто')

    def set_show(self, fl_show: bool):
        self.is_show = fl_show

data_graph = list(map(int, input().split()))

gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()
