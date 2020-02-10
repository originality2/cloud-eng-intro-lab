# Introduction to Clound Computing: IaaS and PaaS

In this workshop you will deploy a Flask App to the App Engine.

# Pre-requisites 
### Git is installed
This allows you to run git commands in the terminal
- Mac: https://www.atlassian.com/git/tutorials/install-git#mac-os-x
- Windows: https://www.atlassian.com/git/tutorials/install-git#windows

### Docker Desktop is Installed
> Required to run flask app locally 
- Mac: https://hub.docker.com/?overlay=onboarding&step=download
- Windows: https://docs.docker.com/toolbox/toolbox_install_windows/
  > Note: Docker Desktop is not available to Windows 10 Home, so we will use Docker Toolbox instead
  
### Gcloud SDK is installed
> This allows you to run gcloud commands in the terminal
- Mac: https://cloud.google.com/sdk/docs/downloads-interactive#mac
- Windows: https://cloud.google.com/sdk/docs/downloads-interactive#windows

### VS Code is installed (or an editor of your choice)
- Mac: https://code.visualstudio.com/download
- Windows: https://code.visualstudio.com/download

# Let's Get Started!
### Step One: Cloning the repo
We need to first clone this repo so that there is a local copy of the app on your machine. 
Navigate to where you want to clone your repo. I recommend creating a directory for all your directories. e.g.
```sh
$ cd ~/Users/[user]
$ mkdir repos
$ cd repos
```
Clone into the directory
```sh
$ git clone https://github.com/originality2/cloud-eng-intro-lab.git
```
And navigate to the directory
```sh
$ cd cloud-eng-intro-lab
```

### Step Two: Running the app locally
The application is set to run in a Docker container upon initialisation. We have used a Makefile to define a set of directives to run our docker container. This workshop does not cover [containerisation] or [Makefiles], but I encourage you to read more on it.

Run the app
```sh
$ make
```

On successful build and run, follow the hyperlink provided in the terminal. 

### Step Three: Editing the app
Feel free to customise the app however you see fit prior to deployment.

### Step Four: Setting up for App Engine
-- TO DO --

### Step Five: Deploy application 
-- TO DO --

[containerisation]:<https://www.docker.com/resources/what-container>
[Makefiles]:<https://www.gnu.org/software/make/manual/html_node/Introduction.html>
