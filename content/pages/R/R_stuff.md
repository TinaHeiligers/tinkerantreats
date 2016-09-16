Title: R
Date: 2016-09-16
Category: R

You'll only find R-related things here..
## R Basics
I've suckered myself into running an R bootcamp in the Valley and so far have compiled classes that cover a little of the basics.
The first class on matrices and data frames is very basic and far more info can be found on the web than what I cover in the [document](http://rpubs.com/ChristianeHeiligers/MatricesAndDataFrames).
The second deals with [reading](http://rpubs.com/ChristianeHeiligers/ReadingDataIntoR) typical data file formats into R.

## Data Visualizations:
### Scatter plots
1. [Plot some variables against many others with tidyr and ggplot2](http://feedproxy.google.com/~r/RBloggers/~3/fHtoZ8qm7Ag/?utm_source=feedburner&utm_medium=email) gives a brief tutorial on how to use tidyr and ggplot2 to plot all the variables in the mtcars data set as scatter plots. The code uses piping and facet_wrap instead of lattice, goes through a quick "how-to" on tidying the data and then shows some perks of ggplot2.

2. [Geographic filled area plots](https://www.r-bloggers.com/map-the-life-expectancy-in-united-states-with-data-from-wikipedia/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+RBloggers+%28R+bloggers%29) are created for life expectancy data gathered from wikipedia in this R-bloggers post. It gives code used to make the plots and is a work-through tutorial. A definite must to go through and use for the R **bootcamp**!

Well worth following for quick vis of data sets that need a visual inspection to find possible correlations between variables.

3. [Plotting survey data](http://feedproxy.google.com/~r/RBloggers/~3/Rf0KMF0ZpvU/?utm_source=feedburner&utm_medium=email) is covered in detail in this post. The author shares his own function in detail, called plot.likert (given in the post), explains input variables and deals with potentially unselected responses.
Gives explanation of defaults to the code.
The plot is a visualization of the responses given with some basics statistics.

## Working with Data
### Merging lists of datasets
[Merging a list of datasets](http://feedproxy.google.com/~r/RBloggers/~3/wj-qU0WpE78/?utm_source=feedburner&utm_medium=email) from a list created by reading in several individual sets from, say .csv, into one list in R is explained in this post.
Libraries used: readr and tibble. 

## Parsing Data
### Reading data into R

1. [readr 1.0.0](https://www.r-bloggers.com/readr-1-0-0/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+RBloggers+%28R+bloggers%29), explained nicely in an R-bloggers post by [Hadley Wickam](https://www.r-bloggers.com/author/hadleywickham/) himself, is used to read in .csv files. The blog explains how to set column types, adding in throwing errors should there be a problem, deals with date-time parsing, low-level readers and writers and a few other changes. Two functions are mentioned that enable one to read in chunks of data for data sets that are too big for memory, although these are experimental API's and the user is warned to use the functions with care. These functions are read_csv_chunked() and read_lines_chunked(). 

2. [Image recognition](https://www.r-bloggers.com/image-recognition-in-r-using-convolutional-neural-networks-with-the-mxnet-package/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+RBloggers+%28R+bloggers%29) is dealt with in this post that uses the EBImage package to work with images of different sizes. There's some code but the user has to provide there own images.
Could be useful to work through, especially the **ML** part!

3. [jailbreakr](https://www.r-bloggers.com/extract-tables-from-messy-spreadsheets-with-jailbreakr/), a fairly new package and very appropriately named makes extracting tables from messy spreadsheets a little easier. There's a 20 odd minute video included in the link and the main page shows a spreadsheet no one in their right mind would want to willing extract data from!

## Skills Tests in R:
### R for Data Science:
Various [tests](https://www.analyticsvidhya.com/blog/2016/08/full-solution-skill-test-on-r-for-data-science/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29) and the full solution for these tests on the basics of using R are given in this post from the Analytics Vidhya.

### R for Statistics
Of course, it's all great and fine to be able to manipulate data but we need to infer things from the data using [statistics](https://www.analyticsvidhya.com/blog/2016/08/solutions-for-skilltest-in-statistics-revealed/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29).

Another test and solution set from the Analytics Vidhya is useful for refreshing one's memory (or learning very quickly!).

# Sentiment Analysis using R and Shiny
Diego lescano posted what looks like a reasonably short tutorial on  how to create a simple application in R & Shiny to perform [Twitter Sentiment Analysis](http://www.datasciencecentral.com/profiles/blogs/how-to-create-a-twitter-sentiment-analysis-using-r-and-shiny) in real-time. While it looks short and the code isn't long, various packages are used (shiny, tm, workcloud, twitteR) and it may not be as easy as first appearances suggest.


