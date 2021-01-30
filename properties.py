# Import libraries
import numpy as np # NumPy: contains basic numerical routines
import scipy # SciPy: contains additional numerical routines to numpy
import scipy.sparse as scysparse
import scipy.sparse.linalg
import re
import itertools # for permutations
import os
import matplotlib.pyplot as plt
import math
from math import pi as PI
from scipy.optimize import fsolve
from matplotlib.font_manager import FontProperties
from sympy import symbols, solve
import os
import CoolProp
import CoolProp.CoolProp as CP
from CoolProp.CoolProp import PropsSI as prop

### Fluid Property Calculations Based on State Conditions
def waterProperties(propertyNames, propertyValues):
	if propertyNames[0]=='P' and propertyNames[1]=='Q':
		rho = prop('D',propertyNames[0],BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # kg/m3
		v = 1/rho # m3/kg
		temp = prop('T',propertyNames[0],BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # K
		intEnergy = prop('U',propertyNames[0],BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg
		enthalpy = prop('H',propertyNames[0],BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg
		entropy = prop('S',propertyNames[0],BarToPa(propertyValues[0]),propertyNames[1],propertyValues[1],'Water') # J/kg-K

	elif propertyNames[0]=='P' and propertyNames[1]=='D':
		rho = propertyValues[1]
		v = 1/rho # m3/kg
		temp = prop('T',propertyNames[0],BarToPa(propertyValues[0]),propertyNames[1],rho,'Water') # K
		intEnergy = prop('U',propertyNames[0],BarToPa(propertyValues[0]),propertyNames[1],rho,'Water') # J/kg
		enthalpy = prop('H',propertyNames[0],BarToPa(propertyValues[0]),propertyNames[1],rho,'Water') # J/kg
		entropy = prop('S',propertyNames[0],BarToPa(propertyValues[0]),propertyNames[1],rho,'Water') # J/kg-K

	print("Water Vapor Properties (SI UNITS)")
	print("===========================================")
	print("Density [rho] =\t\t",rho,"kg/m3")
	print("Specific Volume [v] =\t",v,"m3/kg")
	print("Temperature [T] =\t",temp,"K")
	print("Internal Energy [u] =\t",intEnergy,"J/kg")
	print("Enthalpy [h] =\t\t",enthalpy,"J/kg")
	print("Entropy [s] =\t\t",entropy,"J/kg-K\n")

	return [rho,v,temp,intEnergy,enthalpy,entropy]