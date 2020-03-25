def vip_rule(count, prices):
    if prices >= 200:
        return 0.8 * prices
    if count >= 10:
        return 0.85 * prices
    return prices


def common_rule(count, prices):
    if prices >= 200:
        return 0.8 * prices
    return prices
