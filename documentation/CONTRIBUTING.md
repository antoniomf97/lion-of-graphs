# Contributing to Lion Of Graphs

🚧 *under construction* 🚧

## Developing methodology

- #### Git Workflow:
  In this project, we adopt the [Trunk Based Development](https://trunkbaseddevelopment.com/) as the source-control branching model. it is is one of a set of capabilities that drive higher software delivery and organizational performance. This model is focused in the development of a single main branch, called "trunk", resisting to any pressure to create other long-lived development branches. In practise, each developer divides their own work into small batches and merges that work into trunk at least once (and potentially several times) a day. Naturally, for a single developer the model is reduced to the direct development of the master branch.

  The only exception in this work to this sort of development, is that release branches are not present, assuming the master is the latest and the truest form of the live application.

  **IMPORTANT**: every branch has to be merged through a *PULL REQUEST* and has to be approved by at **least** one developer. Branches shall be **squashed and merged** into a single meaningful commit.

- #### Branching Nomenclature:
  Following the previously mentioned workflow, in multi-colaborators project, each feature/hot fix branch shall follow the following nomenclature:
  `<identifier>/<work-type>/<description>`

  The `identifier`should be a string that each collaborator should choose and stick to it, in order to ease the development process, namely with auto completion when checking out between branches. The `work-type` should fall between the values of `doc`, `ftr`, `fix`, or any other three letter description of the existing work.

- #### Commits terminology:
  Merge commits must have a single line with the maximum of 50 characters, in imperative form, declaring the changes made, and if possible, their basic purpose. The following message, with each line reaching no more than 70 characters, has to explain the **HOW** and **WHY**, rather than the *what*, since the last question should be answered through code.

  Branch commits do not matter.

🚧 *under construction* 🚧

## Looking for support?

🚧 *under construction* 🚧

## How to report a bug

🚧 *under construction* 🚧

## Code of conduct

This project is governed by the [Contributor Covenant Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.
