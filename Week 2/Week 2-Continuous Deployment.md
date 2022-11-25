# MSDS 434 Final Project- Nitya Pariti 
- This document outlines the steps taken to ensure a proper CI/CD pipeline from a git repo was created 
- The first step was to clone the git repository in GCP using the command line (git clone https://github.com/npariti/MSDS434FinalProject)
- Any of the files could be edited within the powershell (Vi test.py). In this file, you could press 'Shift'+'I', and that would allow editing with the file. After editing, pressing ESC--> Shift+Z would exit out of the browser 
- To commit the changes, the following commands can be run: 
  - git add test.py 
  - git commit -m "commit" 
  - git push -u origin main 
    - There was a dev branch and a main branch created, so to push changes to the dev branch, the following command could be run: git push origin dev
