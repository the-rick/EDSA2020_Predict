from predictpackage import metricsPackage

def dictionary_of_metrics(items):
    """
    make sure dictionary_of_metrics works correctly
    """

    assert metricsPackage.dictionary_of_metrics([39660.0, 36024.0, 32127.0, 39488.0, 18422.0, 23532.0, 8842.0, 37416.0, 16156.0, 18730.0, 19261.0, 25275.0]) == [8, 7, 4], 'incorrect'

def date_parser(dates):
    """
    make sure date_parser works correctly
    """

    assert date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29'], 'incorrect'