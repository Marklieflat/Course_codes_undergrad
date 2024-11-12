import pandas as pd
import pywt
import numpy as np

def denoise_factors_with_wavelet(df, factors, wavelet='haar'):
    '''
    Denoise the factors using wavelet transform.
    :param df: DataFrame containing the factors to denoise.
    :param factors: List of factors to denoise.
    :param wavelet: The wavelet to use, default is 'haar'.
    :return: DataFrame containing the denoised factors.
    '''
    def thresholding(data, thresh):
        return pywt.threshold(data, thresh, mode='soft')

    denoised_data = {}

    for factor in factors:
        # Ensure no NA values before wavelet transform
        time_series = df[factor].values
        # Perform Wavelet Decomposition
        coeffs = pywt.wavedec(time_series, wavelet, level=2)
        cA2, cD2, cD1 = coeffs
        # Threshold the detail coefficients
        cD2 = thresholding(cD2, np.std(cD2)/2)
        cD1 = thresholding(cD1, np.std(cD1)/2)
        # Reconstruct the signal using the modified coefficients
        denoised_signal = pywt.waverec([cA2, cD2, cD1], wavelet)
        # Store the denoised signal
        denoised_data[factor] = denoised_signal[:len(df)]  # Slice to original length if needed

    # Convert the dictionary to a DataFrame
    denoised_df = pd.DataFrame.from_dict(denoised_data)
    return denoised_df
