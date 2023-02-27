# FINAL PROPOSAL
### Nicholas Ho

# Maximizing Coffee Rating by Analyzing Coffee Reviews

Coffee is a popular drink worldwide and as a result is a large global industry.  The coffee industry is estimated to be valued in the hundreds of billions of dollars and every day alone, more than 2 billion cups of coffee are consumed.  With no shortage of demand, such a large industry can be an opportunity to analyze consumer trends for the purposes of maximizing profits.  This project seeks to take a look at coffee reviews from the website https://www.coffeereview.com/ in order to determine what characteristics are most favored by consumers and how these can be used to develop coffee in the future to increase profits.

https://en.wikipedia.org/wiki/Economics_of_coffee

## Goal: Analyze the reviews of a wide variety of coffees from around to world in an attempt to create a coffee with the highest rating.

In order to accomplish this goal, There are several angles that can be explored:

• Determine what aspects of coffee that consumers care about most

• Determine correlations between price and rating

• Examine trends in coffee tastes over time (A time series approach)

I will use the data to train a model to predict the rating of a coffee given a review, and use this model with a maximiztion function to determine the values for each feature that will maximize the rating.

## Dataset

Source: https://www.kaggle.com/datasets/hanifalirsyad/coffee-scrap-coffeereview/versions/2?select=coffee_df.csv

Dataset found on Kaggle was created by scraping the website www.coffeereviews.com for reviews between the dates Dec-2017 and Nov-2022

The dataset includes coffee from 988 unqiue origins with the most popular location being southern Ethiopia.  38 entries have unknown origins.  Origins are very specific and may need to be binned by country or region in order to produce a more accurate model.

The original csv file includes 37 columns and 2282 rows.  Some rows and columns will need to be cleaned based off the presence of some null values.

Key features include: 

• origin - object - City and Country where the beans originate from.  (Different from where they were roasted)

• roast - object - The temperature the beans were roasted at. (Light, Light-Medium, Full Medium, Medium-Dark, Dark)

• price - object - Dollars/ounces

• acidity - float64 - 1-10 scale

• aroma - float64 - 1-10 scale

• body - float64 - 1-10 scale

• flavor - float64 - 1-10 scale

• aftertaste - float64 - 1-10 scale

• description
- Blind Assessment - object
- Notes - object 
- Bottom Line (summary) - object 

There are many more useful features that may be used but these were selected in particular to look at due to them being objective numeric values that describe the coffee.

Some of the values are object values in the original dataset and will need some convertion to a numeric system in order to perform regressions.  (For example, the date the review was written)

## Models and techniques:

The main goal of this project is to predict the rating of a coffee given a review.  The rating will be the label.  Some techniques that will help determine the label include:

• Sentiment analysis and natural language processing to analyze consumer reviews.

Sentiment analysis will be used to convert the descriptive portion of the reviews of coffee into a numerical value between -1 and 1 (negative and positive).  Once the numerical number is determined, it can then be used as a feature to predict the overall rating of the coffee.  The model used will be a word-dictionary based model with an Opinion dictionary provided by NLTK (Natural Language Toolkit) for python.  This was choosen due to the low number of data points.  With only several thousand reviews, supervised learning such as naivebayes may not be properly fit.  A word-dictionary based model does not require any training and will not be affected by the number of data points.

• Lasso Regression/Ridge Regression to determine strength of correlation between features and rating (feature selection to base predictions off of)

There are many different features included in this data set.  Each review has various values that are used to describe the coffee.  Coffee characteristics such as acidity, aroma, body, and flavor can be compared in order to determine what combination of these characteristics result in the highest rated coffee.  Lasso Regression and Ridge Regression can identify which of these features have the biggest impact in predicting the label.  This will be useful when attempting to craft the highest rated coffee.

• Prediction Maximization (Simulation?)

Once the model has been trained using the regression techniques above, next is to find a way to maximize the outcome.  This can be done by simulating the model in a brute force method.  By testing all possible combinations of features, a model will be able to eventually determine the optimal combinations of features to produce the highest label value.  However this brute force method can become a very large task based on the number of features and possible values for each of those features.

## Final Result

A successful outcome of this project would be determining the best combination of features for producing the highest rated coffee based off a model trained by using the reviews from the dataset.  This information could give coffee producers an edge in the coffee industry and produce a coffee that consumers will love.

