
def integrate(fun, x1, x2, intervals=1):
    """Compute the integral of fun from x1 to x2 using Simpson's rule.

    Arguments:
        fun - a function with one real argument that returns a real value.
        x1  - starting value of interval for integration (left endpoint)
        x2  - ending value for interval for integration (right endpoint)
        intervals - number of sub-intervals to use with Simpson's rule.
              Default is 1 sub-interval.
    Returns:
        (float) numerical approximation to the integral of fun from x1 to x2.

    Example:
    >>> def fun(x): return x+2
    >>> integrate(fun, 0, 1)
    2.5
    """

    # Do NOT write this code until AFTER you write the unit tests.
    h = (x2 - x1) / 2
    s = fun(x1) + fun(x2)
    for i in range(1, intervals):
        s = s + 4 * fun(x1+i*h)
    for j in range(1, intervals):
        s = s + 2 * fun(x1+j*h)
    return h/3 * s