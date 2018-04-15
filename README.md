# The MapReduce Articles Series Source Code

This repository contains the source code for the articles series about MapReduce:
* *Part 1:* https://klaregis-portal.appspot.com/software/articles/0001/mapred-part1.html. 



## 1. Getting Started

Please clone this directory by doing: 

```
$ git clone https://github.com/rejux/mapreduce-python.git
$ cd mapreduce-python
```

You now have a copy of the **mapreduce-python** project on your host. 

### 1.1. Content For Part 1

The content for the part 1 of the series is as follows:

```
$ ls -l
total 28
drwxr-xr-x 2 xxxxxx xxxxxx 4096 avril 15 08:52 input
-rw-r--r-- 1 xxxxxx xxxxxx 1101 avril 15 08:52 MIT-LICENSE.md
-rw-r--r-- 1 xxxxxx xxxxxx 1041 avril 15 08:52 one_process_MR.py
-rw-r--r-- 1 xxxxxx xxxxxx 2224 avril 15 08:52 README.md
-rw-r--r-- 1 xxxxxx xxxxxx 2436 avril 15 08:52 simple_MR.py
-rw-r--r-- 1 xxxxxx xxxxxx 6267 avril 15 08:52 tools_MR.py
```

### 1.2. Prerequisites

The only prerequisites is the Python interpreter. The code has been run under a Python 3.5.x interpreter; 
but even a 2.7.x interpreter will suffice.

## 2. Running

To run the code, execute the following commands according the part of the series you are currently reading.
Remember to confer to the articles that also provide detailed instructions regarding the part you are 
intested in.

### 2.1. Part 1

Execute the *simple_MR.py* program:

```
$ cd mapreduce-python
$ python simple_MR.py
```
Execute the *one_process_MR.py* program:
* from the Pyton REPL:

```
>>> import sys
>>> sys.argv = ['./input/text.txt']
```

or

```
>>> sys.argv = ['./input/sentence.txt']
```

then

```
>>> exec(open('one_process_MR.py').read())
```

* from the command line:

```
$ cd mapreduce-python
$ python -c "import sys ; sys.argv = ['./input/sentence.txt'] ; exec(open('one_process_MR.py').read())"
```

or

```
$ python -c "import sys ; sys.argv = ['./input/text.txt'] ; exec(open('one_process_MR.py').read())"
```

## Authors

* **Régis Kla, Ph.D. (klaregis@gmail.com)** - *Blog* - [RegisKla](https://klaregis-portal.appspot.com/)

## License

This project is licensed under the MIT License - see the [MIT-ICENSE.md](MIT-LICENSE.md) file for details

## Acknowledgments

See the MapReduce articles series:
* [MapReduce1](https://klaregis-portal.appspot.com/software/articles/0001/mapred-part1.html.)

