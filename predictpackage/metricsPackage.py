#Function 1

def dictionary_of_metrics(items):
    """ 
    Returns a dictionary of metrics (mean, median, variance, standard deviation, minimum and maximum)
    
    Example output: 
    gauteng: List of values
    dictionary_of_metrics(gauteng) == {'mean': 26244.42,
                                       'median': 24403.5,
                                       'var': 108160153.17,
                                       'std': 10400.01,
                                       'min': 8842.0,
                                       'max': 39660.0}
    """

    def find_mean(items):
        denominator = int()
        for item in items:
            denominator += item
        return denominator / len(items)

    def find_median(items):
        if len(items) % 2 != 0:
            sorted_values = sorted(items)
            position = round(len(items) / 2.1)
            return sorted_values[position]
        else:
            sorted_values = sorted(items)
            position1 = int((len(sorted_values) / 2) - 1)
            position2 = int((len(sorted_values) / 2))
            return (sorted_values[position1] + sorted_values[position2]) / 2

    def find_variance(items):
        step1 = 0
        step2 = 0
        for i in items:
            step1 += i
        step1 = (step1**2)/len(items)
        for i in items:
            step2 += i**2
        variance = (step2-step1)/(len(items)-1)
        return round(variance, 2)

    def find_std(items):
        std_deviation = find_variance(items)
        return round(std_deviation**(1/2), 2)

    def find_maximum(items):
        return sorted(items)[-1]

    def find_minimum(items):
        return sorted(items)[0]


    return {'mean': round(find_mean(items), 2),
            'median': round(find_median(items), 2),
            'var': round(find_variance(items), 2),
            'std': round(find_std(items), 2),
            'min': round(find_minimum(items), 2),
            'max': round(find_maximum(items), 2)
           }

# Function 3

def date_parser(dates):
    """
         Returns a list of strings, in the format 'yyyy-mm-dd'
     Args:
         a list of strings in the format 'yyyy-mm-dd hh:mm:ss'
     Returns:
         a list of strings
     Example:
         >>>date_parser(dates[:3])
         ['2019-11-29', '2019-11-29', '2019-11-29']
    """
#create a new list that has split items, dates split from time stamps
    no_time=[dt.split()[0] for dt in dates]
    return no_time

# Function 4

def extract_municipality_hashtags(df):
    """"
     Args:
         pandas dataframe 
     Returns:
         returns a modified dataframe that includes two new columns that contain information 
           about the municipality and hashtag of the twee
    
     Example Output:
        Tweets	Date	municipality	hashtags
        0	@BongaDlulane Please send an email to mediades...	2019-11-29 12:50:54	NaN	NaN
        1	@saucy_mamiie Pls log a call on 0860037566	2019-11-29 12:46:53	NaN	NaN
        2	@BongaDlulane Query escalated to media desk.	2019-11-29 12:46:10	NaN	NaN
        3	Before leaving the office this afternoon, head...	2019-11-29 12:33:36	NaN	NaN
        4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	2019-11-29 12:17:43	NaN	[#eskomfreestate, #mediastatement]
    """"
    
    def mun_func(df):
        muns = []
        for d_ in mun_dict.keys():
            muns.append(d_)
        for item in muns:
            if item in df:
                return mun_dict[item]
            else:
                return np.nan
    
    def hash_tags(df):

        hash_words = []
        search_value = '#'
        
        if search_value in df:
            hash_words.append(df.split())
            hash_tags = []
            for tag in hash_words[0]:
                if search_value in tag:
                    hash_tags.append(tag.lower())
            return hash_tags    
        
        else:
            return np.nan

        df['municipality'] = df['Tweets'].apply(lambda y: mun_func(y))
        df['hashtags'] = df['Tweets'].apply(lambda y: hash_tags(y))
        
        ret = df[['Tweets', 'Date', 'municipality', 'hashtags']]
    
    return ret

# Function 5 

def number_of_tweets_per_day(df):
    """
     Returns a dataframe of the number of tweets per date
     Args:
         A dataframe with Tweets column and a dates column in the format 'yyyy-mm-dd hh:mm:ss'
     Returns:
         A dataframe with number of tweets per day, with date in the format 'yyyy-mm-dd'
    
    """
    df['Date'] = date_parser(df['Date'])
    df = df.groupby('Date').count()
    return df

# Function 6

def word_splitter(df):
    """
     a function which splits the sentences in a dataframe's column into a list of the separate words.
     Args:
       pandas dataframe
     Returns:
       returns a modified dataframe with new column named 'Split Tweets'
    """
    nwe_col = [i.split() for i in df['Tweets']]
    df["Split Tweets"] = nwe_col
    return df

# Function 7

def stop_words_remover(df):
    """
     a function which removes english stop words from a tweet.
     Args:
         pandas dataframe 
     Returns:
         returns a modified dataframe 'without stopwords'
    
     Example Output:
           ['@BongaDlulane', 'Please', 'send', 'an', 'email', 'to', 'mediades@eskom.co.za']
           ['@bongadlulane', 'send', 'email', 'mediadesk@eskom.co.za']
    """
    
    df['Without Stop Words'] = df['Tweets'].apply(lambda func: func.lower().split())
#     print(df['Without Stop Words'].head())
    for stop_words in stop_words_dict.values():
#         print(stop_words)
        for word in stop_words:
            if df['Without Stop Words'].str.contains(word).all():
#                 print("I found a stop word "  '('+word+')')
#                 continue
                df['Without Stop Words'] = df['Without Stop Words'].apply(lambda x: ' '.join([word for word in x if word not in (stop_words)]))
            
    df['Without Stop Words'] = df['Without Stop Words'].map(lambda tweet: tweet.split())
    return df

