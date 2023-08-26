from Array import Array 

numbers = Array(5)


def main():
    numbers.insert(1)
    numbers.insert(2)
    numbers.insert(3)
    numbers.removeAt(0)
    numbers.print()
    print(numbers.indexOf(2))
    
if __name__ == "__main__":
    main()