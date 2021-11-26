# CovidPrediction.com

## Background:
The world is now suffering and battling against Covid-19. To assist with the planning of government policies, we came out with a predictor model to provide some advices based on the trend since 2020.

In the website, you will be predicting:
- How strict your Stay-Home Requirement policy should be
- The number of Covid-19 cases in the country of your choice
based on the features you chose


## Setup

### Install Git

You need to have Git to do the project. Download and install the software according to your OS:
- Windows: [Git for Windows](https://git-scm.com/download/win)
- Mac OS: [Git for MacOS](https://git-scm.com/download/mac)

### Downloading Repository
Clone the mini project repository from Github. On your terminal or Git Bash, type the following:

```shell
$ cd Downloads
$ git clone https://github.com/kelliesyhh/t3-2d-ddw.git
```

### Go to "webpage" Folder

Once you have downloaded the repository, you can go to the repository and to the folder called `webpage` for this mini project.

```shell
$ cd webpage
$ ls
```

The last command should output the following:

```shell
Readme.md		
application.py
requirements.txt
app
```


## Create Virtual Environment (Windows)

**You should open Anaconda Prompt to do the following steps.**

In the following steps, the Windows prompt will be represented by:
```shell
>
```
Go to the root folder `webpage`.
```shell
> cd %USERPROFILE%\Downloads\webpage
```
From the root folder, i.e. `webpage`, create virtual environment called `virtenv`.

```shell
> python -m venv virtenv
```

A folder called `virtenv` will be created. Now, activate the virtual environment.
```shell
> virtenv\Scripts\activate
```

You should see the word `virtenv` in your prompt something like:
```shell
(virtenv) folder>
```

_To exit the virtual environment at the end of this mini project, simply type:_
```shell
> deactivate
```

## Create Virtual Environment (MacOS/Linux)


In the following steps, the MacOS/Linux prompt will be represented by:
```shell
$
```

Go to the root folder `webpage`. 
```shell
$ cd ~/Downloads/webpage
```

From the root folder, i.e. `webpage`, create virtual environment called `virtenv`.

```shell
$ python -m venv virtenv
```

A folder called `virtenv` will be created. Now, activate the virtual environment. 

```shell
$ source virtenv/bin/activate
```

You should see the word `virtenv` in your prompt something like:
```shell
(virtenv) user$
```

_To exit the virtual environment at the end of this mini project, simply type:_
```shell
$ deactivate
```
## Combined (Windows/Mac/Linux)

### Install Python Packages

Install the necessary packages for this mini project. From the root folder, i.e. `webpage`, type the following:

For Windows:
```shell
> python -m pip install -U --force-reinstall -r requirements.txt
```

For MacOS/Linux: (For Linux, you might need to type pip3 instead)
```shell
$ python -m pip3 install -U --force-reinstall -r requirements.txt
```

The above steps will install Flask and Transcrypt Python libraries and some other necessary packages.

 

## Update and Run the files:

## Windows

### Using Transcrypt

Javascript is the commonly used language for front-end web development. However, since this course only covers Python. We will use `Transcrypt` library which can compile and translate Python script into a Javascript file. To compile `library.py`, first we need to go into the `static` folder.

```shell
> cd %USERPROFILE\Downloads\webpage\app\static
> dir
```

The last command will list the file in that folder, and you should see:
```shell
library.py
```

Run Transcrypt on `library.py`:

```shell
python -m transcrypt -b -n library
```

The option `-b` means to build the javascript library. You can use `--help` for more options. Once it is done, you should be able to see a folder called `__target__` containing several files. To see the content of that folder:

```shell
> dir
> dir __target__
```

```shell
__target__/
  library.js
  library.project
  math.js
  org.transcrypt.__runtime__.js
  random.js
```

You should see `library.js` created inside this folder.

### Run Flask

Now you are ready to run your web app in your local computer. To do so, you need to go back to the root directory. This can be done with the following:

```shell
> cd ..\..
```

which means go up the folder two times. Or, simply

```shell
> cd %USERPROFILE\Downloads\webpage
```

You should see `application.py` in this root folder. 

#### Vocareum
If you use Vocareum terminal to run your Flask application, you can do so by running the `runflaskvoc.sh` script. Before running this script, make sure the `voc=True` is set true in the following line inside `webpage/app/__init__.py`.

```python
# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=True)
```

Now, make sure you are inside the `webpage` folder  by using the `pwd` command. 

```shell
> pwd
```

Use `ls` to ensure that you see the `runflaskvoc.sh` in the current folder.

```shell
> ls
```

Make sure that the script is executable by running the following command. 

```shell
> chmod a+x ./runflaskvoc.sh
```
The above script is to change the file to be executable for all users, group and owner.

To run the script, type the following.

```shell
> ./runflaskvoc.sh
```

Once it is running, you can open another tab in your browser and type the following url: [`https://myserver.vocareum.com/`](https://myserver.vocareum.com/).

To stop the web app type `CTRL+C`. 

#### Local Computer

If you are using your own computer, make sure to change the flag `voc=False` in the following line inside `webpage/app/__init__.py`.

```python
# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=False)
```

Now, you can run Flask by typing:

```shell
> flask run
```

You should see that some output will be thrown out, which one of them would be:

```shell
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now you can open your browser at `http://127.0.0.1:5000/` to see the web app. 

To stop the web app type `CTRL+C`. 


## MacOS/Linux

### Using Transcrypt

Javascript is the commonly used language for front-end web development. However, since this course only covers Python. We will use `Transcrypt` library which can compile and translate Python script into a Javascript file. To compile `library.py`, first we need to go into the `static` folder.

```shell
$ cd ~/Downloads/webpage/app/static
$ ls
```

The last command will list the file in that folder, and you should see:
```shell
library.py
```

Run Transcrypt on `library.py`:

```shell
python -m transcrypt -b -n library
```

The option `-b` means to build the javascript library. You can use `--help` for more options. Once it is done, you should be able to see a folder called `__target__` containing several files. To see the content of that folder:

```shell
$ ls
$ ls __target__
```

```shell
__target__/
  library.js
  library.project
  math.js
  org.transcrypt.__runtime__.js
  random.js
```

You should see `library.js` created inside this folder.

### Run Flask

Now you are ready to run your web app in your local computer. To do so, you need to go back to the root directory. This can be done with the following:

```shell
$ cd ../..
```
which means go up the folder two times. Or, simply
```shell
$ cd ~/Downloads/webpage/
```

You should see `application.py` in this root folder. Run Flask by typing:

```shell
$ flask run
```

You should see that some output will be thrown out, which one of them would be:

```shell
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now you can open your browser at `http://127.0.0.1:5000/` to see the web app. 

To stop the web app type `CTRL+C`. 




## First Prediction: Stay-Home Requirement Policy

In this section of the webpage, you will choose one scale for each of the 4 features using the drop-down list. There will be descriptions to explain the criteria of each scale. Users can choose the one that best matches their country.

Features:
- Vaccination Policy
- Testing Policy
- Facial Coverings
- Restriction Gatherings

Based on these 4 features, we will collect the inputs and run through our model to produce a **recommendations on how strict the Stay-Home Requirement Policy should be**.

The code will run when user press the predict button.


There are 4 possible outcomes from this prediction:
- No measures
- Recommended not to leave the house
- Required to not leave the house with exceptions for daily exercise, grocery shopping, and 'essential' trips
- Required to not leave the house with minimal exceptions (e.g. allowed to leave only once every few days, or only one person can leave at a time, etc.)


## Second Prediction: Covid-19 Cases

In this section of the webpage, you will first choose the country of your choice, and one scale for each of the 5 features using the drop-down list. There will be descriptions to explain the criteria of each scale. Users can choose the one that best matches their country.

Features:
- Vaccination Policy
- Testing Policy
- Facial Coverings
- Restriction Gatherings
- Stay Home Requirement Policy


Based on these 5 features, we will collect the inputs and run through our model to produce the **predicted number of Covid cases the country will likely have for it to require the policies you have chosen**. You can tryout different combinations to see how each policy affects the number of predicted covid cases.

The code will run when user press the predict button.


Have Fun!
