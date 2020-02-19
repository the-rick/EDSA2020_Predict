# EDSA2020_Predict Team 16

## This repo contains our functions for doing some stuff to data:

# Usage:

```
pip install git+https://github.com/the-rick/EDSA2020_Predict/
```
```
import predictPackage as (whatever)
```
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

## Function 5: Number of Tweets per Day

This a function which calculates the number of tweets that were posted per day. 

**Function Specifications:**
- It should take a pandas dataframe as input.
- It should return a new dataframe, grouped by day, with the number of tweets for that day.
- The index of the new dataframe should be named `Date`, and the column of the new dataframe should be `'Tweets'`, corresponding to the date and number of tweets, respectively.
- The date should be formated as `yyyy-mm-dd`, and should be a datetime object. **Hint:** look up `pd.to_datetime` to see how to do this.

## Function 6: Word Splitter

This function splits the sentences in a dataframe's column into a list of the separate words. The created lists should be placed in a column named `'Split Tweets'` in the original dataframe. This is also known as [tokenization](https://www.geeksforgeeks.org/nlp-how-tokenizing-text-sentence-words-works/).

**Function Specifications:**
- It should take a pandas dataframe as an input.
- The dataframe should contain a column, named `'Tweets'`.
- The function should split the sentences in the `'Tweets'` into a list of seperate words, and place the result into a new column named `'Split Tweets'`. The resulting words must all be lowercase!
- The function should modify the input dataframe directly.
- The function should return the modified dataframe.

# Function 7: Stop Words

This function removes english stop words from a tweet.

**Function Specifications:**
- It should take a pandas dataframe as input.
- Should tokenise the sentences according to the definition in function 6. Note that function 6 **cannot be called within this function**.
- Should remove all stop words in the tokenised list. The stopwords are defined in the `stop_words_dict` variable defined at the top of this notebook.
- The resulting tokenised list should be placed in a column named `"Without Stop Words"`.
- The function should modify the input dataframe.
- The function should return the modified dataframe.

## More useful function to come keep watching
