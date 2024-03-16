import random
class RandomInList(list):
    def __init__(self, count):
        super().__init__()
        self.count = count
        self.getList()

    def getList(self):
        for i in range(self.count):
            rand_int = random.randint(1, 100)
            self.append(rand_int)

    def getCount(self):
        return self.count

    def getTotal(self):
        return sum(self)

    def getAverage(self):
        return sum(self) / self.count

    def __str__(self):
        return ", ".join(str(i) for i in self)


def main():
    print("Random Integer List")
    print()
    while True:
        try:
            num_int = int(input("How many random integers should the list contain?: "))
            if num_int > 0:
                break
            else:
                print("Enter a positive integer")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    while True:
        print()
        print("Random Integers")
        print("=" * 16)
        int_list = RandomInList(num_int)
        print(f"Integers: {int_list}")
        print(f"Count:   {int_list.getCount()}")
        print(f"Total:   {int_list.getTotal()}")
        print(f"Average: {int_list.getAverage()}")
        print()
        choice = str(input("Continue? (y/n): "))
        while choice.lower() != "y" and choice.lower() != "n":
            print("Invalid input. Please enter y or n.")
            choice = str(input("Continue? (y/n):"))
        if choice.lower() == "n":
            break
    print()
    print("Bye!")
main()




