import random

def generate_large_mat_in(file_path, num_matrices, rows, cols):
    with open(file_path, 'w') as file:
        for _ in range(num_matrices):
            matrix_data = ''.join(random.choice('01') for _ in range(rows * cols))
            file.write(f"{rows}x{cols}:{matrix_data}\n")

generate_large_mat_in('mat.in', 100000, 5, 5)
