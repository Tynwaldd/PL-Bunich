def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        rows, cols = map(int, file.readline().strip().split())
        matrix = [list(map(int, file.readline().strip().split())) for _ in range(rows)]
    return matrix


def write_matrix_to_file(filename, matrix):
    with open(filename, 'w') as file:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        file.write(f"{rows} {cols}\n")
        for row in matrix:
            file.write(" ".join(map(str, row)) + '\n')


def main():
    input_filename = "Бунич_Денис_Андреевич_У_244_vvod.txt"
    output_filename = "Бунич_Денис_Андреевич_У_244_vivod.txt"

    matrix = read_matrix_from_file(input_filename)
    result_matrix = matrix

    write_matrix_to_file(output_filename, result_matrix)


if __name__ == "__main__":
    main()
