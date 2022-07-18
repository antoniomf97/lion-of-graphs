# MPB

![GitHub top language](https://img.shields.io/github/languages/top/MrToino/EGT-Sim?logo=Python)
![GitHub repo file count](https://img.shields.io/github/directory-file-count/MrToino/EGT-Sim)
![GitHub last commit](https://img.shields.io/github/last-commit/MrToino/EGT-Sim)
![GitHub](https://img.shields.io/github/license/MrToino/EGT-Sim)

(under construction)

## Project Descriptions
  (under construction)

## Project Structure

This is a monorepo project where all the necessary information to deploy the project is contained within this single source of truth. It's currently divided into the following structure:
- `application` the web application
- `assets` for documentation and README purposes
- `documentation` general documentation
- `services` the different services with their own APIs

## Project Methodology
In this project, there are some assumptions that one must take into account. Namely, collaborators must be aware not only of the project policies but also of the applied methodology. In the following points, we will be going through the source-control branching model and the commiting terminology.
  
- #### Git Workflow:
  In this project, we adopt the [Trunk Based Development](https://trunkbaseddevelopment.com/) as the source-control branching model. it is is one of a set of capabilities that drive higher software delivery and organizational performance. This model is focused in the development of a single main branch, called "trunk", resisting to any pressure to create other long-lived development branches. In practise, each developer divides their own work into small batches and merges that work into trunk at least once (and potentially several times) a day. Naturally, for a single developer the model is reduced to the direct development of the master branch.
  
  The only exception in this work to this sort of development, is that release branches are not present, assuming the master is the latest and the truest form of the live application.

  **IMPORTANT** every branch has to be merged through a *PULL REQUEST* and has to be approved by at **least** one developer. Branches are **squashed and merged** into a single meaningful commit.

- #### Branching Nomenclature:
  Following the previously mentioned workflow, in multi-colaborators project, each feature/hot fix branch shall follow the following nomenclature:
  `<identifier>/<work-type>/<description>`

  The `identifier`should be a string that each collaborator should choose and stick to it, in order to ease the development process, namely with auto completion when checking out between branches. The `work-type` should fall between the values of `doc`, `ftr`, `fix`, or any other three letter description of the existing work.

- #### Commits terminology:
  Merge commits must have a single line with the maximum of 50 characters, in imperative form, declaring the changes made, and if possible, their basic purpose. The following message, with each line reaching no more than 70 characters, has to explain the **HOW** and **WHY**, rather than the *what*, since the last question should be answered through code.

  Branch commits do not matter.

## Project Policies
(example from [template](https://betterscientificsoftware.github.io/A-Team-Tools/TeamPoliciesTemplate.html))

The following policies are meant to guide collaborators in their activities, establishing expectations for ongoing work.

- #### Code of Conduct:
    1. Collaborators will conduct themselves in a professional manner, following the project's code of conduct, 
       avoiding any non-professional behaviours.
    2. Collaborators will frequently update the project's Kanban boards. Specifically, each collaborator is in charge 
       of managing and updating the tasks to which they are assigned. The tasks priority order must be respected (Hot 
       Fixes, On Progress and To Do), although some ponctual exceptions are allowed, accordingly to the project plan.


## Contributors
![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=MrToino&show_icons=true&theme=react)
![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=luisferreira32&show_icons=true&theme=react)