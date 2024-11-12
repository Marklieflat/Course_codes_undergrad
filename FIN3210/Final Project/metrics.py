import numpy as np

def pearson_correlation(actual, predicted):
    """
    Return the Pearson correlation coefficient.

    Parameters:
    actual (array-like): The array of actual values.
    predicted (array-like): The array of predicted values.

    Returns:
    float: The Pearson Correlation value
    """
    actual, predicted = np.array(actual), np.array(predicted)
    actual_mean = np.mean(actual)
    predicted_mean = np.mean(predicted)
    numerator = np.sum((actual - actual_mean) * (predicted - predicted_mean))
    denominator = np.sqrt(np.sum((actual - actual_mean)**2) * np.sum((predicted - predicted_mean)**2))
    return numerator / denominator

def theil_u(actual, predicted):
    """
    Return the Theil-U coefficient.

    A Theil's U of 0 indicates a perfect forecast.  

    A Theil's U of 1 indicates that the forecast is no better than a naive forecast (i.e., using the last observed value as the next forecast). 

    A Theil's U less than 1 indicates that the forecast is better than a naive forecast.  

    A Theil's U greater than 1 indicates that the forecast is worse than a naive forecast

    Parameters:
    actual (array-like): The array of actual values.
    predicted (array-like): The array of predicted values.

    Returns:
    float: The Theil_U value
    """
    actual, predicted = np.array(actual), np.array(predicted)
    numerator = np.sqrt(np.mean((actual - predicted)**2))
    denominator = np.sqrt(np.mean(actual**2)) + np.sqrt(np.mean(predicted**2))
    return numerator / denominator

def mase(actual, predicted):
    """
    Calculate the Mean Absolute Scaled Error (MASE) for non-seasonal data.

    :param actual: Array of actual values.
    :param predicted: Array of predicted values.
    :return: MASE value.

    MASE < 1: If the MASE is less than 1, it indicates that the forecasting model performs better than the simple naive forecast (usually one-step lag). This suggests that the model has predictive value.

    MASE = 1: A MASE of 1 implies that the performance of the forecasting model is equivalent to that of the naive model. In other words, the model does no better or worse than simply predicting the last observed value.

    MASE > 1: When the MASE is greater than 1, it suggests that the model performs worse than the naive forecast. This could mean that the model is not suitable or needs improvement.

    MASE = 0: A MASE of 0 would indicate perfect predictions with no error, which is an ideal but rarely achievable scenario in practice.

    Closer to 0, the better: Generally, the closer the MASE is to 0, the more accurate the model. Lower values indicate higher accuracy and a better fit to the actual data.
    """
    actual, predicted = np.array(actual), np.array(predicted)

    # Calculate the Mean Absolute Error (MAE) of the forecast
    mae_forecast = np.mean(np.abs(predicted - actual))

    # Calculate the Mean Absolute Error of the naive forecast (one-step lag)
    mae_naive = np.mean(np.abs(actual[1:] - actual[:-1]))

    # Calculate MASE
    return mae_forecast / mae_naive
