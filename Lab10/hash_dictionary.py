small = (open("small.txt")).read().split(" ")
small_dict = []
for i in small:
    small_dict.append(i)

full = (open("full.txt")).read().split(" ")
full_dict = []
for i in full:
    full_dict.append(i)

class Node:
    def __init__(self, key, word):
        self.key = key
        self.word = word
        self.next = None
        self.data = (key, word)


class HASHTABLE:
    def __init__(self, dicts):
        self.hash_table = []
        self.hash_lst = []
        self.entry = 0
        self.size = self.prime(len(dicts) // 5)
        self.dicts = dicts
        self.head = None
        self.load = 0
        self.expand = 0
        self.collision = 0

    def hash(self, st):
        h = 0
        for ch in st:
            h *= 37
            h += ord(ch)
        return h

    def prime(self, n):
        if n > 1:
            for i in range(2, int(n / 2) + 1):
                if n % i == 0:
                    return self.prime(n + 1)
        return n

    def hash_st(self, dicts):
        prime_size = self.prime(len(dicts) // 5)
        for i in range(len(dicts)):
            self.hash_lst.append((self.hash(dicts[i]) % prime_size, dicts[i]))
        return self.hash_lst

    def add(self, key, word):
        num = Node(key, word)
        num.next = self.head
        self.head = num

    def separate(self, dicts):
        for x in range(len(self.hash_lst)):
            self.hash_table.append("")
        for x in range(len(self.hash_lst)):
            self.entry += 1
            if self.entry > self.size:
                self.clear()
                self.entry = 0
                self.size = self.prime(self.size * 2)
                self.expand += 1
                self.separate(dicts)
                break

            if self.hash_table[self.hash_lst[x][0]] == "":
                self.head = Node(self.hash_lst[x][0], dicts[x])
                self.hash_table[self.hash_lst[x][0]] = Node(self.hash_lst[x][0], dicts[x])
            else:
                self.collision += 1
                cur = self.hash_table[self.hash_lst[x][0]]
                while cur.next is not None:
                    cur = cur.next
                    self.head = cur
                new = Node(self.hash_lst[x][0], self.hash_lst[x][1])
                cur.next = new
            self.load = self.entry / self.size
        return [self.expand, self.load, self.collision]

    def clear(self):
        self.hash_table = []
        return self.hash_table

    def print_separate(self):
        longest = 0
        for x in self.hash_table:
            sep_table_list = []
            if x != "":
                while x.next is not None:
                    sep_table_list.append(x.data)
                    x = x.next
                sep_table_list.append(x.data)
                print(sep_table_list)
            else:
                sep_table_list.append(x)
                print(sep_table_list)
            count = len(sep_table_list)
            if longest < count:
                longest = count
        return longest

    def linear(self, dicts):
        for x in range(len(self.hash_lst)):
            self.hash_table.append("")
        for x in range(len(self.hash_lst)):
            self.entry += 1
            if self.entry > self.size:
                self.clear()
                self.entry = 0
                self.size = self.prime(self.size * 2)
                self.expand += 1
                self.linear(dicts)
                return
            if self.hash_table[self.hash_lst[x][0]] == "":
                self.hash_table[self.hash_lst[x][0]] = self.hash_lst[x]
            else:
                self.collision += 1
                p = 1
                while self.hash_table[self.hash_lst[x][0] + p] != "":
                    p += 1
                self.hash_table[self.hash_lst[x][0] + p] = self.hash_lst[x]

    def print_linear(self):
        for x in range(len(self.hash_table)):
            print(x, " : ", self.hash_table[x])

    def check(self, input_word, dicts):
        prime_size = self.prime(len(dicts) // 5)
        index = self.hash(input_word) % prime_size
        if self.hash_table[index][1] == input_word:
            return True
        else:
            p = 1
            while self.hash_table[index + p][1] != input_word:
                p += 1
                if p + index >= len(self.hash_table):
                    return False
            return True


def start():
    dict_choice = str(input("s : small dict\nf : full dict\n"))
    collision_choice = str(input("se : separate chaining\nl : linear probing\n"))
    if dict_choice == "s":
        hash_dict = HASHTABLE(small_dict)
        hash_dict.hash_st(small_dict)
        if collision_choice == "se":
            hash_dict.separate(small_dict)
            expands = hash_dict.separate(small_dict)[0]
            loads = hash_dict.separate(small_dict)[1]
            collisions = hash_dict.separate(small_dict)[2]
            print("Longest Collisions : ", hash_dict.print_separate())
            print("Total words : ", len(small_dict))
            print("Collision resolution : ", collisions)
            print("Expands : ", expands)
            print("Loads : ", loads)
        if collision_choice == "l":
            hash_dict.linear(small_dict)
            hash_dict.print_linear()
            check_word = str(input("Check Spelling - Input word : "))
            print(hash_dict.check(check_word, small_dict))
    elif dict_choice == "f":
        hash_dict = HASHTABLE(full_dict)
        hash_dict.hash_st(full_dict)
        if collision_choice == "se":
            hash_dict.separate(full_dict)
            expands = hash_dict.separate(full_dict)[0]
            loads = hash_dict.separate(full_dict)[1]
            collisions = hash_dict.separate(full_dict)[2]
            print("Longest Collisions : ", hash_dict.print_separate())
            print("Total words : ", len(full_dict))
            print("Collision resolution : ", collisions)
            print("Expands : ", expands)
            print("Loads : ", loads)
        if collision_choice == "l":
            hash_dict.linear(full_dict)
            hash_dict.print_linear()
            check_word = str(input("Check Spelling - Input word : "))
            print(hash_dict.check(check_word, full_dict))


start()
