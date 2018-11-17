################################
# 파이썬 기본 - 모듈화, 패키지
################################
'''
패키지=> /mod : 폴더 내부에는 하위 버전 호환을 위해 
               통상 __init__.py 파일을 생성해 둔다
모듈명=> a.py라면 a가 모듈명
        모듈의 이름을 정할때는 .가 이름에 포함되면 않된다!! 
        (포함되면 참조할때 패키지로 인식함)
참조하기
from 패키지(__init__.py가 존재할때) ~
from 모듈명 ~
from 패키지.모듈명 ~
from 패키지.패키지.모듈명 ~

from (패키지명.패키지명...)(모듈명) import 변수, 함수, 클레스, 모듈명 (as 별칭)
or
import 패키지명(모듈명) 함수, 변수, 클레스등등 하위로 내려갈수 있다 (as 별칭)
'''
# 패키지를 지칭하면 __init__.py가 대응된다 고로 __init__.py안에 있는 
# 변수, 함수, 클레스등등을 참조할수 있다
from a import PI1
print( PI1 )

# 패키지.모듈으로 타고 가서 해당 모듈의 변수, 함수, 클레스등등을 참조할수 있다
from a.a_sub import PI2
print( PI2 )

# b 패키지 밑에 있는 __init__.py가 대응된다 고로 __init__.py안에 있는 
# 변수, 함수, 클레스등등을 참조할수 있다
from a.b import PI3
print( PI3 )

# 패키지.패키지.모듈으로 타고 가서 해당 모듈의 변수, 함수, 클레스등등을 참조할수 있다
from a.b.b_sub import PI4
print( PI4 )

import a.b.b_sub as m1
print( m1.PI4 )

import a.b as m2
print( m2.PI3 )