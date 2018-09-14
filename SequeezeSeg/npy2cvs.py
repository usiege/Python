#!/usr/bin/python3

import numpy as np 
import pandas as pa

import argparse

def load(path):
	npy = np.load(path)
	print(np.shape(npy))
	print(npy)

	return npy


if __name__ == '__main__':

	parser = argparse.ArgumentParser(description = "script")
	parser.add_argument("--path", type = str, default = None)

	args = parser.parse_args()
	print("parser path: ")
	print(args)

	npdata = load(args.path)
	npdata = np.reshape(npdata, (-1, 6))

	#
	padata = pa.DataFrame(npdata,columns = ['x', 'y', 'z', 'intensity', 'range', 'category'])
	# padata = pa.DataFrame(npdata, columns = None)
	print(padata)

	xyz_data = padata[['x', 'y', 'z', 'intensity', 'range', 'category']].astype('float64')
	xyz_data.to_csv('data.csv', index = False, header = False)