from decimal import ROUND_DOWN, Decimal, getcontext


def truncate(x, d: int = 2):
    getcontext().prec = d + 10
    if isinstance(x, Decimal):
        x = float(x)
    fator = Decimal(10) ** d
    if str(x)[::-1].find('.') > 2:
        try:
            return float((Decimal(x) * fator).to_integral_value(rounding=ROUND_DOWN) / fator)
        except Exception:
            return int(x * (10.0**d)) / (10.0**d)
    return x
