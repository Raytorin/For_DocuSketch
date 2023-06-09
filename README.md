# About
### This application builds plots on which the deviations of the floor vs ceiling corners. Accepts a json file as input and outputs all histograms to jupiter notebook
# Tech Stack
### - [Python](https://www.python.org/)
### - [Jupiter Notebook](https://jupyter.org/)
### - [Pandas](https://pandas.pydata.org/)
### - [Pillow](https://python-pillow.org/)
# Setup
### Before launching, install the necessary libraries from requirements.txt
### 1) `python -m pip install -r requirements.txt` or `pip install -r requirements.txt`
### 2) Enjoy:)
# Note
### __main.py__ - *DrawingPlots* class with the *draw_plots* function, which takes as input the location of a json file and optional max count of elements. Returns a list with the path of all plots
### __Notebook.ipynb__ - displays plots, at the beginning you need to specify the location of the json file
# Tests
### Used by unittests
### 1) `python -m unittest tests/main_tests.py`
![GitHub](https://img.shields.io/github/license/Raytorin/For_DocuSketch)
![GitHub language count](https://img.shields.io/github/languages/count/Raytorin/For_DocuSketch)
![GitHub top language](https://img.shields.io/github/languages/top/Raytorin/For_DocuSketch)