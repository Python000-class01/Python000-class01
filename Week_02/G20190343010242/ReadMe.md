## Week02 Assignment

This application is used to display the user's shopping items and total price with discount if applicable.

### Data
This application doesn't use database. Instead, it uses csv files for the required data. The data is small only used to test 
the basic function of the application.

### Configuration
See config.yaml file to set locale and related discount values for different category of user.

### Prerequisite
Python3 and pip should be installed.

### Run Application (Linux or MacOS)

./run.sh <venv> <username>

### For Windows Users

I don't have time to write bat file, but you can still run the application.

You need to pre-install python3 with virtual environment installed, then activate that environment. After that, you can run 
```
(venv) pip install -r requirements.txt
```
then run
```
(venv) python week02_0242_app.py <username>