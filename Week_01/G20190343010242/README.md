## Week 01 Assigments

See [here](https://u.geekbang.org/lesson/8?article=201439) for the requirements.

This assignment is done by python3.7, actually it should be ok with python3.4+. All the code has been tested under linux or macos. You must make sure you have python3 pre-installed before running the application. 

### About the Application (Task 1)
The application currently supports both top 250 of douban movies and douban books, also has potential to extends to other categories. You can configure the settings in <b>config.yaml</b> file. 

### Run Application (Linux or MacOS)

./run.sh <i>venv_name</i> <i>assignment</i> <i>target_name</i>

e.g.

Task 1:
```bash
$ ./run.sh myvenv task1 douban_movie
```
Task2: (third argument will be http method like 'get', 'post', 'put', etc.)
```bash
$ ./run.sh myvenv task2 post
```
<b>Note: </b> assignment argument can only be task1 or task2.

### For Windows Users

I don't have time to write bat file, but you can still run the application.

You need to pre-install python3 with virtual environment installed, then activate that environment. After that, you can run 
```
(venv) pip install -r requirements.txt
```
then run

Task 1:
```
(venv) python app.py douban_movie
```
Task 2:
```
(venv) python httpbin.py post
```


