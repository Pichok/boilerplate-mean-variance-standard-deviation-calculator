import numpy as np

# input: list containing 9 digits
# output: mean, variance, standard deviation, 
# max, min and sum of the rows, columns, 
# and elements in a 3x3 matrix.
def calculate(lista):
    if not isinstance(lista, list):
        raise ValueError("List must be a list.")
        return type(lista)
    elif not len(lista) == 9:
        raise ValueError("List must contain nine numbers.")
        return len(lista)
    else: 
        matrix = np.array(lista).reshape(3,3)
        
        means = [
            np.mean(matrix, axis=0).tolist(), 
            np.mean(matrix, axis=1).tolist(), 
            np.mean(matrix)
        ]

        vars = [
            np.var(matrix, axis=0).tolist(), 
            np.var(matrix, axis=1).tolist(), 
            np.var(matrix)
        ]

        stds = [
            np.std(matrix, axis=0).tolist(), 
            np.std(matrix, axis=1).tolist(), 
            np.std(matrix)
        ]

        maxs = [
            np.max(matrix, axis=0).tolist(), 
            np.max(matrix, axis=1).tolist(), 
            np.max(matrix)
        ]

        mins = [
            np.min(matrix, axis=0).tolist(), 
            np.min(matrix, axis=1).tolist(), 
            np.min(matrix)
        ]

        sums = [
            np.sum(matrix, axis=0).tolist(), 
            np.sum(matrix, axis=1).tolist(), 
            np.sum(matrix)
        ]

        calculations = {
            'mean': means,
            'variance': vars,
            'standard deviation': stds,
            'max': maxs,
            'min': mins,
            'sum': sums
        }
                
        return calculations

#try:
#    print(calculate([2,6,2,8,4,0,1,]))
#except ValueError as e:
#    print(f"Error: {e}")