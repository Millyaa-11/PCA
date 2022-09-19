import random


class stack_class:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
        return self.stack

    def pop(self):
        del self.stack[-1]
        return self.stack

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            print("Empty Stack")
        else:
            print("Stack is not empty")

    def size(self):
        print(len(self.stack))

    def contains(self, element):
        if element in self.stack:
            return True
        else:
            return False

    def get_stack(self):
        return self.stack


class valet_park:
    def __init__(self):
        self.stack_a = stack_class()
        self.stack_b = stack_class()

    def random_car(self):
        for i in range(3):
            random_plate = random.randint(100, 999)
            self.stack_a.push(random_plate)
            random_plate = random.randint(100, 999)
            self.stack_b.push(random_plate)

    def park(self):
        print("\nSoi A - Number of Cars : ", len(self.stack_a.get_stack()), "\nNo. Plates : ", self.stack_a.get_stack())
        print("\nSoi B - Number of Cars : ", len(self.stack_b.get_stack()), "\nNo. Plates : ", self.stack_b.get_stack())
        input_car = int(input("Enter car plate no. : "))
        soi = input("\nChoose soi A or soi B : ")
        if soi == "A":
            self.stack_a.push(input_car)
            print(self.stack_a.get_stack())
        if soi == "B":
            self.stack_b.push(input_car)
            print(self.stack_b.get_stack())

    def get_car(self):
        print("\nSoi A - Number of Cars : ", len(self.stack_a.get_stack()), "\nNo. Plates : ", self.stack_a.get_stack())
        print("\nSoi B - Number of Cars : ", len(self.stack_b.get_stack()), "\nNo. Plates : ", self.stack_b.get_stack())
        input_car = int(input("Enter car plate no. : "))
        for i in range (len(self.stack_a.get_stack())):
            if self.stack_a.contains(input_car) == True:
                if self.stack_a.peek() == input_car:
                    print("Your car has been taken out")
                    print("\nSoi A - Number of Cars : ", len(self.stack_a.get_stack()), "\nNo. Plates : ",
                          self.stack_a.get_stack())
                    print("\nSoi B - Number of Cars : ", len(self.stack_b.get_stack()), "\nNo. Plates : ",
                          self.stack_b.get_stack())
                    break
                else:
                    self.stack_b.push(self.stack_a.peek())
                    self.stack_a.pop()
            elif self.stack_b.contains(input_car) == True:
                if self.stack_b.peek() == input_car:
                    print("\nSoi A - Number of Cars : ", len(self.stack_a.get_stack()), "\nNo. Plates : ",
                          self.stack_a.get_stack())
                    print("\nSoi B - Number of Cars : ", len(self.stack_b.get_stack()), "\nNo. Plates : ",
                          self.stack_b.get_stack(), "\n")
                    break
                else:
                    self.stack_a.push(self.stack_b.peek())
                    self.stack_b.pop()


def start():
    choice = int(input("1 : Park \n2 : Retrieve\n"))
    var_valet = valet_park()
    var_valet.random_car()
    if choice == 1:
        var_valet.park()
    if choice == 2:
        var_valet.get_car()


start()
