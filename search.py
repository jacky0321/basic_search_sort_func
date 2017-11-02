#-*-coding:utf-8-*-
def binarysearch(item, l):
    start = 0
    stop = len(l) - 1
    flag = False
    while start <= stop and not flag:
        mid = (start + stop)//2

        if l[mid] == item:
            flag = True
        elif l[mid] < item:
            start = mid + 1
        else:
            stop = mid - 1

    return flag


def binarysearch(item, l):
    if len(l) == 0:
        return False

    mid = len(l) //2

    if l[mid] == item:
        return True
    elif l[mid] < item:
        return binarysearch(item, l[mid+1:])
    else:
        return binarysearch(item, l[:mid]) 

    
'''
1、散列函数：
    (1)取余
    (2)分组取余
    (3)平方区中取余
    (4)字符串：reduce(lambda x,y:x+y, map(lambda x:ord(x), l))
2、冲突解决：
    (1)线性探测
    (2)再散列
    (3)二次探测法
    (4)数据链

'''

if __name__ == '__main__':
    l = [1,10,-11,4,5,1000,7,80,9]
    l.sort()
    print(l)
    print(binarysearch(90, l))
    print(binarysearch(1000, l))
