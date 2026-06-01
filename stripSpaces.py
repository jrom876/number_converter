#!/usr/bin/env python3
# https://github.com/jrom876/decToBinCalculator/blob/master/decToBinCalc.py

# Description:	Universal binary/octal/decimal/hexidecimal converter which
#				removes all spaces before converting values

import pdb
import math

#========= Binary ==========#
def bin_to_dec(binary):
	decimal, i = 0, 0 
	binary = str(binary)
	binary = binary.replace(" ", "")
	binary = int(binary, 2)
	while(binary != 0):
		dec = binary % 10
		decimal = decimal + dec * pow(10, i)
		binary = binary//10
		i += 1
	return decimal

# ~ def bin_to_oct(binary):
	# ~ octal, i = 0, 0
	# ~ binary = str(binary)
	# ~ binary = binary.replace(" ", "")
	# ~ binary = int(binary, 2)
	# ~ while(binary != 0):
		# ~ oct = binary % 8
		# ~ octal = octal + oct * pow(8, i)
		# ~ binary = binary//8
		# ~ i += 1
	# ~ return octal

def bin_to_oct(binary):
	x = bin_to_dec(binary)
	return oct(x)

# ~ def bin_to_hex(binary):
	# ~ hexa, i = 0, 0
	# ~ binary = str(binary)
	# ~ binary = binary.replace(" ", "")
	# ~ binary = int(binary, 2)
	# ~ while(binary != 0):
		# ~ hexad = binary % 16
		# ~ hexa = hexa + hexad * pow(16, i)
		# ~ binary = binary//16
		# ~ i += 1
	# ~ return hex(hexa)

def bin_to_hex(binary):
	x = bin_to_dec(binary)
	return hex(x)

#========= Octal ==========#
def oct_to_bin(oct):
	# return int(oct(x)[2:])
	bina = str(oct)
	bina = bina.replace(" ", "")
	octa = int(bina, 8)
	return bin(octa)

def oct_to_dec(oct):
	# return int(oct(x)[2:])
	dec = str(oct)
	dec = dec.replace(" ", "")
	octa = int(dec, 8);
	return octa

def oct_to_hex(oct):
	hexa = str(oct)
	hexa = hexa.replace(" ", "")
	octa = int(hexa, 8)
	return hex(octa)

#========= Decimal ==========#
# def dec_to_bin(x):
#     # return int(bin(x)[2:])
#     return bin(x)

def dec_to_bin(decimal):
	binary, i = 0, 0
	decimal = str(decimal)
	decimal = decimal.replace(" ", "")
	decimal = int(decimal, 10)
	while(decimal != 0):
		bin = decimal % 2
		binary = binary + bin * pow(10, i)
		decimal = decimal//2
		i += 1
	return binary

# def dec_to_oct(x):
#     # return int(oct(x)[2:])
#     return oct(x)

def dec_to_oct(decimal):
	octal, i = 0, 0
	decimal = str(decimal)
	decimal = decimal.replace(" ", "")
	decimal = int(decimal, 10)
	while(decimal != 0):
		oct = decimal % 8
		octal = octal + oct * pow(10, i)
		decimal = decimal//8
		i += 1

	return '0o'+str(octal)

def dec_to_hex(x):
	x = str(x)
	x = x.replace(" ", "")
	x = int(x, 10)
	return hex(x)

#========= Hexadecimal ==========#
def hex_to_bin(hex):
	dec = str(hex)
	dec = dec.replace(" ", "")
	dec = int(dec, 10)
	return dec_to_bin(dec)

	
def hex_to_oct(hex):
	dec = str(hex)
	dec = dec.replace(" ", "")
	dec = int(dec, 10)
	return dec_to_oct(dec)
	
def hex_to_dec(hex):
	hex = str(hex)
	hex = hex.replace(" ", "")
	hex = int(hex, 10)
	return hex

########################################
### User Interface ###
def getuserInput():
	"""Test the hex_to_dec function
	
	Usage examples:
	>>> bin_to_dec("11 11")
	15
	
	>>> bin_to_oct("11 11")
	'0o17'
	
	# ~ >>> bin_to_hex("11 11")	
	# ~ '0xf'	

	>>> oct_to_bin("2 5")
	'0b10101'
	
	>>> oct_to_dec("2 5")
	21

	>>> oct_to_hex("2 5")
	'0x15'

	>>> dec_to_bin("2 5")
	11001
	
	>>> dec_to_oct("18 29")
	'0o3445'

	>>> dec_to_hex("65 5 34")
	'0xfffe'
		
	>>> hex_to_bin("88 99")
	'1000100010011001'
			
	>>> hex_to_oct("88 99")
	'0o104231'
	
	>>> hex_to_dec("88 99")
	'34969'

	"""
	print("1 = Binary to All    2 = Octal to All")
	print("3 = Decimal to All   4 = Hex to All")
	print("5 = Exit\n")
	choice = str(input("Choose from the above list:\t"))
	choice = choice.replace(" ", "")
	#choice = int(input("Choose from the above list:\t"))
	choice = int(choice)

	if choice == 1:# Binary to all
		# ~ bin = bin.strip()
		bin = str(input("Binary in ==> "))
		bin = bin.replace(" ", "")
		bin = int(bin)
		print("Octal: ",bin_to_oct(bin))
		print("Decimal: ",bin_to_dec(bin))
		print("Hexadecimal: ",bin_to_hex(bin))
		return 0
	elif choice == 2:# Octal to All
		oct = str(input("Octal in ==> "))
		oct = oct.replace(" ", "")
		oct = int(oct)
		# ~ oct = input("Octal in ==> ")
		print("Binary: ",oct_to_bin(oct))
		print("Decimal: ",oct_to_dec(oct))
		print("Hexadecimal: ",oct_to_hex(oct))
		return 0
	elif choice == 3:# Decimal to All
		dec = str(input("Decimal in ==> "))
		dec = dec.replace(" ", "")
		dec = int(dec)
		# ~ dec = int(input("Decimal in ==> "))
		print("Binary: ",dec_to_bin(dec))
		print("Octal: ",dec_to_oct(dec))
		print("Hexadecimal: ",dec_to_hex(dec))
		return 0
	elif choice == 4:# Hex to All
		hexa = str(input("Hex in ==> "))
		hexa = hexa.replace(" ", "")
		hexa = int(hexa, 16)		
		print("Binary: ",hex_to_bin(hexa))
		print("Octal: ",hex_to_oct(hexa))
		print("Decimal: ",hex_to_dec(hexa))
		# ~ print("Decimal: ",hex_to_decimal(hexa))
		return 0
	elif choice == 5: # Exit
		exit_flag = 1
		return 0
	else:
		return 0

#########################################
# Driver program
if __name__ == "__main__":

	exit_flag = 0

	while exit_flag == 0:
		print("\nWelcome to Number Converter ")
		ch = input("To begin, choose (c)ontinue or (q)uit\n")
		if ch == "q":
			print("Now exiting the program\n ")
			exit_flag = 1
		elif ch == "c":
			getuserInput()
			exit_flag = 0
		else:
			print("Incorrect answer. \n Exiting\n ")
			exit_flag = 1
