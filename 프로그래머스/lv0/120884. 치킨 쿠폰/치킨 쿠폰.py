def solution(chicken):
    answer = -1
    # 최대 서비스 치킨의 수
    # 조건 : 서비스치킨에도 쿠폰 발급, 10장에 한마리
    # 반복횟수 지정 x
    service=0
    coupon = chicken
    while coupon//10:
        service+=(coupon//10)
        coupon = (coupon%10+coupon//10)
        print(coupon)
    return service