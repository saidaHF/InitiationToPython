# Pre-course installation instructions

For this course, we need the following software installed and working:
- python
- ipython
- scipy
- matplotlib
- pyqtgraph
- an IDE or text editor: I recommend Pycharm or spyder 

The following instructions will use miniconda to install everything (except PyCharm). If you work on debian/ubuntu, you can alternatively install all this with the package manager (although the miniconda instructions would also work for you too). 


## Preparing the environment with miniconda

### Download miniconda
Download the miniconda installer from https://conda.io/miniconda.html

Which installer to choose?
- 32b or 64b? If your OS is 64b, choose 64b
- python3 or python2? Better choose py3.

### Install miniconda
If working on windows, execute the installer, and select default options.

If working on linux, use: `bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda`  (adjust the name of the .sh file to the one you downloaded). **Do not forget to pass the -b option** (we do not want the PATH variable to be adjusted by conda)

### Create a python2 environment with all the modules used in the course

First enter into a conda session:

- on windows just open the "Anaconda prompt" from the start Menu->Anaconda
- On linux, run: `source $HOME/miniconda/bin/activate`


Now create a new environment with the programs that we use in the course (follow
[these instructions](http://taurus-scada.org/users/getting_started.html#installing-in-a-conda-environment-windows-and-linux))


Install Taurus and some extra dependencies

```
pip install taurus
pip install git+https://github.com/taurus-org/taurus_pyqtgraph.git
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

https://www.jetbrains.com/pycharm/

- Installation instructions for linux:
    - Copy the pycharm-2018.1.4.tar.gz to the desired installation location
    (make sure you have rw permissions for that directory)
    - Unpack the pycharm-2018.1.4.tar.gz using the following command:
    tar -xzf pycharm-2018.1.4.tar.gz
    - Remove the pycharm-2018.1.4.tar.gz to save disk space (optional)
    - Run pycharm.sh from the bin subdirectory

- Installation instructions for windows:
    - run the installer .exe

### Create a PyCharm project for the course

- Download (or git-clone) the course files
- In the conda prompt where the "course" environment is activated, type 
  `where python` (in windows) or `which python` (in linux) to find out the path 
  of the python executable for the "course" environment.
- Open PyCharm and "Create New  Project"
  - Location: choose the downloaded course dir (or cloned repo dir, if you used git)
  - Interpreter -> **Existing** interpreter -> `...` -> Conda environment -> 
  and choose the python executable that you found out before for the "course" conda environment.
- Check that the `Settings-> editor-> inspections-> code compatibility inspections` is set to 2.7, 3.5 and 3.6

