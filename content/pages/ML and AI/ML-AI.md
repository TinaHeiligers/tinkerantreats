Title: ML and AI
Date: 2016-09-16
Category: Machine Learning and Artificial Intelligence.

These were brief paragraphs and links scattered throughout the pages on this site and it became high time to gather these concepts together in their own category.

There may be some repetition here, since the following was literally copied and pasted below.
If there is anyone who reads this and is kind enough to point out where it becomes annoying, please let me know!

Both R and Python are used in the links that follow.

# Map it through!
New? Don't know where to start? Look no further! Follow this [map](http://scikit-learn.org/stable/tutorial/machine_learning_map/) and you'll get somewhere...

# Machine Learning
Machine learning, is it's raw essence is either classification or prediction problems. These are done using algorithms stemmed from raw maths. If you understand the maths, the rest is simply coding it all together!

# Overview
Basically, machine learning problems can be split into two fields: classification and prediction. Classification is supervised learning where we want to find the similarity between variables where supervision comes into play in that the training set has been classified already.
Prediction is generally unsupervised learning, where we want to predict an outcome based on some data.

Useful resources for dealing with factors or factor-like variables in a machine learning algorithm are:

1. [One-hot/One-of-k](http://code-factor.blogspot.com/2012/10/one-hotone-of-k-data-encoder-for.html) Data Encoder for Machine Learning.

2. [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

3. [OneHotEncoder](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) within the scikit learn library.

4. Converting [categorical data](http://fastml.com/converting-categorical-data-into-numbers-with-pandas-and-scikit-learn/) into numbers with Pandas and Scikit-learn

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

The R code is concise and there are a few lines of comments describing what the code does but most of the pseudo code is given in the Python code section. It's referenced again on that page.

In case some have been missed, another post covers their [10 algorithms](https://gab41.lab41.org/the-10-algorithms-machine-learning-engineers-need-to-know-f4bb63f5b2fa#.k5g1mndg5) ML engineers need to know.

## Linear classification
An example of linear classification of [images of cats and dogs](http://www.pyimagesearch.com/2016/08/22/an-intro-to-linear-classification-with-python/) is given in this excellent work-through tutorial.
The tutorial makes extensive use of the scikit-learn library and numpy. Pandas is not used.


Useful resources for dealing with factors or factor-like variables in a machine learning algorithm are:

1. [One-hot/One-of-k](http://code-factor.blogspot.com/2012/10/one-hotone-of-k-data-encoder-for.html) Data Encoder for Machine Learning.

2. [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

3. [OneHotEncoder](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) within the scikit learn library.

4. Converting [categorical data](http://fastml.com/converting-categorical-data-into-numbers-with-pandas-and-scikit-learn/) into numbers with Pandas and Scikit-learn

## Machine Learning - taken seriously
Going from knowing almost nothing to using machine learning in a "day-job" (if you're lucky enough to have one of those illusive things) can be done. Apparently, it can be done within a year. If taken seriously, very, very seriously!

Mr Borgen articulate his journey down this road very well in a [blog](https://medium.com/learning-new-stuff/machine-learning-in-a-year-cdb0b0ebd29c#.d3ggjur7t) post that starts with some Python code snippets. It's eye catching, a great read and makes it sound like a breeze at first. Then the nerves set in as one begins to realize the dedication, time and commitment it takes to venture up this very, very steep learning curve.

However, it can be done, like anything else, it's possible if broken down into steps, the first of which is reading his how-to-guide on [ML in a week](https://medium.com/learning-new-stuff/machine-learning-in-a-week-a0da25d59850#.n7uc79x7m).


#AI
What to write a few lines of Python following the PEP8 style guide? Then dive into this code that uses AI to get a bot to [reach 133/3131 in a Tron](http://kootenpv.github.io/2016-09-07-ai-challenge-in-78-lines) game. Apparently, there are other bots that have been written using many, many more lines of code, so it's an informative read.

#Common ML Questions:
Data science interviews, like any other technical interviews, test one's basic understanding of a process. Answering questions on the fly require a deep understanding of the underlying principles.
A good place to start is reading Q&A blogs, such as [this one](https://www.analyticsvidhya.com/blog/2016/09/40-interview-questions-asked-at-startups-in-machine-learning-data-science/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29) by the Analytics Vidhya.
I learned a lot by a simple read-through, and it offers links for further clarification of the underlying principles. 

For example:
"Q12. How is kNN different from kmeans clustering?

Answer: Don’t get mislead by ‘k’ in their names. You should know that the fundamental difference between both these algorithms is, kmeans is unsupervised in nature and kNN is supervised in nature. kmeans is a clustering algorithm. kNN is a classification (or regression) algorithm..."

For the more mathematically inclined, there are equations too:
"Q13. How is True Positive Rate and Recall related? Write the equation.

Answer: True Positive Rate = Recall. Yes, they are equal having the formula (TP/TP + FN)."

"Q14. You have built a multiple regression model. Your model R² isn’t as good as you wanted. For improvement, your remove the intercept term, your model R² becomes 0.8 from 0.3. Is it possible? How?

Answer: Yes, it is possible. We need to understand the significance of intercept term in a regression model. The intercept term is shows model prediction without any independent variable i.e. mean prediction. The formula of R² = 1 – ∑(y – y´)²/∑(y – ymean)² where y´ is predicted value.   

When intercept term is present, R² value evaluates your model wrt. to the mean model. In absence of intercept term (ymean), the model can make no such evaluation, with large denominator, ∑(y - y´)²/∑(y)² equation’s value becomes smaller than actual, resulting in higher R²."


