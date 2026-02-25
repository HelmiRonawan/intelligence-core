import os
from constraint import *
import numpy as np
os.system('cls')

problem = Problem(RecursiveBacktrackingSolver())

problem.addVariables(range(9), range(1, 10))

problem.addConstraint(AllDifferentConstraint())

# Diagonal
problem.addConstraint(ExactSumConstraint(15), [0, 4, 8])
problem.addConstraint(ExactSumConstraint(15), [2, 4, 6])

# Baris
problem.addConstraint(ExactSumConstraint(15), [0, 1, 2])
problem.addConstraint(ExactSumConstraint(15), [3, 4, 5])
problem.addConstraint(ExactSumConstraint(15), [6, 7, 8])

# Kolom
problem.addConstraint(ExactSumConstraint(15), [0, 3, 6])
problem.addConstraint(ExactSumConstraint(15), [1, 4, 7])
problem.addConstraint(ExactSumConstraint(15), [2, 5, 8])

solutions = problem.getSolutions()

print(f"""
      Ditemukan {len(solutions)} solusi Magic Square 3x3!
      1. Tampilkan salah satu solusi
      2. Tampilkan semua solusi\n
      """)


pilihan = int(input("Input angka 1-2: "))

match pilihan:
    case 1:
        if solutions:
            sol = int(input("Pilih solusi 1-8: "))
            first_sol = solutions[sol-1]
            res_list = [first_sol[i] for i in range(9)]
            matrix = np.array(res_list).reshape(3, 3)
            print("Salah satu solusinya:")
            print(matrix)
    case 2:
        no = 0
        for solution in solutions:
            sol_list = [solution[i] for i in range(9)]
            matrix = np.array(sol_list).reshape(3, 3)
            no += 1
            print(no,':')
            print(matrix,'\n')
    case _:
        print("Input tidak valid")