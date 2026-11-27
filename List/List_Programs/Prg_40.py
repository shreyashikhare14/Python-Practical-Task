"""
40. Create a list and demonstrate all list methods.
"""

lst1 = input("Enter a List = ")
lst = list(map(int,lst1.split()))

while True :
    print("===========Methods List=============")
    print("1.append")
    print("2.extend")
    print("3.insert")
    print("4.remove")
    print("5.pop")
    print("6.clear")
    print("7.index")
    print("8.count")
    print("9.sort")
    print("10.reverse")
    print("11.copy")
    print("12. Exit")

    choice = int(input("Enter a choice = "))

    match choice :
        case 1:
            app_ele = int(input("Enter a element to add on list = "))
            lst.append(app_ele)

        case 2 :
            ele = input("Enter a Elemets to add on list = ")
            exte_ele = list(map(int,ele.split()))
            lst.extend(exte_ele)

        case 3:
            index_use = int(input("Enter a Index of the element = "))
        
            ele_inst = int(input("Enter a Element to add"))

            lst.insert(index_use,ele_inst)

        case 4:
            remove_lst = int(input("Enter a element to remove = "))
            lst.remove(remove_lst)

        case 5 :
            pop_index = int(input("Enter a index to pop = "))
            lst.pop(pop_index)

        case 6:
            lst.clear()

        case 7:
            lst_ele = int(input("Enter a Element = "))
            index_ele = lst.index(lst_ele)
            print("Element Index = ",index_ele)

        case 8:
            ele = int(input("Enter Element = "))
            count_ele = lst.count(ele)
            print("Element Count = ",count_ele)

        case 9:
            lst.sort()
            print("Sorted List = ",lst)

        case 10:
            lst.reverse()
            print("Reversed List = ",lst)

        case 11:
            new_lst = lst.copy()
            print("Copied List = ",new_lst)

        case 12:
            print("Program Exited")
            break

        case _ :
            print("Invalid choice! Please enter 1 to 12")
            
    print("Final List = ",lst)