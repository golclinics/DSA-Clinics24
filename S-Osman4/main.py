from fizzbuzz import fizzbuzz

fizzbuzz = __import__('fizzbuzz').fizzbuzz

def run_fizzbuzz():
    """
    Run FizzBuzz function
    """
    fizzbuzz()

if __name__ == "__main__":
    run_fizzbuzz()
