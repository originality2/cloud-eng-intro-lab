# Introduction to Cloud Computing: IaaS and PaaS

In this workshop you will deploy a Flask App to the App Engine.

Slides: https://docs.google.com/presentation/d/1Q_oNTZWsFdykGo9Ih5yKCruVm8xpORJ4AAp_VWe__sc/edit?usp=sharing

# Pre-requisites 
### Git is installed
This allows you to run git commands in the terminal
- Mac: https://www.atlassian.com/git/tutorials/install-git#mac-os-x
- Windows: https://www.atlassian.com/git/tutorials/install-git#windows
  
### Gcloud SDK is installed
> This allows you to run gcloud commands in the terminal
> You will also need a google login (work or personal) and a project of created within the Google Cloud Platform
> You will be prompted to choose a project on start up in the terminal, or to create your own.
- Mac: https://cloud.google.com/sdk/docs/downloads-interactive#mac
- Windows: https://cloud.google.com/sdk/docs/downloads-interactive#windows

### Python 2.7 is installed
> We need this to run one file in App Engine for deployment
> Yes, I know this is deprecated. I will upgrade to v3 soon!
- Mac: https://www.python.org/downloads/release/python-2717/
- Windows: https://www.python.org/downloads/release/python-2717/

# Let's Get Started!
### Step One: Cloning the repo
We need to first clone this repo so that there is a local copy of the app on your machine. 
Particularly if you are using Windows, if you are wanting to make changes to the app, it may be worth forking the repo and cloning the fork so that you can push and pull from here.
Navigate to where you want to clone your repo. I recommend creating a directory for all your directories. e.g.
```sh
cd ~
mkdir repos
cd repos
```
Clone into the directory
```sh
git clone https://github.com/originality2/cloud-eng-intro-lab.git
```
And navigate to the directory
```sh
cd cloud-eng-intro-lab
```

### Step Two: Deploy to Compute Engine
This is optional - you can follow along during the workshop or read instructions for later. It's extensive set up and I wouldn't recommend it for this kind of application (hence us using App Engine later)! 

https://github.com/originality2/cloud-eng-intro-lab/blob/master/IaaS-README.md

### Step Three: Editing the app
Feel free to customise the app however you see fit prior to deployment.
To open the project in VS Code: 
```
code .
```

### Step Four: Setting up for App Engine
For App Engine, we don't need any of the Docker files or Makefiles we have already made. We also do not need Docker or any bash scripting (big win for Windows!). All we need is a couple of small config files and we can deploy.
- Create a ```appengine_config.py``` file and specify the libraries we are using
  ```
  from google.appengine.ext import vendor

  # Add any libraries installed in the "lib" folder.
  # Includes jinja, flask (and heaps more: https://cloud.google.com/appengine/docs/standard/python/tools/built-in-libraries-27)
  # In this case, we are adding all available libraries
  # https://cloud.google.com/appengine/docs/standard/python/tools/appengineconfig
  vendor.add('lib')
  ```
- Create a ```app.yaml``` file and specify runtime, handlers and libraries
  For more on this: https://cloud.google.com/appengine/docs/standard/python/config/appref
  ```
  runtime: python27
  api_version: 1
  threadsafe: true
  # must be unique
  service: unique-app-name

  handlers:
  - url: /static
    static_dir: static
  - url: /.*
    script: main.app

  libraries:
    - name: ssl
      version: latest
  ```

### Step Five: Deploy application 
- Initialise gcloud
```
gcloud init
```
- Choose a project (or create a new one)
- While navigated into your app, deploy!
```
cd ~/repos/cloud-eng-intro-lab
gcloud app deploy
```
- Follow the link and see your app. You can check this link on another device - it's deployed up into the web!


[here]:<https://github.com/originality2/cloud-eng-intro-lab/blob/master/Windows-README.md>
