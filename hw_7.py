# 1

def chop(list1):
  list1.remove(list1[0])
  list1.pop()
  return None

def middle(list1):
  list1 = list1[1:-1]
  return list1

list1 = [1, 2, 3, 4]

print("my list before call chop function =>", list1)
chop(list1)
print("my list after call chop function =>", list1)

list1 = [1, 2, 3, 4]
print("my list before call middle function =>", list1)
middle(list1)
print("my list after call middle function =>", list1)

list1 = middle(list1)

print("new list after call middle function =>", list1)

# 2


with open("romeo.txt", "r") as file:
    list1 = []
    for i in file:
        i = i.split()
        for word in i:
            if word not in list1:
                list1.append(word)
    list = sorted(list1)
    print(list1)
    
        
# 3

with open("mbox.txt", "r") as file:
    
    count = 0
    for i in file:
        if i.startswith("From:"):
            i = i.replace("From:", "")
            print(i.rstrip())
            count += 1
    print("Total %d lines were printed" %count)

# 4

list1 = []

while True:
    try:
        num_input = input("Please enter an integer: ")
        if num_input == "done":
            print("---------- Bye !! --------------")
            break
        else:
            num_input = int(num_input)
            list1.append(num_input)
            total = 0
            count = 0
            for num_input in list1:
                total += num_input
                count += 1
                
            average = total / count
            print(list1,", average = ", average)
    except ValueError:
        print("Please, enter numeric value!")



