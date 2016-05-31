Python Introduction Course
==========================

This project contains materials and resources related to the Python Introductory
course at ALBA.

At least it contains:

- Slides for the course (they are just and index of topics that will be 
  explained in practice.

- Proposed exercises and my solutions to them

- solutions directory (empy, to be filled by the attendees, see below)

Pre-course checklist
--------------------

- make sure that python 2.x, ipython, matplotlib, scipy and spyder are 
  installed in your PC. If you use windows, just install 
  [PythonXY](http://python-xy.github.io). Try at least to launch spyder once. 
  If you need assistance, please contact Systems.

- read this intro: http://docs.python.org/2/tutorial/introduction.html

- follow this tutorial: http://introtopython.org/var_string_num.html

- and the first part (till the first block of exercises) of:
  http://introtopython.org/lists_tuples.html

About the exercises and solutions
---------------------------------

After each session, some exercises will be proposed, and the solutions from 
each attendee will be personally reviewed by me. On the next session(s) we will 
comment the different approaches and common problems.

The procedure for getting your exercises reviewed, is:

1. **Fork** this repository (use the "Fork repository" button from 
   [the project home page](https://gitcomputing.cells.es/cpascual/pythoncourse-intro).
    This will create your personal "copy" of this project in:
    `https://gitcomputing.cells.es/YOUR_USER_NAME/pythoncourse-intro`

2. **Download** your forked repo: 
   - You can use the "Download zip" button from: 
    `https://gitcomputing.cells.es/YOUR_USER_NAME/pythoncourse-intro`
   - Alternatively, advanced users may **clone** it using git:
   
            git clone https://gitcomputing.cells.es/YOUR_USER_NAME/pythoncourse-intro

3. Go to the exercises directory in your downloaded/cloned directory and 
   **work** on the already existing .py file corresponding to the exercise you 
   want to solve.

4. When finished, **upload** the solved exercise. *Suppose* you want to upload 
   your solution for `exercise0X.py`
   - If you downloaded and unzipped:
      - go to `https://gitcomputing.cells.es/cpascual/pythoncourse-intro/tree/master/exercises`
      - click on the `exercise0X.py` file and click on `edit`
      - Copy-paste your code in here
      - Put some descriptive comment in the "Commit message" box
      - click on "Commit Changes"
   - If you cloned with git, just commit and push the changed file:
        
            git add exercises/exercise0X.py
            git commit exercises/exercise0X.py - m 'finished exercise0X'
            git push origin/master

5. When I **review** your solution, I will **add comments** to your file. You 
   can **reply** with more comments.

6. If, as a result of the review you want to **do more changes** just repeat 
   steps 3 and 4
