Function Name
nmatrix_stat_summary

Description
matrix_stat_summary is a versatile statistical summary function that accepts a flat or one-level nested list of numerical data and reshapes it into a 2D matrix of any specified shape. It automatically flattens one level of nesting in the input list to ensure correct reshaping. The function calculates a comprehensive set of statistical measures—such as mean, variance, standard deviation, min, max, sum, median, range, and mode—either across rows, columns, or the entire matrix, depending on the user-specified axis. The results can be returned flexibly as a Python dictionary, flattened list of labeled tuples, JSON string, or a Pandas DataFrame for further data analysis or visualization.

What Makes It Unique?
1. Automatic Nested List Flattening: Accepts both flat and one-level nested lists, automatically flattening nested input to simplify user data preparation.
2. Flexible Reshaping: Allows user to specify exact 2D matrix shape for reshaping input data
3. Axis Control: Supports computation of statistics by rows, columns, or overall, for granular insights.
4. Wide Range of Stats: Provides mean, variance, std, min, max, sum, median, range, and mode in a single unified function.
5. Multiple Output Formats: Outputs results as dict, JSON, labeled list, or DataFrame, adapting to different downstream use cases.
6. Robust Input Validation: Checks input types, shapes, axis values, and output format options to minimize errors.
7. Correct Mode Calculation with Axis Support: Handles mode calculations properly along specified axis, a common pitfall in similar utilities.
