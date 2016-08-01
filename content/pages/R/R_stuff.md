Title: Using R for data and plotting
Date: 2016-07-31
Category: R

This folder is for R stuff.

## Data Visualisations:
### Scatter plots
1. [Plot some variables against many others with tidyr and ggplot2](http://feedproxy.google.com/~r/RBloggers/~3/fHtoZ8qm7Ag/?utm_source=feedburner&utm_medium=email) gives a brief tutorial on how to use tidyr and ggplot2 to plot all the variables in the mtcars data set as scatter plots. The code uses piping and facet_wrap instead of lattice, goes through a quick "how-to" on tidying the data and then shows some perks of ggplot2.

Well worth following for quick vis of data sets that need a visual inspection to find possible correlations between variables.
2. [Plotting servey data](http://feedproxy.google.com/~r/RBloggers/~3/Rf0KMF0ZpvU/?utm_source=feedburner&utm_medium=email) is covered in detail in this post. The author shares his own function in detail, called plot.likert (given in the post), explains input variables and deals with potentially unselected responses.
Gives explination of defaults to the code.
The plot is a visualisation of the reponses given with some basics statistics.

## Working with Data
### Merging lists of datasets
1. [Merging a list of datasets](http://feedproxy.google.com/~r/RBloggers/~3/wj-qU0WpE78/?utm_source=feedburner&utm_medium=email) from a list created by reading in several individual sets from, say .csv, into one list in R is explained in this post.
Libraries used: readr and tibble. 

