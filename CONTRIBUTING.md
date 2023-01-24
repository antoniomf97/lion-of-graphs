# Contributing to Lion Of Graphs

In this document you can find all the information that is relevant for you as a contributor or developer. Please make sure to be aware of this project policies.

### Table of Contents

<ol>
  <li><a href="#developing-methodology">Developing methodology</a></li>
  <li><a href="#looking-for-support">Looking for support?</a></li>
  <li><a href="#how-to-report-a-bug">How to report a bug</a></li>
  <li><a href="#how-to-suggest-a-feature-or-enhancement">How to suggest a feature or enhancement</a></li>
</ol>


🚧 *under construction* 🚧

## Developing methodology

Regarding the project evolution, developers must follow a set of norms and rules that is common for everyone, to maintain a cohesive, comprehensive and stable development of the project. In the topics below you may encounter some of the main rules that you must comply with , such as the source-control branching model and the commiting terminology.

### Git Workflow

In this project, we adopt the [Trunk Based Development](https://trunkbaseddevelopment.com/) as the source-control branching model. it is is one of a set of capabilities that drive higher software delivery and organizational performance. This model is focused in the development of a single main branch, called "trunk", resisting to any pressure to create other long-lived development branches. In practise, each developer divides their own work into small batches and merges that work into trunk at least once (and potentially several times) a day. Naturally, for a single developer the model is reduced to the direct development of the master branch.

The only exception in this work to this sort of development, is that release branches are not present, assuming the master is the latest and the truest form of the live application.

**IMPORTANT**: every branch has to be merged through a **PULL REQUEST** and has to be approved by at **least** one developer. Branches shall be **squashed and merged** into a single meaningful commit.

### Branching Nomenclature:

Following the previously mentioned workflow, in multi-colaborators project, each feature/hot fix branch shall follow the following nomenclature:
`<identifier>/<work-type>/<description>`

The `identifier`should be a string that each collaborator should choose and stick to it, in order to ease the development process, namely with auto completion when checking out between branches. The `work-type` should fall between the values of `doc`, `ftr`, `fix`, or any other three letter description of the existing work.

### Commits terminology:

Merge commits must have a single line with the maximum of 50 characters, in imperative form, declaring the changes made, and if possible, their basic purpose. The following message, with each line reaching no more than 70 characters, has to explain the **HOW** and **WHY**, rather than the *what*, since the last question should be answered through code.

Branch commits do not matter.

🚧 *under construction* 🚧

## Looking for support?

🚧 *under construction* 🚧

## How to report a bug?

Think you found a bug? Please check the [list of open issues](https://github.com/MrToino/lion-of-graphs/issues) to see if your bug has already been reported. If it hasn't please [submit a new issue](https://github.com/MrToino/lion-of-graphs/issues/new).

Here are a few tips for writing great bug reports:

- Describe the specific problem, as detailed as possible;
- Include the steps to reproduce the bug, what you expected to happen, and what happened instead;
- Check that you are using the latest version of the project and its dependencies;
- Include what version of the project your using, as well as any relevant dependencies;
- Only include one bug per issue. If you have discovered multiple bugs, please file one issue for each;
- Include relevant screenshots or screencasts if possible;
- Even if you don't know how to fix the bug, including a failing test may help others track it down

🚧 *under construction* 🚧

## How to suggest a feature or enhancement

[Open an issue](https://github.com/MrToino/lion-of-graphs/issues/new) which describes the feature you would like to see, why would you want it, how it should work, and other informations you consider relevant.

🚧 *under construction* 🚧

## Code of conduct

This project is governed by the [Contributor Covenant Code of Conduct](./CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.
