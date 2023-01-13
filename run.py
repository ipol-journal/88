#!/usr/bin/env python3

import subprocess
import argparse

# parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("alpha", type=int)
ap.add_argument("omega", type=str)
ap.add_argument("gaussianstd", type=int)
ap.add_argument("method", type=str)
ap.add_argument("numlevels", type=int)
ap.add_argument("degree", type=int)
args = ap.parse_args()

if args.omega == 'G':
    args.omega += ':' + str(args.gaussianstd)

if args.method == 'poly':
    args.method += ':' + str(args.degree)
else:
    args.method += ':' + str(args.numlevels)


with open('stdout.txt', 'w') as stdout:
    p1 = ['ace', '-a', str(args.alpha), '-w' + str(args.omega), '-m' + str(args.method), 'input_0.png', 'ace.png']
    subprocess.run(p1, stdout=stdout, stderr=stdout) 

with open('stdout.txt', 'w') as stdout:
    p2 = ['histeq', 'input_0.png', 'he.png']
    subprocess.run(p2, stderr=stdout)
