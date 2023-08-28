
list_test = [4, 7, 11, 15, 3]


def sort_list(list, sort_method):   # --sort method is only 'ascend' or 'descend'(Bubble Sort)

    high_idx = len(list) - 1
    lst_change = False

    if sort_method == "ascend":
        for i in range(high_idx):
            for j in range(high_idx):
                item = list[j]
                next = list[j + 1]

                if item > next:
                    list[j] = next
                    list[j + 1] = item
                    lst_change = True
                print(list, i, j)
            print(lst_change)

            if lst_change == False:
                break

    if sort_method == "descend":
        for i in range(high_idx):
            for j in range(high_idx):
                item = list[j]
                next = list[j + 1]

                if item < next:
                    list[j] = next
                    list[j + 1] = item
                    lst_change = True
                    print(list, i, j)
            print(lst_change)

            if lst_change == False:
                break


sort_list(list_test, "ascend")
print()
print("  === Seperator === ")
print()
sort_list(list_test, "descend")
