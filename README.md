# 5 Minute Challenge
###### This project will generate a 100 simple mathematics problems on a document.

Recently I've visited my friends home and noticed some mathematics problems written on papers,
I've asked them what is it for they said they write some problems on papers everyday as a task for there kid.
It came into my mind why can't I create a simple project which automatically creates some problems randomly and
stores in a document.

> It requires a single parameter as an input which tell about desired complexity.
To see help:
  > create-challenge --help
```
  complexity
              0: i) Additions up to 50
                 ii) Subtractions up to 50
                 iii) Multiplications up to table 6
                 iv) Divisions up to 10,
              1: i) Additions up to 100
                 ii) Subtractions up to 100
                 iii) Multiplications up to table 10
                 iv) Divisions up to 20
              2: i) Additions up to 200
                 ii) Subtractions up to 200
                 iii) Multiplications up to table 15
                 iv) Divisions up to 25,
              any_thing_else:
                 i) Additions up to 500
                 ii) Subtractions up to 500
                 iii) Multiplications up to table 20
                 iv) Divisions up to 50
```

Steps to install:

```
Step 1: Git clone the repository in your local machine.
        git clone https://github.com/pyprasad/createchallenge.git
Step 2: in project install modules using
        pip install .
Step 3: close and re-open your terminal, you should be able to see a command attached to your terminal as
        "create-challenge"
```

How to use:

```
   create-challenge --help
   create-challenge <complexity>

    Example:  create-challenge 0
```
