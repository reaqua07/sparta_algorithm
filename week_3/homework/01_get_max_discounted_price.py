# 최대로 많이 할인 받기
# 가장 비싼 가격을 가장 많은 할인율 적용 : 정렬해서 가장 큰 값을 구하면 되겠다!
# sort 함수 사용
shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# sort는 기본적으로 오름차순
# 큰 값이 먼저 필요하면 내림차순 정렬이 필요한데 이때는
# reverse 사용
def get_max_discounted_price(prices, coupons):
    # 내림차순 정렬
    prices.sort(reverse=True)
    coupons.sort(reverse=True)

    # 비교할 집합의 크기가 다르기 때문에 while과 index 사용
    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index])
        price_index += 1
        coupon_index += 1

    # 길이 차이가 나는 집합을 설정했기 때문에 길이가 긴쪽이 남을 수도 있다
    # 그러니까 한 번 더 돌려준다
    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1
    return max_discounted_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.