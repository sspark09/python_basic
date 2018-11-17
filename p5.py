################################
# 파이썬 기본 - 딕셔너리 - {}
################################
# 순서X, 키:값 세트 , 키는 중복되면 않됨
# 값은 중복데이터 OK, 키의 타입 모가 되던 OK
# {}
################################
dic  = {}
dic2 = dict()
print( dic, dic2, type(dic) )
# 추가
dic['lan'] = 'python'
print( dic, len(dic) )
dic[0] = 'python'
print( dic, len(dic) )
# 인덱싱
print( dic[0] )
# 슬라이싱 => X
# 삭제
del dic['lan']
print( dic, len(dic) )
dic['web'] = 'flask'
print( dic.items() )
print( dic.keys() )
print( dic.values() )
print( '*'*80 )
######################################
# 반복문 for : 정해진 횟수를 돈다, 파이썬은 오직 for ~ each만 지원( for ~ in )
for key in dic.keys():
    print( 'key=%s, value=%s' % (key, dic[key]) )
for item in dic.items():
    print( type(item), len(item), item[0], item[1] )
# 굳이 인덱스를 쓰고 싶다면
# 2개 이상의 자료구조(순서가 존재하는)를 건드릴때 유용
for index, value in enumerate(dic.values()):
    print( index, value )






