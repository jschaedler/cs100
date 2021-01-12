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
    Month_names = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
    print(Month_names[i], 'Average Temperature:',
          temp_sum[i] / day_count[i])
    f_out.write('Month:' + '\t' + (Month_names[i]) + '\t' + 'Average Temperature: ' +
                '\t' + str(temp_sum[i] / day_count[i]) + '\n')


f_in.close()
f_out.close()
