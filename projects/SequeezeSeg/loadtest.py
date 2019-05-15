#!/usr/bin/python3

import numpy as np
import sys
import argparse

def load(path):
	npy = np.load(path)
	print(np.shape(npy))
	print(npy)


if __name__ == '__main__':

	argvs = sys.argv
	print("sys path: ")
	print(argvs)

	parser = argparse.ArgumentParser(description = "script")
	parser.add_argument("--path", type = str, default = None)

	args = parser.parse_args()
	print("parser path: ")
	print(args)

	load(args.path)