################################
# 파이썬 기본 - 집합
################################
# 중복제거!!
# 정렬은 운이 좋으면!
a = [1,3,4,2,5,6,3,1,3,2]
print( a, type(a) )
b = set( a )
print( b, type(b) )
a = list( b )
print( a, type(a) )
###############################
# 합집합, 차집합(방향중요), 교집합
a = set( [1,3,5,7,9] )
b = set( [2,4,6,8,1] )
print( a.union(b) )
print( a.intersection(b) )
print( a.difference(b) )
print( b.difference(a) )
