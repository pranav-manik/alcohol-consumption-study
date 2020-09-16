import math
import numpy as np
from mathplotlib import pyplot as plt
import nsfg

def MakeFrames():
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    in_appl = []
    for x in preg.ageprep:
    	if math.isnan(x):
    		in_appl.append(x)
	return live

def Regression(live):
	mean = live.prglngth.mean()
	var = live.prglngth.var()
	std = live.prglngth.std()
	
	z_age = []
	z_wt = []
	z_cross = []

	wt_mean = live.totalwgt_lb.mean()
	age_mean = live.agepreg.mean()
	wt_sd = live.totalwgt_lb.std()
	age_sd = live.agepreg.std()

	data = live[np.isfinite(live['totalwgt_lb'])]

	z_a = (preg.agepreg - age_mean)/age_sd
	z_age.append(z_a)
	z_w = (preg.totalwgt_lb - wt_mean)/wt_sd
	z_wt.append(z_w)
	# print ("ZA and ZW ARE", z_a, z_w)
	z_cross.append(z_a * z_w)

	sum_cross = sum(z_cross)
	len_cross = len(z_cross)
	r = sum_cross/len_cross
	print("Sum IS", sum_cross)
	print("LEN IS", len_cross)
	print("WT_SD IS", wt_sd)
	print("AG_SD IS", age_sd)

	m = r * (wt_sd/age_sd)
	b = wt_mean - age_mean * m
	print("Regression line is wt =", m, "age +",b)

live = MakeFrames()
Regression(live)

