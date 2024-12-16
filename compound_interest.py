def calculate_compound_interest(principal: float, rate: float, times_compounded: int, years: int) -> float:
    """
    Calculate the compound interest based on the given principal, rate, times compounded per year, and number of years.

    :param principal: The initial amount of money.
    :param rate: The annual interest rate as a decimal.
    :param times_compounded: The number of times the interest is compounded per year.
    :param years: The number of years the money is invested or borrowed for.
    :return: The amount of money accumulated after n years, including interest.
    :raises ValueError: If any of the input values are invalid.
    """
    if principal < 0 or rate < 0 or times_compounded <= 0 or years < 0:
        raise ValueError("Inputs should be non-negative and times_compounded should be greater than zero.")
    
    try:
        amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)
    except TypeError:
        raise ValueError("Invalid input types.")
    
    return amount
