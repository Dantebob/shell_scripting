# Intro To Sequence Processing
# Introduction

The aim of this exercise is to help you understand the basics of shell scripting, a skill that is used in genomic pipeline development

# Contents

-   [Getting set up](#getting-set-up)
-   [Completing the exercise](#completing-the-exercise)


# Getting set up

At this point, you should have
(1) basic knowledge on using the command line to navigate in terminal,
(2) an account on [Github](https://github.com/), and
(3) been introduced to the very basics of [Git](https://git-scm.com/).

IF you don't know how to use terminal, don't have a github account, or don't know how to use git, notify your instructor (they will help you get the pretest up and running). Otherwise, proceed to #1 below.

1.  Login to your [Github](https://github.com/) account.

1.  Fork [this repository](https://github.com/KLab-UT/4310-pretest) by
    clicking the 'Fork' button on the upper right of the page.

    After a few seconds, you should be looking at *your* 
    copy of the repo in your own Github account.

1.  Click the 'Clone or download' button, and copy the URL of the repo via the
    'copy to clipboard' button.

1.  In your terminal, navigate to where you want to keep this repo (you can
    always move it later, so just your home directory is fine). Then type:

        $ git clone the-url-you-just-copied

    and hit enter to clone the repository. Make sure you are cloning **your**
    fork of this repo.

1.  Next, `cd` into the directory:

        $ cd the-name-of-directory-you-just-cloned

1.  At this point, you should be in your own local copy of the repository.

1.  As you work on the exercise below, be sure to frequently `add` and `commit`
    your work and `push` changes to the *remote* copy of the repo hosted on
    GitHub. Don't enter these commands now; this is just to jog your memory:

        $ # Do some work
        $ git add file-you-worked-on.py
        $ git commit
        $ git push origin master

---

# Completing the exercise

Your goal in this exercise is to (1) summarize the number of fasta files in a directory, (2) summarize data from fasta files, and (3) create a directory that contains fasta file for each sequence from all fasta files. You must have a shell script written in bash that calls two python scripts. You will draw from computer science skills you have learned in classes up to this point. Each of these objectives is broken up below.

> note: This readme contains several code blocks. Blocks with a ```$``` prompt refer to command that can be executed using bash (or generally other shell languages). Blocks with a ```>>>``` prompt refer to python code. Blocks without a prompt refer to content within a text file.

## Summarize the number of fasta files in a directory
You should create a script that determines the total number of fasta files within a directory. Some of these files will be directly within the provided directory, while others might be nested within directories within the provided directory. Your output should include a file called "log.txt" that provides the total number of fasta files.

## Summarize data from a fasta file
You should create a script that will process a fasta file. This script should output information to "log.txt" that contains (1) the total number of sequences and (2) the total number of base pairs.


#### What is a FASTA file?
A fasta file stores genetic sequence data and a descriptive header for each sequence. A fasta file can have a single header or multiple headers. The header line can contain various items pertaining to the sequence, such as the chromosome, species, and individual ID. A header line is demarcated by the '>' character, and the following line(s) contain the sequence information pertaining to this specific header. The sequence line should only contain information pertaining to the sequence described by the previous header. A single fasta file can contain multiple sequences. Here is an example of what this can look like:

```
>Gene_4310, Brooks
AUGCACCGCUAG
>Gene_4310, Bailey
AUGGACCTCUAG
>Gene_4310, Benjamin
AUGTACCGCUAG
```

#### Looking at a FASTA file
Let's look at a sequence alignment. At the command line you can examine this file using ```vim ExampleAlignments/ExampleAlignment.fasta```.

> note: If you are new to using vim, you can exit without saving by typing ':q!' followed by enter.

Once you exit vim, you can count the number of sequences within this file from the command line by counting the number of headers:

```
$ grep '>' ExampleFasta1.fasta | wc -l
```

## Create a fasta file for each individual sequence 
You should create a script that creates a fasta file for each individual sequence, with the file names being the same as the header for the sequence. The files should be appended with the ```.fasta``` file suffix. These files should all be placed in a directory called ```individual_fastas```.

# Final product
#### What you started with
1. A directory (which will contain a number of fasta files and directories)
#### What you end with
1. A text file called ```log.txt``` with (1) the total number of fasta files, (2) the total number of sequences, and (3) the total number of bases across all fasta files.
1. A directory called ```individual_fastas``` that contains a fasta file for each individual sequence (where the title of the file comes from the sequence header and the file is of type ```.fasta```.
#### Requirements
You must have a shell script that is written in bash and two python files that the bash script calls.

# Final recommendations
Use ExampleAlignments as a test directory with test files- but this will not be the directory that will be used to test your script. I would draw out your approach using pseudocode before you start coding. What are the primary tasks you need to address? What kind of script will you write to address that task? You got this!



