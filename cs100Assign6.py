# =======================================================================================================
# Read and process data from a file.
# =======================================================================================================

#import os
import tkinter as tk
from tkinter.filedialog import *

# -----------------------------------------------------------------------------------------
# input file
fn_in = askopenfilename(title="Select input file",
                        filetypes=[("*.TXT", "*.txt")])
f_in = open(fn_in, "r")

# -----------------------------------------------------------------------------------------
# output file
fn_out = asksaveasfilename(title="Select output file",
                           filetypes=[("*.TXT", "*.txt")])
f_out = open(fn_out, "w")

line_list = f_in.readlines()

temp_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
day_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for line in line_list:
    s = line.split()
    month, temp = int(s[0]), float(s[-1])
    if temp == -99:
        continue
    temp_sum[month - 1] += temp
    day_count[month - 1] += 1
for i in range(12):
    print(i + 1, temp_sum[i] / day_count[i])


f_in.close()
f_out.close()
