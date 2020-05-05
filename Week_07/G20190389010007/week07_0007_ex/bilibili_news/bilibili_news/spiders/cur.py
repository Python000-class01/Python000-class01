from pprint import pprint
import datetime
import time
dict_a = {"name": "1", "students": [{
    "name": "2", "students": [{"name": "3", "students":
                               [{"name": "4", "students": "null"}]}]
}]}


class Person(object):
    def __init__(self, name):
        self.name = name


def get_person(dict1):
    p = Person(dict1['name'])
    return p


abc = {"abc": 123, "bcs": 345}
# pprint.pprint(get_person(dict_a))
person_list = []


def getlist(dict_a):
    pp = get_person(dict_a)
    person_list.append(pp)
    if dict_a['students'] == 'null':
        return person_list
    else:
        for i in dict_a['students']:
            getlist(i)


    # return person_list
if __name__ == '__main__':
    
    the_date = datetime.datetime.now() #指定当前日期 2018-11-10
    date_now = time.ctime()
    # the_date_now= datetime.datetime()
    pre_date = the_date - datetime.timedelta(hours=24)
    # pre_date = pre_date.strftime('%Y-%m-%d %H:%M:%S')#将日期转换为指定的显示格式
    # pre_time = time.strptime(pre_date, "%Y-%m-%d %H:%M:%S") #将时间转化为数组形式
#    print(pre_date)
    pre_stamp = int(pre_date.timestamp()) #将时间转化为时间戳形式
    print(pre_stamp)
    print(the_date)
    print(date_now)
    print(int(855/20))
