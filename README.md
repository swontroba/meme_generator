# Meme Generator Project
Meme Generator, second project of the Intermediate Python Nanodegree.

[Udacity Intermediate Python Nanodegree Program](https://www.udacity.com/course/intermediate-python-nanodegree--nd303)

## Overview

Meme Generator – Instructions
Of the page: The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote.

## Main Modules

- [QuoteEngine](./QuoteEngine)
- [MemeEngine](./MemeEngine)

## Packages to be installed

- [Flask](https://github.com/pallets/flask/)
- [Pandas](https://github.com/pandas-dev/pandas)
- [Python-docx](https://github.com/python-openxml/python-docx)
- [Pillow](https://github.com/python-pillow/Pillow)
- [Requests](https://github.com/psf/requests)
- [matplotlib](https://matplotlib.org/)

## Packages used and imported
- [typing](https://github.com/python/typing)
- [random](https://github.com/python/cpython/blob/main/Lib/random.py)
- [subprocess](https://github.com/python/cpython/blob/main/Lib/subprocess.py)
- [ABC](https://github.com/python/cpython/blob/main/Lib/abc.py)
- [os](https://github.com/python/cpython/blob/main/Lib/os.py)
- [argparse](https://github.com/python/cpython/blob/main/Lib/argparse.py)

## Usage

### Flask Web Interface

- Run `python app.py` on the terminal or IDE of your choice.
- Access the webpage via this url [http://localhost:5000](http://localhost:5000).

### Command Line Interface

- Run `python meme.py` on the terminal or IDE of your choice. 
- Pass the optional CLI arguments below:
  --body: string quote body
  --author: string quote author
  --path: path to image file
  
Resulting in a command like the following: 
- python meme.py --path [PATH to image] --body[BODY] --author[AUTHOR]

## Submodules Summary

This project is split up into several modules/directories, like defined in the project description.
The main ones are the [QuoteEngine](./src/QuoteEngine) and [MemeEngine](./src/MemeEngine) modules. 
They handle parsing & extracting data from files like txt, pdf or csv. 
Later using the data to create memes with the MemeEngine. 

Inside the MemeEngine matplotlib was used to find an font on the computer without using a specific path.

The \_data directory holds all the data for various parts of the project. 
The tmp directory is responsible for keeping temporary files created. 
The static directory is for static files created when running meme.py/app.py.
The .gitkeep file in there helps to add a completely empty directory.
The pyproject.toml has some specific ruff - code formatting configuration.
