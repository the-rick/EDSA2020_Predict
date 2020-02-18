def dictionary_of_metrics(items):
    # your code here
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
