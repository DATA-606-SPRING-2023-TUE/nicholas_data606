# DRAFT PROPOSAL
### Nicholas Ho

# Coffee

Coffee is a popular drink worldwide and as a result is a large global industry.  The coffee industry is estimated to be valued in the hundreds of billions of dollars and every day alone, more than 2 billion cups of coffee are consumed.  With no shortage of demand, such a large industry can be an opportunity to analyze consumer trends for the purposes of maximizing profits.  This project seeks to take a look at coffee reviews from the website https://www.coffeereview.com/ in order to determine what characteristics are most favored by consumers and how these can be used to develop coffee in the future to increase profits.

https://en.wikipedia.org/wiki/Economics_of_coffee

## Goal: Analyze the reviews of a wide variety of coffees from around to world in an attempt to create the most profitable coffee.

In order to accomplish this goal, several small goals can be accomplished first:

• predict global demand and flavor trends

• determine what aspects of coffee reviwer's care about most

• datermine correlations between price and country of origin

## Dataset

Source: https://www.kaggle.com/datasets/hanifalirsyad/coffee-scrap-coffeereview/versions/2?select=coffee_df.csv

Dataset found on Kaggle was created by scraping the website www.coffeereviews.com for reviews between the dates Dec-2017 and Nov-2022

The dataset includes coffee from 988 unqiue origins with the most popular location being southern Ethiopia.  38 entries have unknown origins.

The original csv file includes 37 columns and 2282 rows.  Some rows and columns will need to be cleaned based off the presence of some null values.

Key features include: 

• origin

• roast

• price

• acid

• aroma

• body

• flavor

• description

Some of the values are object values in the original dataset and will need some convertion to a numeric system in order to perform regressions.

## Models and techniques:

• Sentiment analysis and natural language processing to analyze consumer reviews

• Lasso Regression/Ridge Regression to determine strength of correlation between features and price (feature selection to base predictions off of)

Using natural language processing, reviews can be scanned for key words to determine what customers seem to value in coffee.  These key words can be compared to ratings in order to train a prediction based on sentiment analysis.  Using this, it may be possible to predict future ratings based on the text of a review alone.  Furthermore, a correlation can be drawn between key words and high ratings in order to determine what customers seem to value in coffee.  This can give manufacturers an idea of what to produce in order to generate the best profits.
Coffee characteristics such as acidity, aroma, body, and flavor can also be compared with price and reviews in order to determine what combination of these characteristics result in the highest priced coffee and the coffee with the best consumer ratings.
Lastly, origin of the coffee may also be analyzed and determined whether or not to have a strong relation to the price or ratings.


