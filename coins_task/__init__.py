__version__ = '0.1.0'

def split_on_coins(total: int, coins: list[int]) ->list[int]:
    """generate coins return with minimal amount of coins

    Args:
        total (int): total sum of return
        coins (list[int]): type of coins

    Returns:
        list[int]: returns all coins to return
    """
    to_ret = []
    for coin in sorted(coins, reverse=True):
        amount = total // coin
        total -= amount * coin
        to_ret += [coin] * amount
    return to_ret
    