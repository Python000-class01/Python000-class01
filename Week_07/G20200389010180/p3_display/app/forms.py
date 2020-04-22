from wtforms import Form, StringField, SelectField

class CommentSearchForm(Form):
    search = StringField('')