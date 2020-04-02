Python Introduction exercises 
=============================

At the end of each session, some exercises from this directory will be 
proposed, which you should try to solve before the next session. 

If you submit your solution I will review it and make comments (see the 
procedure below).

On the following session, we will discuss the different approaches and 
common problems/solutions.

Procedure for submitting your exercises:
----------------------------------------

In order to submit your exercises, we will use the [Fork-and-Pull model](https://en.wikipedia.org/wiki/Fork_and_pull_model),
which is the same that many developers use to coordinate in software 
collaborations.

First you need some preparation (only done once):
   
- [Sign-in into gitlab.com](https://gitlab.com/users/sign_in) (you can create a gitlab.com account, or use your login from google/facebook/github/etc). Make note of your Gitlab user name.

- Create you own public fork of the course repository using [this link](https://gitlab.com/alba-synchrotron/controls-section/pythoncourse-intro/-/forks/new).   

- If you haven't already, clone the **official** course repository:
   ```console
   git clone https://gitlab.com/alba-synchrotron/controls-section/pythoncourse-intro.git
   ```

Then, to submit a given exercise:

1. Make sure that your local copy is up-to-date with the official repository:
  ```console
  git pull
  ```

2. Open the corresponding file in your local copy of the `exercises` folder 
   (e.g. `warmup.py`), and solve the exercise, testing it in your PC.

3. When ready, go back to the [exercises page from the official repository][1]
   (**see important note below**). Then click on the file corresponding to the 
   exercise and select `Edit`. Copy & Paste your code here and click on the 
   `Commit Changes` button

4. You will be presented with a new page called `New Merge Request`. Just click 
   on the `Submit merge request` button. If you do not get here, it is probably 
   because you are editing a file in your own repository instead of the official
   repository (see note below).
   
5. This will create a *merge-request* which is where I will add comments when I 
   review the code that you wrote. You can also add comments in this 
   merge-request. Note: You can access your merge-requests at any time from 
   [here](http://gitlab.com/alba-synchrotron/controls-section/pythoncourse-intro/merge_requests)
   (tip: filter by "author" to see only your requests)
 
6. If, as a result of the review, you want to resubmit your code, just close 
   this merge-request and repeat steps 3-5.


**NOTE:** In step 3, make sure that you are editing the exercise file from 
[the exercises page from the official repository][1], **not your fork**. Just 
check that the address in the browser contains 

`gitlab.com/alba-synchrotron/controls-section/pythoncourse-intro`

and not `gitlab.com/YOUR_USER_NAME/pythoncourse-intro`


[1]: http://gitlab.com/alba-synchrotron/controls-section/pythoncourse-intro/tree/master/exercises
 
