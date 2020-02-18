# EDSA2020_Predict

## This repo contains our functions for doing some stuff to data:

## Function 4: Municipality & Hashtag Detector

Is a function which takes in a pandas dataframe and returns a modified dataframe that includes two new columns that contain information about the municipality and hashtag of the tweet.

**Function Specifications:**
* Function should take a pandas `dataframe` as input.
* Extract the municipality from a tweet using the `mun_dict` dictonary given below, and insert the result into a new column named `'municipality'` in the same dataframe.
* Use the entry `np.nan` when a municipality is not found.
* Extract a list of hashtags from a tweet into a new column named `'hashtags'` in the same dataframe.
* Use the entry `np.nan` when no hashtags are found.
```
