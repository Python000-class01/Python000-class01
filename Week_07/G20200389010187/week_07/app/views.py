from . import admin

@admin.route('/')
def index():
     return '<h1> you are allowed to manage many stuff</h1>'