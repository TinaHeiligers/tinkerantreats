Title: Python projects
Date: 2016-07-31
Category: Python

This page is for Python related goodies.

# Making a virtual environment work in Sublime text:

1. Save as a new Project
2. Edit the projectname.sublime-project json script to include the path to the new build envitonment as follows:

``` javascript
{
 "folders":
 [
  {
   "path": "."
  }
 ],
 "virtualenv": "/Users/Tina/.virtualenvs/strengths",
 "build_systems": [
  {
   "name": "strengths",
   "cmd": ["/Users/Tina/.virtualenvs/strengths/bin/python", "$file"]
  }
 ] 
}
```
3. Select SHIFT+COMMAND+P to select the build system using build with.....

# Learning Python for Data Science
There's a host of free online leraning materials that look well worth exploring.
[Data Science Central's](http://www.datasciencecentral.com/profiles/blogs/learning-python-for-data-science) lists a whole hist of links to the categories given below. Here, I'm only going to document and give links to the ones I think I'll get to.


## Tutorials
[Codementor](https://www.codementor.io/startups/tutorial) appears to be free, has sections for [Tutorials](https://www.codementor.io/tutorial), [Insights](https://www.codementor.io/learn-programming), [Startups](https://www.codementor.io/startups/tutorial), a [blog](https://www.codementor.io/blog) and [Case Studies](https://www.codementor.io/success-stories).

The Startups section has a list of articles that are expensive enought to give one value from reading them but concise enough to read in one sitting. [This one](https://www.codementor.io/startups/tutorial/developer-guide-to-launching-a-startup-marketing-101) on start-ups is great to share!.

They also have code mentors who one can pay to help you out.
It costs money but may be worth it if there's no body else around. For [python mentors](https://www.codementor.io/python-experts), the cost is between $50 and $15 per 15 minutes. This could get expensive!

## Open Online Resources
MOOCS, mostly not free but the ones by [udemy on matplotlib](https://www.udemy.com/data-visualization-with-python-and-matplotlib/?siteID=OyHlmBp2G0c-.mew2nb1tZlughhOlrk9wg&LSNPUBID=OyHlmBp2G0c) and [pandas](https://www.udemy.com/data-analysis-with-python-and-pandas/?siteID=OyHlmBp2G0c-Z6IUOHV0hSLSK3Hag30vXw&LSNPUBID=OyHlmBp2G0c) are cheep enough ($12 and $15, respectively), don't have set assignmnets (perhaps a good thing or not?) and no exams (that's a big win!) THe Pandas one I must do, it's only 6 hours long and would be a very good thing to get a handle on!

## Resources and newsletter
Already signed up to those...

## Cheet sheets
THere are several sheet sheets for the statistical and data science libraries used in Python. Links to these are given in the other page `<{other.md}../Other/other.md>`_

# Machine Learning
Basically, machine learning problems can be split into two fields: classification and prediction. Classification is supervised learning where we want to find the similarity between variables where supervision ocmes into play in that the training set has been classified already.
Prediction is generally unsupervised learning, where we want to predict an outcome based on some data.

## Common algorithms
Analytics Vidhya did it again with a fantastic [post](https://www.analyticsvidhya.com/blog/2015/09/full-cheatsheet-machine-learning-algorithms/) giving both R and python code for 10 most commonly used machine learning algorithms.
It covers just the basics, but is a great start!
Algorithms covered:
1. Linear Regression
2. Logistic regressing
3. Decision Tree
4. SVM (Support Vector Machine)
5. Naive Bayes
6. kNN (k-Nearest Neighbors)
7. k-Means
8. Random Forest
9. Dimensionality Reduction Algorithms
10. Gradient Boosting & AdaBoost.
The R code is concise and there are a few lines of comments describing what the code does but msot of the pseudocode is given in the Python code section. It's referenced again on that page.


## Linear classification
An example of linear classification of [images of cats and dogs](http://www.pyimagesearch.com/2016/08/22/an-intro-to-linear-classification-with-python/) is given in this excellent work-through tutorial.
The tutorial makes extensive use of the scikit-learn library and numpy. Pandas is not used.

# Data Visualisation
Interactive maps are the rage right now and that's because they're fascinating!
Drawing on inspiration from Leaflet and Libchamplain, [mapview](https://github.com/kivy-garden/garden.mapview) is a Kivy widget for doing just that.
THe link will take you to the github repo and the readme explains feautres, requirements, installation and usage.
