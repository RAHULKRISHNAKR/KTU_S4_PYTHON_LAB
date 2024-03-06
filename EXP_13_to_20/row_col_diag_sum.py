def calculate_and_append_sums(mat):
  rsum = [sum(row) for row in mat]
  csum = [sum(col) for col in zip(*mat)]

  dsum = None
  if len(mat) == len(mat[0]):
    dsum = sum(mat[i][i] for i in range(len(mat)))

  new_matrix = [[0 for _ in range(len(mat[0]) + 1)] for _ in range(len(mat) + 1)]

  for i in range(len(mat)):
    for j in range(len(mat[0])):
      new_matrix[i][j] = mat[i][j]
  for i in range(len(mat)):
    new_matrix[i][-1] = rsum[i]
  for j in range(len(mat[0])):
    new_matrix[-1][j] = csum[j]
  if dsum is not None:
    new_matrix[-1][-1] = dsum

  return new_matrix

m, n = map(int, input("Enter the dimensions of the matrix (m x n): ").split())
matrix = [[int(input(f"Enter element ({i+1},{j+1}): ")) for j in range(n)] for i in range(m)]

new_matrix = calculate_and_append_sums(matrix)

print("\nOriginal matrix:")
for row in matrix:
  print(row)
print("\nNew matrix:")
for row in new_matrix:
  print(row)
