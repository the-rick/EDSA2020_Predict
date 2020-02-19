from predictpackage import metricsPackage

# Function 1
def dictionary_of_metrics(items):
    """
    make sure dictionary_of_metrics works correctly
    """

    assert metricsPackage.dictionary_of_metrics([39660.0, 36024.0, 32127.0, 39488.0, 18422.0, 23532.0, 8842.0, 37416.0, 16156.0, 18730.0, 19261.0, 25275.0]) == {'mean': 26244.42,'median': 24403.5,'var': 108160153.17,'std': 10400.01,'min': 8842.0,'max': 39660.0}, 'incorrect'

# Function 2
def five_num_summary(items):
    """
    make sure five_num-summary works correctly
    """
    assert five_num_summary([39660.0, 36024.0, 32127.0, 39488.0, 18422.0, 23532.0, 8842.0, 37416.0, 16156.0, 18730.0, 19261.0, 25275.0])=={'max': 39660.0,'median': 24403.5,'min': 8842.0,'q1': 18653.0,'q3': 36372.0}, 'incorrect'

# Function 3
def date_parser(dates):
    """
    make sure date_parser works correctly
    """

    assert date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29'], 'incorrect'

