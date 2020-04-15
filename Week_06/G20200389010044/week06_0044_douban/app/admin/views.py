from . import admin

@admin.route('/')
def index():
        return '<h1> page admin </h1>'