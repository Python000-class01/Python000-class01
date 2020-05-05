
class Observer:
    def __init__(self):
        self._number = None
        self._depart = []

    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, value):
        self._number = value
        print('当前客户数：{}'.format(self._number))
        for obj in self._depart:
            obj.change(value)
        print('-------')

    def notice(self, depart):
        self._depart.append(depart)

    def delete(self,depart):
        try:
            self._depart.remove(depart)
        except ValueError:
            pass
    
    
class Hr:
    def change(self, value):
        if value < 10:
            print("人事变动：裁员")
        elif value > 20:
            print("人事变动：扩员")
        else:
            print("人事无变化")

class Factory:
    def change(self, value):
        if value < 10:
            print('生产计划变动：减产')
        elif value > 20:
            print('生产计划变动：增产')
        else:
            print("生产计划不变")

if __name__ == '__main__':
    observer = Observer()
    hr = Hr()
    factory = Factory()

    observer.notice(hr)
    observer.notice(factory)

    observer.number = 8
    observer.number = 15
    observer.number = 30

    observer.delete(hr)
    observer.number = 5