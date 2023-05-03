# Nicholas_data606
My UMBC Capstone project

## Abstract

## Introduction

Coffee is a popular drink worldwide and as a result is a large global industry. The coffee industry is estimated to be valued in the hundreds of billions of dollars and every day alone, more than 2 billion cups of coffee are consumed. With no shortage of demand, such a large industry can be an opportunity to analyze consumer trends for the purposes of maximizing profits. This project seeks to take a look at coffee reviews from the website https://www.coffeereview.com/ in order to determine what characteristics are most favored by consumers and how these can be used to develop coffee in the future to increase profits.

## Objectives

Goal: Analyze the reviews of a wide variety of coffees from around to world in an attempt to create a coffee with the highest rating.
In order to accomplish this goal, There are several angles that can be explored:

- What aspects of coffee have the largest impact on rating and price?
- Which regions produce the best coffee?
- Does price and rating have a correlation?

I will use the data to train a model to predict the rating of a coffee given a review, and use this model with a maximiztion function to determine the values for each feature that will maximize the rating.

## Dataset

The dataset being used for this project was found on Kaggle and was created by scraping the website www.coffeereviews.com for reviews between the dates Dec-2017 and Nov-2022

Target values include
- Price
- Rating

The most impactful features will be the numeric-typed features
- acidity (float64) - 1-10 scale
- aroma (float64) - 1-10 scale
- body (float64) - 1-10 scale
- flavor (float64) - 1-10 scale
- aftertaste (float64) - 1-10 scale

There are several non-numeric features as well
- Blind assessments
- Notes
- Bottom Line

There are several biases noted on the website where the data was scraped from.  Firstly the ratings are skewed high.  This is due to the website's philosophy of focusing on the positive side of Coffee instead of highlighting those that are underperforming.  Another thing to note is that the bar for coffee standards have been rising.  The competition over producing the best coffee has driven producers to continue pushing the quality of their coffee causing an overall increase in rating.  Lastly, because coffeereviews.com is a critic website, they can expect to recieve a higher quality of samples for review.  These facts result in the majority of the data points being focused on the high end of the ratings.  This can lead to a situation where a predictor can become overly fit to match only the high end of the spectrum of coffee.

## Cleaning

The cleaning process included not only removing unneeded columns but also performing type conversions.  Non-numeric type values were converted into numeric type values for the purpose of regression.  Over 12 different currencies had to be converted to USD in order to for the data to be used accurately.  Metric and empyrical measurements had to be converted as well.

- Dates were converted from string to dateTime then to integer
- Prices and quantities were standardized.
  - These values were converted to USD/grams for the sake of comparison
  - Currency conversions were taken from Google Finance using rates from March 29, 2023
- Text portions of reviews were converted to numeric values using VADER lexicon-based sentiment analysis
  - Special symbols were removed
  - A polarity score was assigned to each text, representing negative or positive sentiment (-1 to 1)
- Redundant columns were dropped

## Models and Techniques

### Sentiment Analysis

Sentiment analysis will be performed using VADER, a lexicon-based analyzer.  Lexicon-based analyzers remove the need for greater context because they break down texts into individual tokens before they are processed.  Each token can then be analyzed indivdually without the need to understand it in the context it was given in.  This makes Lexicon-based analyzers a general solution for sentiment analysis without the worry of needing to understand the nuances behind the text being analyzed.

### Feature Reduction

In order to find the variables with the strongest correlations, a correlation heat map was generated.  This allows us to identify at a glance which of the features have a strong correlation to the label.  When these features are identified, the remaining features with little to no coreelation can be dropped, thus decreasing the overall complexity of the dataset.  In cases where there are many unrelated features, this step can result in more accurate predictors.


We find from the heatmap that the features with the strongest correlation to the rating are Aroma, Acid, Body, Flavor, and Aftertaste.  The rest of the features have negligible correlation to rating and can be discarded.  This includes the polarities of the text portions of the review.  They have little to no role in predicting the rating.

### Lasso Regression

Lasso Regression – A penalized regression method that is useful when dealing with a large number of features.  Lasso Regression Uses coefficients to decrease the effects that unrelated variables have on predicting the label. This can negatively impact accuracy in cases where coefficients are driven so low that the features no longer impact the label.  This may be a result of insufficient training, datasets with little correlation, or large outliers.

- Lasso Score: 0.02147
- Lasso Score (Reduced Features): -0.00655

The computed score for Lasso Regression, or the coefficient of determination, is the proportion of the label that can be predicted by the features.  The scored produced here are very low and provide no reliable predictability.  This shows that Lasso Regression is not a suitable model for this data.

### Ridge Regression

Ridge Regression - Another penalized regression method.

- Ridge Score: 0.99393
- Ridge Score (Reduced Features): 0.99995

### Decision Tree

- Decision Tree Score: 0.98373
- Decision Tree Score (Reduced Features): 0.99994

### Random Forest

- Random Forest Score: 0.98751
- Random Forest Score (Reduced Features): 0.99979

## Results

The predictor built using ridge regression proves to be the most accurate of the models with a near perfect accuracy once the features are reduced.  Using the predictor, a simulation was run using every single possible combination of feature values in order to determine which combination would produce the the highest rating.  It was found that a value of 10 for each feature produced a rating of 99.960235, which when rounded to the nearest integer, would be a rating of 100.

This is an interesting outcome due to the fact that features such as acidity and body are highly subjective.  I would not have assumed that a coffee with a high acidity rating would be the best rated option.  But this could also be an unintended consequence of having a skewed dataset.

Grouping the coffee by region also produces some insight into how the regions compare.  A box plot shows that Central America and South America produce coffee with some of the highest potential but also varies widely in quality while regions like Africa-Arabia and Hawaii are more consistent in quality.

The groupings also show that Hawaii produces coffee with the highest value.  This is likely due to the cost of property in Hawaii and the limitted real estate creating scarcity.

## Conclusions



## Future Work

## References
 
