#-*- coding:utf-8 -*-
#合并两个有序列表
#采用尾递归
#solution One
def _recursion_merge_sort2(l1, l2, tmp):
    if len(l1) == 0 or len(l2) == 0:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return _recursion_merge_sort2(l1, l2, tmp)

def recursion_merge_sort2(l1, l2):
    return _recursion_merge_sort2(l1, l2, [])


list1 = [1, 2, 3, 4, 5]
list2 = [6, 4, 2, 1, 7]
list3 = recursion_merge_sort2(list1, list2)

print (list3)

#solution two
def loop_merge_sort(l1, l2):
    tmp = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
    tmp.extend(l1)
    tmp.extend(l2)
    return tmp

list4 = [1, 2, 3, 4, 5]
list5 = [6, 4, 2, 1, 7]
list6 = loop_merge_sort(list1, list2)

print list6
