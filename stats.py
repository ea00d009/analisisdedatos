import numpy as np

def calculate_metrics(data):
    return {'mean': np.mean(data), 'std': np.std(data)}
