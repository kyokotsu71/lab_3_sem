#  Сортировка методом прочесывания

def CombSort(ls):
    n = len(ls)
    step = n
    while step > 1 or flag:
       if step > 1:
           step = int(step / 1.247331)
       flag, i = False, 0
       while i + step < n:
          if ls[i] > ls[i + step]:
              ls[i], ls[i + step] = ls[i + step], ls[i]
              flag = True
          i += step
    return ls


a = [1, 2, 4, 5, 3]
print(CombSort(a))

