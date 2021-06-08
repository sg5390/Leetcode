import math

# ALL_LATENCIES = [
    0.25589525815118686,
    0.1666865011880021,
    0.3640850051711415,
    0.46888554561214413,
    1.5264772687981958,
    1.2182882133438868,
    0.2963250423370145,
    2.070337738926535,
    5.32887226557879,
    3.5611535580285754,
    0.6357744879510403,
    2.609330343370753,
    3.167112136066649,
    1.9448104942989919,
    0.3110763092201544,
    2.039493671452421,
    0.43159245938645563,
    2.500865500659632,
    0.8442174772740363,
    1.998084024508116
 ]

def compute_percentile(latencies, percentile):
    latencies.sort()
    index = (len(latencies)-1) * percentile / 100
    print(index)
    lower_index = math.floor(index)
    print(lower_index)
    upper_index = math.ceil(index)
    print(upper_index)
    if upper_index == lower_index:
        return latencies[int(index)]
    # Note that here we are interpolating percentile values based
    # on lower and upper bounds around where the exact index in the array
    # would be
    d0 = latencies[int(lower_index)] * (upper_index - index)
    print(d0)
    d1 = latencies[int(upper_index)] * (index - lower_index)
    print(d1)
    return d0 + d1

def compute_p50(latencies):
    """
    TODO: Fill in this function! Don't use any external libraries :)
    :param latencies: A list of latencies.
    :return: Computed p50 provided as float.
    """
    return compute_percentile(latencies, 50)

def compute_p90(latencies):
    """
    TODO: Fill in this function! Don't use any external libraries :)
    :param latencies: A list of latencies.
    :return: Computed p90 provided as float.
    """
    return compute_percentile(latencies, 90)


ALL_LATENCIES = [
    0.25589525815118686,
    0.1666865011880021,
    0.3640850051711415,
    0.46888554561214413,
    1.5264772687981958,
    1.2182882133438868,
    0.2963250423370145,
    2.070337738926535,
    5.32887226557879,
    3.5611535580285754,
    0.6357744879510403,
    2.609330343370753,
    3.167112136066649,
    1.9448104942989919,
    0.3110763092201544,
    2.039493671452421,
    0.43159245938645563,
    2.500865500659632,
    0.8442174772740363,
    1.998084024508116
 ]



print(compute_p50(ALL_LATENCIES))
print(compute_p90(ALL_LATENCIES))
