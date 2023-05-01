# Nicholas_data606
My UMBC Capstone project

## Abstract

## Introduction

Coffee is a popular drink worldwide and as a result is a large global industry. The coffee industry is estimated to be valued in the hundreds of billions of dollars and every day alone, more than 2 billion cups of coffee are consumed. With no shortage of demand, such a large industry can be an opportunity to analyze consumer trends for the purposes of maximizing profits. This project seeks to take a look at coffee reviews from the website https://www.coffeereview.com/ in order to determine what characteristics are most favored by consumers and how these can be used to develop coffee in the future to increase profits.

## Objectives

Goal: Analyze the reviews of a wide variety of coffees from around to world in an attempt to create a coffee with the highest rating.
In order to accomplish this goal, There are several angles that can be explored:

• What aspects of coffee have the largest impact on rating and price?

• Which regions produce the best coffee?

• Does price and rating have a correlation?

I will use the data to train a model to predict the rating of a coffee given a review, and use this model with a maximiztion function to determine the values for each feature that will maximize the rating.

## Dataset

The dataset being used for this project was found on Kaggle and was created by scraping the website www.coffeereviews.com for reviews between the dates Dec-2017 and Nov-2022

Target values include
• Price

• Rating

The most impactful features will be the numeric-typed features
• acidity (float64) - 1-10 scale

• aroma (float64) - 1-10 scale

• body (float64) - 1-10 scale

• flavor (float64) - 1-10 scale

• aftertaste (float64) - 1-10 scale

There are several non-numeric features as well
• Blind assessments

• Notes

• Bottom Line

There are several biases noted on the website where the data was scraped from.  Firstly the ratings are skewed high.  This is due to the website's philosophy of focusing on the positive side of Coffee instead of highlighting those that are underperforming.  Another thing to note is that the bar for coffee standards have been rising.  The competition over producing the best coffee has driven producers to continue pushing the quality of their coffee causing an overall increase in rating.  Lastly, because coffeereviews.com is a critic website, they can expect to recieve a higher quality of samples for review.  These facts result in the majority of the data points being focused on the high end of the ratings.  This can lead to a situation where a predictor can become overly fit to match only the high end of the spectrum of coffee.

## Cleaning

## Models and Techniques

### Lasso Regression

### Ridge Regression

### Decision Tree

### Random Forest

### Sentiment Analysis

## Conclusions

## Future Work

## References

