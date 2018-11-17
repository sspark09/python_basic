################################
# 파이썬 기본 - 문자열
################################
# 문자열을 표현하는 방법
# 한줄 표현   : ', ", ''' ''',  """ """
# 여러줄 표현 : ''' ''',  """ """
################################
# ''' ''',  """ """ : 여러줄표현, 구조를 유지, 주석용 사용
################################
a = 'hi'
print( a, type(a) )
# 문자열 더하기
b = "hello"
print( a + b )
# 인덱싱 => 연속 데이터에서 하나 값을 획득 하는 방식 => 차원축소의미를 가짐
# 기호 : 변수명[인덱스(0부터출발)]
c = "hello world"
# e 출력 : 정방향 탐색(앞에서부터)
print( c[1] )
# d 출력 : 역방향 탐색(뒤에서부터)
print( c[-1] )
# 슬라이싱 => 데이터를 범위내로 자르기 => 차원유지
# 문법 : 변수명[시작인덱스:끝인덱스:setp(생략되면1)]
# llo를 출력하시오
# 끝인덱스의 경계값으로만 사용되고 앞까지만 포함된다 (정방향)
print( "["+c[2:5]+"]" )
# 앞뒤로 하나씩 잘르시오
# ello worl
print( "["+c[1:-1]+"]" )
# 처음부터 5번재 가지
print( c[:5] )
# 원본 복사
print( c[:] )
# 포멧팅
# 타입을 정확하게 기재
print( "%d + %d = %d" % (1,2,3) )
# 타입을 모르겟다, 그냥 무난하게 문제 없이 갔으면 좋겟다
print( "%s + %s = %s" % (1,2,3) )
# 명확하게 포멧팅을 세팅하고 싶다 혹은 %도 표현해야 해서 복잡하다. 인덱스로 처리
print( "{0} + {1} = {2}".format(1,2,3) )
print( "{x} + {y} = {sum}".format(y=2, x=1, sum=3) )








