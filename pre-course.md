# Pre-course installation instructions

For this course, we need the following software installed and working:
- python 2.7
- ipython
- scipy
- matplotlib
- pyqtgraph
- an IDE or text editor: I recommend Pycharm and/or spyder 

The following instructions will use miniconda to install everything (except PyCharm). If you work on debian/ubuntu, you can alternatively install all this with the package manager (although the miniconda instructions would also work for you too). 


## Preparing the environment with miniconda

### Download miniconda
Download the miniconda installer from https://conda.io/miniconda.html

Which installer to choose?
- 32b or 64b? If your OS is 64b, choose 64b
- python3 or python2? It does not matter. Both will allow you to create py2 and py3 environments.

### Install miniconda
If working on windows, execute the installer

If working on linux, use: `bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda`  (adjust the name of the .sh file to the one you downloaded). **Do not forget to pass the -b option** (we do not want the PATH variable to be adjusted by conda)

### Create a python2 environment with all the modules used in the course

First enter into a conda session:

- on windows just open the "Anaconda prompt" from the start Menu
- On linux, run: `source $HOME/miniconda/bin/activate`

Now create a **python2** environment called "course" with the programs that we use in the course:

`conda create -n course -c conda-forge python=2 pyqt=4 ipython scipy matplotlib pyqtgraph spyder`


Now you can enter the newly created environment (activate it) with:

`conda activate course`

Within the activated course environment, check that spyder can be launched with the following command:

`spyder`

See more info in:
https://conda.io/docs/user-guide/getting-started.html


## Install Pycharm community edition

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

