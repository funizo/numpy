import numpy as np
kor = np.array([90,70,80,100,85],dtype=int)
eng = np.array([70,80,90,40,95],dtype=int)
mat = np.array([50,70,80,70,65],dtype=int)

total = kor + eng + mat
print("학생별 총점:",total)
print("학생별 평균:",total/3)

korsum = np.sum(kor,axis=0)
print("국어총점:",korsum)
print("국어평균",korsum/5)

engsum = np.sum(eng,axis=0)
print("영어총점:",korsum)
print("영어평균",korsum/5)

matsum = np.sum(mat,axis=0)
print("수학총점:",korsum)
print("수학평균",korsum/5)


total.sort()
print(total)