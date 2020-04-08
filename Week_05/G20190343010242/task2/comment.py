class Comment:

    __slots__ = ['__title', '__content', '__score']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, "_Comment__" + key, value)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        self.__score = score

    def to_dict(self):
        return dict(
            title = self.__title,
            content = self.__content,
            score = self.__score
        )
