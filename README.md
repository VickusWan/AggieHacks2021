# AggieHacks2021

Deck slides: https://docs.google.com/presentation/d/1dXoqQfLIBY66v7o4s0BDbizG7YuGZowVm1V1v7hm0ss/edit?usp=sharing

The purpose of this project is to model the effect of the pandemic on the number of homeless people, specifically in California. For this Hackathon, the process can be broken down into the following steps

1. Understanding the driving factors
2. Research appropriate and relevant datasets
3. Data cleaning and EDA
4. Statistical Analysis
5. Feature Engineering
6. Regression

## Understanding driving factors

According to a report done by the National league of Cities (NLC) (1), there are 5 distinct driving factors for homeless people. Though the root cause is extremely complex, the common factors that come up, can be categorized as:

- House Affordability
- Income Stagnation
- Racial Disparities
- Mental Health and Substance Use
- Domestic Violence

## Data Interpolation

Because the dataset has been pulled from different sources, the time period for each variable is not consistent; some variables are monthly, quarterly or yearly. In this case, the monthly period time is selected.

Furthermore, we interpolated data from the annual data onto the monthly, in order to fill the gaps in-between.

![](https://github.com/VickusWan/AggieHacks2021/blob/main/img/noInterpolate.PNG)

![](https://github.com/VickusWan/AggieHacks2021/blob/main/img/withinterpolate.PNG)

## Data Extrapolation

To measure the effect of the pandemic on the number of homeless people, we extrapolated values for 2020 based on values for 2019. This leads to 2 different models: model with pandemic and without pandemic.

![](https://github.com/VickusWan/AggieHacks2021/blob/main/img/homelesss.PNG)

As shown, based on our regression analysis, the pandemic has led to an increase in homeless people, for the state of California.







links: (1) - https://www.nlc.org/wp-content/uploads/2021/02/UnlockingHomelessnessReportPart1.pdf
