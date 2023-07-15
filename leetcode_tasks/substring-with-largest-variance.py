from collections import Counter

def main():
    test_str = "substring-with-largest-variance"
    
    substring_with_largest_variance(test_str)
    
def substring_with_largest_variance(str):
    variance = []
           
    list_values = list(map(lambda k : k[0],filter(lambda key_val : key_val[1] >= 2, Counter(str).most_common())))
    
    print(list_values)
    
    return variance
    


if __name__ == "__main__":
    main()