Title: R
Date: 2016-07-31
Category: R

You'll only find R-related things here..
## R Basics
I've suckered myself into running an R bootcamp in the Valley and so far have compiled classes that cover a little of the basics.
The first class on matrices and data frames is very basic and far more info can be found on the web than what I cover in the [document](http://rpubs.com/ChristianeHeiligers/MatricesAndDataFrames).
The second deals with [reading](http://rpubs.com/ChristianeHeiligers/ReadingDataIntoR) typical data file formats into R.

## Data Visualisations:
### Scatter plots
1. [Plot some variables against many others with tidyr and ggplot2](http://feedproxy.google.com/~r/RBloggers/~3/fHtoZ8qm7Ag/?utm_source=feedburner&utm_medium=email) gives a brief tutorial on how to use tidyr and ggplot2 to plot all the variables in the mtcars data set as scatter plots. The code uses piping and facet_wrap instead of lattice, goes through a quick "how-to" on tidying the data and then shows some perks of ggplot2.
2. [Geographic filled area plots](https://www.r-bloggers.com/map-the-life-expectancy-in-united-states-with-data-from-wikipedia/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+RBloggers+%28R+bloggers%29) are created for life expectancy data gatheres from wikepedia in this R-bloggers post. It gives code used to make the plots and is a work-through tutorial. A definite must to go through and use for the R **bootcamp**!

Well worth following for quick vis of data sets that need a visual inspection to find possible correlations between variables.
3. [Plotting survey data](http://feedproxy.google.com/~r/RBloggers/~3/Rf0KMF0ZpvU/?utm_source=feedburner&utm_medium=email) is covered in detail in this post. The author shares his own function in detail, called plot.likert (given in the post), explains input variables and deals with potentially unselected responses.
Gives explination of defaults to the code.
The plot is a visualisation of the reponses given with some basics statistics.

## Working with Data
### Merging lists of datasets
1. [Merging a list of datasets](http://feedproxy.google.com/~r/RBloggers/~3/wj-qU0WpE78/?utm_source=feedburner&utm_medium=email) from a list created by reading in several individual sets from, say .csv, into one list in R is explained in this post.
Libraries used: readr and tibble. 

## Parsing Data
### Reading data into R
1. [readr 1.0.0](https://www.r-bloggers.com/readr-1-0-0/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+RBloggers+%28R+bloggers%29), explained nicely in an R-bloggers post by [Hadley Wickam](https://www.r-bloggers.com/author/hadleywickham/) himself, is used to read in .csv files. THe blog explains how to set column types, adding in throwing errors should there be a problem, deals with date-time parsing, low-level readers and writers and a few other changes. Two functions are mentioned that enable one to read in chuncks of data for data sets that are too big for memory, althought these are experimental API's and the user is warned to use the functions with care. These functions are read_csv_chunked() and read_lines_chunked(). 
2. [Image recognition](https://www.r-bloggers.com/image-recognition-in-r-using-convolutional-neural-networks-with-the-mxnet-package/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+RBloggers+%28R+bloggers%29) is dealt with in this post that uses the EBImage package to work with images of different sizes. There's some code but the user has to provide there own images.
Could be useful to work through, especially the **ML** part!