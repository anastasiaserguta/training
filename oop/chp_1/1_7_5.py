class AppStore:

    _apps = []

    def add_application(self, app):
        self._apps.append(app)

    def remove_application(self, app):
        self._apps.remove(app)

    def block_application(self, app):
        indx = self._apps.index(app)
        self._apps[indx].blocked = True

    def total_apps(self):
        return len(self._apps)
    
class Application:

    def __init__(self, name):
        self.name = name
        self.blocked = False

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
print(store.total_apps(), app_youtube.blocked)
store.block_application(app_youtube)
print(store.total_apps(), app_youtube.blocked)
store.remove_application(app_youtube)
print(store.total_apps())
