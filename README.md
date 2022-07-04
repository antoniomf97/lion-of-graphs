# MPB
(under construction)

## Project Descriptions
  (under construction)

## Project Methodology
In this project, there are some assumptions that one must take into account. Namely, collaborators must be aware not 
only of the project policies but also of the applied methodology. In the following points, we will be going through the 
source-control branching model and the commiting terminology.
  
- #### Git Workflow:
  In this project, we adopt the [Trunk Based Development](https://trunkbaseddevelopment.com/) as the source-control 
  branching model. it is is one of a set of capabilities that drive higher software delivery and organizational 
  performance. This model is focused in the development of a single main branch, called "trunk", resisting to any 
  pressure to create other long-lived development branches. In practise, each developer divides their own work into 
  small batches and merges that work into trunk at least once (and potentially several times) a day. Naturally, for a 
  single developer the model is reduced to the direct development of the master branch.

  Below you can find a representative schematic of the Trunk Based complete workflow:
  
  ![plot](./Assets/gitworkflow.png)

- #### Branching Nomenclature:
  Following the previously mentioned workflow, in multi-colaborators project, each feature/hot fix branch shall follow 
  the following nomenclature: 
  `T<release version>-feature-<task identifier>` 
  that is, `T` (from trunk) followed by the current release version, then `-feature-` and finally an identifier that 
  defines the feature's corresponding task. Take the following branch as an example: `T0.1-feature-Task`.
  The referred tasks must be explicitly described on the project boards.

- #### Commits terminology:
  All commits are initialized with action that was taken on the respective commit, in specific, one of the following:
  - `ADD`: added a new file, document or directory to the project;
  - `UPD`: updated an existing file or document;
  - `RMV`: removed an existing file, document or directory from the
  project;
  - `TST`: tested (pre-release) the mentioned file;
  - `FIX`: solved an high priority hotfix issue;
  
  The performed action is then followed by a brief description of the commit, 
  including the affected files.
  <br>
  **Note:** multiple files may be modified in a single commit, 
  keeping in mind that all files must be mentioned in the commit
  message.

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