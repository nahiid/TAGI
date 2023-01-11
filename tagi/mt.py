"""Metric for performance evaluation"""
import math
import statistics


def compute_error(y, ypred):
    """This function calculates the Root Mean Square Error (RMSE). It takes as input
    two vectors (or matrices) with one containing the real \eqn{y}'s and the other the
    predicted \eqn{y}'s from the model.
    Args:
        y: Response data
        ypred: Mean of predicted responses
    Returns:
        RMSE for the given data
    """
    e = math.sqrt(statistics.mean((y - ypred) ^ 2))
    return e


def log_lik(y, ypred, vpred):
    """Compute log-likelihood
    This function calculates the log-likelihood (LL). It takes as input
    three vectors (or matrices) with one containing the real \eqn{y}'s, one with the
    predicted \eqn{y}'s from the model and the last one with the variance of the \eqn{y}'s.
    Args:
        y: Response data
        ypred: Mean of predicted responses
        Vpred: Variance of the predicted responses
    Returns:
        LL for the given data
    """
    d = len(y)  # unsure
    if d == 1:
        ll = statistics.mean(
            (-0.5 * math.log(2 * math.pi * vpred)) - (0.5 * (y - ypred) ^ 2) / vpred
        )
    return ll
