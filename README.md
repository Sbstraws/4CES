# LiftEmotion

### Techinical Requirements
* Python 3.7
* Flask
* Google Cloud AutoML


### Installation
Using Python 3.7...
* create a virtualenv
* Install requirements
    - change to this directory
    `cd LiftEmotion`
    - install requirements
    `pip install -r requirements.txt`
* Environment variable
    - create a googlekey.json file in the root of ./LiftEmotion
    `touch ./googlekey.json`
    - paste your private key data here
    - set environment variable for key
    `GOOGLE_APPLICATION_CREDENTIALS=googlekey.json`

### Run
In the LiftEmotion directory... 
* activate the virtualenv
* run flask
`flask run`

### Current version
- In App.py, enter content information for the content variable (text to be tested)
- stop/restart flask to re-run the application
- output is json of the ML response

### Next Steps
* create a flask web form to accept text (see resources)
* Create a better template display output


### Resourses
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms
