import os

def read_matrices(file_path):
    matrices = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            dimensions, matrix_data = line.split(':')
            rows, columns = map(int, dimensions.split('x'))
            matrix = [[int(matrix_data[i * columns + j]) for j in range(columns)] for i in range(rows)]
            matrices.append(matrix)
    return matrices

def is_valid_position(matrix, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])

def count_isolated_ones(matrix):
    isolated_count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                if all(
                    not is_valid_position(matrix, row + dr, col + dc) or matrix[row + dr][col + dc] == 0
                    for dr in [-1, 0, 1] for dc in [-1, 0, 1] if dr != 0 or dc != 0
                ):
                    isolated_count += 1
    return isolated_count

def count_clusters_of_size(matrix, size):
    def dfs(r, c):
        if not is_valid_position(matrix, r, c) or matrix[r][c] != 1 or visited[r][c]:
            return 0
        visited[r][c] = True
        count = 1
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            count += dfs(r + dr, c + dc)
        return count
    
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    cluster_count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1 and not visited[row][col]:
                if dfs(row, col) == size:
                    cluster_count += 1
    return cluster_count

def main():
    file_path = 'mat.in'
    matrices = read_matrices(file_path)
    
    results = []
    for matrix in matrices:
        isolated_ones = count_isolated_ones(matrix)
        clusters_of_two = count_clusters_of_size(matrix, 2)
        clusters_of_three = count_clusters_of_size(matrix, 3)
        results.append(f"{isolated_ones} {clusters_of_two} {clusters_of_three}")
    
    with open('mat.out', 'w') as output_file:
        output_file.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
