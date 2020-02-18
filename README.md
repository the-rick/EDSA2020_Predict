# EDSA2020_Predict

## This repo contains our functions for doing some stuff to data:

## Function 1: Metric Dictionary

This is a function that calculates the mean, median, variance, standard deviation, minimum and maximum of of list of items. You can assume the given list is contains only numerical entries, and you may use numpy functions to do this.

**Function Specifications:**
- Function should allow a list as input.
- It should return a `dict` with keys `'mean'`, `'median'`, `'std'`, `'var'`, `'min'`, and `'max'`, corresponding to the mean, median, standard deviation, variance, minimum and maximum of the input list, respectively.
- The standard deviation and variance values must be unbiased. **Hint:** use the `ddof` parameter in the corresponding numpy functions!
- All values in the returned `dict` should be rounded to 2 decimal places.

## Function 2: Five Number Summary

This a function which takes in a list of integers and returns a dictionary of the [five number summary.](https://www.statisticshowto.datasciencecentral.com/how-to-find-a-five-number-summary-in-statistics/).

**Function Specifications:**
- The function should take a list as input.
- The function should return a `dict` with keys `'max'`, `'median'`, `'min'`, `'q1'`, and `'q3'` corresponding to the maximum, median, minimum, first quartile and third quartile, respectively. You may use numpy functions to aid in your calculations.
- All numerical values should be rounded to two decimal places.

## Function 3: Date Parser

```
dates[:3] == [
    '2019-11-29 12:50:54',
    '2019-11-29 12:46:53',
    '2019-11-29 12:46:10'
]
```

This is a function that takes as input a list of these datetime strings and returns only the date in `'yyyy-mm-dd'` format.

**Function Specifications:**
- The function should take a list of strings as input.
- Each string in the input list is formatted as `'yyyy-mm-dd hh:mm:ss'`.
- The function should return a list of strings where each element in the returned list contains only the date in the `'yyyy-mm-dd'` format.

## Function 4: Municipality & Hashtag Detector

Is a function which takes in a pandas dataframe and returns a modified dataframe that includes two new columns that contain information about the municipality and hashtag of the tweet.

**Function Specifications:**
* Function should take a pandas `dataframe` as input.
* Extract the municipality from a tweet using the `mun_dict` dictonary given below, and insert the result into a new column named `'municipality'` in the same dataframe.
* Use the entry `np.nan` when a municipality is not found.
* Extract a list of hashtags from a tweet into a new column named `'hashtags'` in the same dataframe.
* Use the entry `np.nan` when no hashtags are found.
```
