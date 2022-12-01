# github_intro
Introduction to git/github for the team members

## A quick introduction to git and github main concepts

### Why use github in research

#### Github - Solo mode

#### Github - Collab mode



![github_workflow](https://i0.wp.com/build5nines.com/wp-content/uploads/2018/01/GitHub-Flow.png?fit=900%2C310&ssl=1)

**TODO** : explanations about git/github, .gitignore, installations (GUI for windows or atom), team_nbc organization...

## Mini example
### Goal

A [csv file](team_members.csv) containing the team pseudos is available along with corresponding [hex colors](https://g.co/kgs/QYgAHH). This table is loaded by a [python script](python_example/draw_names.py) which saves the following picture in the [output](output) folder:

![](output/out_python.png)

### Tasks

#### Github - Solo mode

- Create your own **[fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo)** of the repository from github interface
- **[Download / Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)** your **fork** of the repository from github interface
- Add your name to the csv file (e.g. using excel)
- Re-run the python script to update the figure with your name
- **Commit** your changes on your computer
- **Push** your commit to your online **fork**

#### Github - Collab mode

- Create your own **[fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo)** of the repository from github interface
- Create a new **[branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository#creating-a-branch)** in your fork of the repository
- **[Download / Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)** your **fork** of the repository from github interface
- **Change branch** to your newly created **branch** on your local copy of your **fork**
- Add your name to the csv file (e.g. using excel)
- Re-run the python script to update the figure with your name
- **Commit** your changes on your computer
- **Push** your commit to your **branch** of your **fork**
- Open a **[pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)** to the original repository so that your **commit** can be **merged**



### Installation and running the script
**TODO** : Python install if needed

After cloning the repository, change directory to the repository folder and install the requirements as follows:

```bash
$ cd github_intro
$ pip install -r requirements.txt
```

Then the python script can be run as follows:
```bash
$ python -m python_example.draw_names
```
