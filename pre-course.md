# Pre-course installation instructions

For this course, we need the following software installed and working:
- python (v3)
- ipython (v3)
- scipy
- matplotlib
- pyqtgraph
- an IDE or text editor: I recommend Pycharm (spyder or jupyterlab may also be ok, but I'll prioritize support on PyCharm)

The following instructions will use miniconda to install everything (except PyCharm). If you work on debian/ubuntu, you can alternatively install all this with the package manager (but I'll prioritize support on miniconda installations).


## Preparing the environment with miniconda

### Download miniconda
Download the miniconda installer from https://conda.io/miniconda.html

Which installer to choose?
- 32b or 64b? If your OS is 64b, choose 64b
- python3 or python2? Better choose py3.

### Install miniconda
If working on windows, execute the installer, and select default options.

If working on linux, use: `bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda`  (adjust the name of the .sh file to the one you downloaded). **Do not forget to pass the -b option** (we do not want the PATH variable to be adjusted by conda)

### Create a python environment with all the modules used in the course

First enter into a conda session:

- on windows just open the "Anaconda prompt" from the start Menu->Anaconda
- On linux, run: `source $HOME/miniconda/bin/activate`

**IMPORTANT**: At this point you should be in a console whose prompt starts with `(base)`. If not, check that all previous steps were done without errors.

Now create a new environment with the programs that we use in the course (follow
[these instructions](http://taurus-scada.org/users/getting_started.html#installing-in-a-conda-environment-windows-and-linux))

**IMPORTANT**: At this point you should be in a console whose prompt starts with `(py3qt5)`

Install Taurus and some extra dependencies

```
pip install taurus
pip install taurus_pyqtgraph
```


... and finally check that it all works, e.g.:

```
taurus --help
taurus form "eval:rand()"
```

## Install Pycharm community edition

This is optional for the intro course, but very recommended for more advanced courses.

PyCharm is a very complete IDE (Integrated Development Environment). I recommend it over spyder when getting into "serious" programming. Spyder is fine (and simpler to use) for a more casual programmer.

See download and installation instructions in:

https://www.jetbrains.com/pycharm/download

Note: I recommend installing the **"Community" Edition** (not the "Professional" one). The Community Edition is Open Source and powerful enough.


### Create a PyCharm project for the course

- Download (or git-clone) the course files
- In the conda prompt where the "py3qt5" environment is activated, type 
  `where python` (in windows) or `which python` (in linux) to find out the path 
  of the python executable for the "course" environment.
- Open PyCharm and "Create New Project"
  - Location: choose the downloaded course dir (or cloned repo dir, if you used git)
  - Interpreter -> **Existing** interpreter -> `...` -> Conda environment -> 
  and choose the python executable that you found out before for the "py3qt5" conda environment.
- Check that `Settings-> editor-> inspections-> code compatibility inspections` is set to 3.5, 3.6, 3.7 and 3.8
 

## (Optional) Create a local tango system using docker

This is optional. It is only needed if you want to run a complete self-contained tango system locally in your computer.

This requires the installation of docker and downloading ~2Gb of data.

It is not needed if you have access to an already-running Tango system (such as those in ALBA's control room or a beamline).

- Install docker (including docker-compose). See the instructions for your OS [here](https://docs.docker.com/get-docker/). 
    - Note that for older versions of Windows or Mac where "Docker Desktop" cannot be installed, you may install [Docker-toolbox](https://docs.docker.com/toolbox/)
    - For GNU/Linux users make sure to also install [Docker-compose](https://docs.docker.com/compose/install/)
- Check that docker runs by issueing the following commands (for details, see [this](https://docs.docker.com/get-started/)):
    - `docker --version`
    - `docker run hello-world`
- Download the tango docker images (from the root of the course directory):
  ```
  cd pythoncourse-intro  # make sure that you are at the course dir
  docker-compose pull
  ```
  
- To start the tango system, you can do (from the root of the course dir):
  ```
  docker-compose up -d
  ``` 
  
- To check the tango system, you can do (from the root of the course dir):
  ```
  docker ps
  ```
  you should see something like:
  ```
               Name                            Command               State            Ports          
  ---------------------------------------------------------------------------------------------------
  pythoncourse-intro_tango-cs_1     /bin/sh -c /usr/local/bin/ ...   Up      0.0.0.0:10000->10000/tcp
  pythoncourse-intro_tango-db_1     docker-entrypoint.sh mysqld      Up      0.0.0.0:9999->3306/tcp  
  pythoncourse-intro_tango-test_1   /usr/bin/supervisord --con ...   Up           
  ```
  
- To stop the tango system, you can do (from the root of the course dir):
  ```
  docker-compose down
  ```