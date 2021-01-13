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
sat_dict = {}

for line in line_list:
    sat = line.split()[0]
    if sat == '1':
        continue
    elif sat == '2':
        continue
    else:
        sat_dict[sat] = sat_dict.get(sat, 0) + 1

for sattelite in sorted(sat_dict.keys()):
    print(sattelite, sat_dict[sattelite])
    f_out.write(str(sattelite) + '\t' + str(sat_dict[sattelite]) + '\n')

f_in.close
f_out.close
