################################
# 파이썬 기본 - 리스트 : []
################################
'''
- 순서가 있다. 값은 중복되도 상관 없다
- []
- 타언어에 배열로 연상해도 ok
'''
a = []
b = list()
print( a, b, type(a) )
a.append('cat')
print( a )
a.append(1)
# 리스트의 구성원들의 타입이 같을 필요 없다
print( a )
# append()는 무조건 마지막 맴버로 추가
a.append( b )
a.append( b[:] )
print( a )
# b는 같은 참조를 가르킨다
b.append( 2 )
print( a, b )
# ['cat', 1, [2], []] [2]
c = [5,6,7]
# 리스트 합하기
print( a + c )
print( a )
print( a.extend(c) )
print( a )
# 인덱싱
print( '*'*80 )
print( a[0] )
# 슬라이싱
print( a[:3] )
# 삭제
print( a, len(a) )
del a[1]
print( a, len(a) )
a.remove('cat')
print( a, len(a) )
del a[:]
print( a, len(a) )
# 정렬
a = [4,2,5,6,34,2,4]
a.sort()
print( a )