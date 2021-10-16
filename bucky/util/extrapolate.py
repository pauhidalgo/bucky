"""Provides are version of xp.interp that will perform polynomial extrapolation for all OOB x values"""

from ..numerical_libs import sync_numerical_libs, xp


@sync_numerical_libs
def interp_extrap(x, x1, yp, order=2):
    """xp.interp function with polynomial extrapolation"""
    y = xp.interp(x, x1, yp)
    if xp.any(x > x1[-1]):
        p = xp.poly1d(xp.polyfit(x1[-order - 1 :], yp[-order - 1 :], order))
        y[x > x1[-1]] = p(x[x > x1[-1]])
    if xp.any(x < x1[0]):
        p = xp.poly1d(xp.polyfit(x1[: order + 1], yp[order + 1], order))
        y[x < x1[0]] = p(x[x < x1[0]])
    return y
