################################
# 파이썬 기본 - 예외처리
################################
try:
    print("1")
except Exception as e: # 오류 나면 수행
    print("2", e)
else: # 오류가 없었으면 진입 => while, for에서도 사용 =>break가 없었으면 진입
    print("3")
finally:# 무조건 수행
    print("4")

try:
    print("1")
    1/0
except Exception as e: # 오류 나면 수행
    print("2", e)
else: # 오류가 없었으면 진입 => while, for에서도 사용 =>break가 없었으면 진입
    print("3")
finally:# 무조건 수행
    print("4")