# github_intro
Introduction to git/github for the team members

## Explanations about git, github...



![github_workflow](https://i0.wp.com/build5nines.com/wp-content/uploads/2018/01/GitHub-Flow.png?fit=900%2C310&ssl=1)

**TODO** : explanations about git/github, .gitignore, installations (GUI for windows or atom), team_nbc organization...

## Mini example
### Goal

A [csv file](team_members.csv) containing the team pseudos is available along with corresponding [hex colors](https://g.co/kgs/QYgAHH). This table is loaded by a [python script](python_example/draw_names.py) which saves the following picture in the [output](output) folder:

![](output/out_python.png)

Your job here is to:

- **Clone** the repository
- Add your name to the csv file (e.g. using excel)
- Re-run the python script to update the figure with your name
- **Commit** your changes on your computer
- **Push** your commit to the online repository

### Installation and running the script
**TODO** : Python install if needed

From the command line, clone the repository and from the repository folder install the requirements:

```bash
$ git clone https://github.com/teamnbc/github_intro.git
$ cd github_intro
$ pip install -r requirements.txt
```

Then the python script can be run as follows:
```bash
$ python -m python_example.draw_names
```
