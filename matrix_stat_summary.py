import numpy as np 
import pandas as pd
import json
from scipy.stats import mode


def matrix_stat_summary(input, shape=None, axis=None, output_format='dict'):
    """
    Calculate a comprehensive set of statistics for a given list of numbers reshaped into a matrix.

    Parameters:
    ----------
    input : list
        A flat or nested list of numerical values. Length must equal the product of the dimensions specified in `shape`.
    
    shape : tuple of two ints
        The desired shape (rows, columns) to reshape the input list into a 2D NumPy array.
    
    axis : int or None, optional (default=None)
        Axis along which to compute statistics:
        - 0 : compute column-wise statistics
        - 1 : compute row-wise statistics
        - None : compute statistics over the entire matrix
    
    output_format : str, optional (default='dict')
        Format of the output results:
        - 'dict' : returns a dictionary with statistic names as keys and their results as values
        - 'list' : returns a flattened list of tuples (stat_name, value)
        - 'json' : returns a JSON string of the results
        - 'dataframe' : returns a pandas DataFrame of the results

    Returns:
    -------
    dict, list, str, or pandas.DataFrame
        The calculated statistics in the specified output format.

    Raises:
    ------
    TypeError
        If `input` is not a list or `shape` is not a tuple of two integers.
    ValueError
        If the product of `shape` does not equal the length of `input`.
        If `axis` is not one of 0, 1, or None.
        If `output_format` is not one of the supported formats.
    """

    def flatten(input):
        flattened = []
        for element in input:
            if isinstance(element,list):
                flattened.extend(element)
            else:
                flattened.append(element)
        return flattened
   
    #check if input contains nested lists and flatten 
    
    if any(isinstance(i, list) for i in input):  # detect nested list
        input = flatten(input)
    
    # verify input and specified shape
    if not (isinstance(input, list) and isinstance(shape, tuple) and len(shape) == 2):
        raise TypeError("Input must be a list and shape must be a tuple of two integers")

    if shape[0] * shape[1] != len(input):
        raise ValueError("Product of shape must match number of elements in list")

    if axis not in [0, 1, None]:
        raise ValueError("Axis value must be either 0, 1, or None")

    if output_format not in ['dict','json','list','dataframe']:
        raise ValueError("Output format must either be one of: 'dict','json','dataframe','list'")
    
    def calc_mode(x, ax):
        return mode(x, axis=ax, keepdims=False).mode
    
    operations = {'mean':np.mean,'var':np.var,'std':np.std,'max':np.max,'min':np.min,'sum':np.sum, 
                  'median':np.median,'range':np.ptp,'mode': calc_mode}
    calculations = {}

    array = np.array(input).reshape(shape)
        
    for operation, func in operations.items():
        try:
            if operation == 'mode':
                if axis is None:
                    result = func(array, None)
                else:
                    result = func(array, axis)
            else:
                if axis is None:
                    result = func(array)
                else:
                    result = func(array, axis=axis)
            try:
                calculations[operation] = result.tolist()
            except AttributeError:
                calculations[operation] = result
        except Exception as e:
            calculations[operation] = str(e)


    if output_format == 'dict':
        output = calculations
    elif output_format == 'list':
        output = []
        for name,sublist in calculations.items():
            if isinstance(sublist,list):
                for item in sublist:
                    output.append((name,item))
            else:
                output.append((name,sublist))
    elif output_format == 'dataframe':
        if axis is None:
            output = pd.DataFrame.from_dict(calculations, orient='index', columns=['value'])
        else:
            output = pd.DataFrame(calculations)
    elif output_format == 'json':
        output = json.dumps(calculations)


    return output
