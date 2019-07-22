
# list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]

list = [2,3,5,4,9,6]
li = []

def get_min(list):
    a = min(list)
    list.remove(a)
    li.append(a)
    if len(list) > 0:
        get_min(list)
    return li
li = get_min(list)
print(li)