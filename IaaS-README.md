# Introduction to Cloud Computing: IaaS Lab

This is an optional step, but here are the instructions to deploy the app to Compute Engine (an Infrastructure as a Service product)

### Step One: Making a VM
- In the [GCP Console], navigate to Compute Engine -> Vm Instances in the Navigation Menu.
- Click "Create" to make a new instance
- Name: whatever you like
- Region: australia-southeast1 (Sydney)
- Zone: any
- Machine Family: default
- Bootdisk: Debian GNU/Linux 9 (stretch)
- Allow HTTP traffic
- Create!

### Step Two: Remoting into the Instance/VM
- Click SSH

### Step Three: Provisioning 
- install Python tooling
```
sudo apt-get update
sudo apt-get install python-setuptools python-dev build-essential
```
- install Git
```
sudo apt-get install git
```
- install pip
```
mkdir repos
cd repos
git clone http://github.com/originality2/get-pip.git
cd get-pip
python get-pip.py
PATH=~/.local/bin:$PATH
```
- install flask
```
pip install flask
```
- install docker
https://docs.docker.com/install/linux/docker-ce/debian/

### Step Three: Cloning the app repo
Clone into the repos directory
```sh
cd ~/repos
git clone https://github.com/originality2/cloud-eng-intro-lab.git
```
And navigate to the directory
```sh
cd cloud-eng-intro-lab
```

### Step Four: Running the Flask App
```
sudo make
```

### Step Five: Setting up for App Engine
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

  handlers:
  - url: /static
    static_dir: static
  - url: /.*
    script: main.app

  libraries:
    - name: ssl
      version: latest
  ```

### Step Six: Deploy application 
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


[GCP Console]:<https://console.cloud.google.com/>
