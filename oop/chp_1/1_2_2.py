class TravelBlog:
    total_blogs = 0

tb1 = TravelBlog()
tb1.name, tb1.days = 'Франция', 6

TravelBlog.total_blogs += 1

tb2 = TravelBlog()
tb2.name, tb2.days = 'Италия', 5

TravelBlog.total_blogs += 1


class Figure:
    type_fig = 'ellipse'
    color = 'red'

fig1 = Figure()

fig1.start_pt, fig1.end_pt, fig1.color = (10, 5), (100, 20), 'blue'

del fig1.color

print(*fig1.__dict__.keys())

class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

p1 = Person()

print('job' in p1.__dict__.keys())