################################
# 파이썬 기본 - 함수
################################
# 기본형
def sum(a, b):
    return a + b
print( sum( 1, 2) )
# 가변인자
def sumEx( *params ):
    print( type(params) )
    tmp = 0
    for p in params:
        tmp += p
    return tmp

print( sumEx( 1,2,3,4,5,6,7,8,9 ) )

# 가변인자인데 리턴이 2개(하나는 누적합, 하나는 누적곱)
def sumEx2( *params ):
    tmp  = 0
    tmp2 = 1
    for p in params:
        tmp  += p
        tmp2 *= p
    return tmp, tmp2#, 10

# 함수의 리턴값을 1개 이상의 변수로 받고 있다면 
# 이함수는 무조건 튜플을 리턴하고 있다 (리턴값이 여러개다)
# 반드시 리턴의 개수만큼 변수를 같이 받아줘야 문제 없다
sum1, mul1 = sumEx2( 1,2,3,4,5,6,7,8,9 )
print( sum1, mul1 )    
# 하나로만 받으면 튜플 덩어리르 받는 것임 
sum1 = sumEx2( 1,2,3,4,5,6,7,8,9 )
print( sum1 )    

# 함수 인자 초기값 주기
def person(name, age, height=100):
    print( "name=%s, age=%s, height=%s" % (name, age, height) )

person("CEN",50, 10)
person("CEN2",30)
#person(name="CEN3",30)
# 함수의 기본값을 부여한 파라미터명을 함수 호출시 명시적으로 표현하여 설정할수 있다
person("CEN3",30, height=108)
#person(height=108, "CEN3",30)