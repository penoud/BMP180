#!/usr/bin/env python
# -*- coding: utf-8 -*-
import PyBCM2835
import re
import inspect

class BMP180:
        ADDRESS = 0x77
        CONFIG_REG = 0xF4

	CONFIG_CMD_TEMP_CNV = 0x2E
	CONFIG_CMD_PRESSURE_CNV = 0x34	

        ID_REG = 0xD0
        ID = 0x55
	RESET_REG = 0xE0
	RESET = 0xB6
	XLSB_REG = 0xF9
	LSB_REG = 0xF7
	MSB_REG = 0xF6

	AC1 = 0
	AC2 = 0
	AC3 = 0
	AC4 = 0
	AC5 = 0
	AC6 = 0
	B1 = 0
	B2 = 0
	MB = 0
	MC = 0
	MD = 0
	UT = 0
	UP = 0
	T = 0
	P = 0

	oversampling = 0	

        def __init__(self):
                if not (PyBCM2835.init()):
                        raise EnvironmentError("Cannot initialize BCM2835.")
                PyBCM2835.i2c_begin()
	def readPressure(self):
		return self.P/100.0
	def readTemperature(self):
		return self.T/10.0
	def conversion(self):
		self.readCalibration()
		self.startTempConversion()
		self.startPressureConversion()
		self.calculateTemperature()
		self.calculatePressure()
	def setOvversampling(self,oversampling):
		if(oversampling < 4):
			print("Error, oversampling value must be lower than 4")
		else:
			self.oversampling = oversampling
	def setSlaveAddress(self):
		try :
		    function_call = inspect.stack()[1][4][0].strip()

		    # See if the function_call has "self." in the begining
		    matched = re.match( '^self\.', function_call )
		    if not matched :
		        print 'This is Private Function, Go Away'
		        return
		except :
		    print 'This is Private Function, Go Away'
		    return

		# This is the real Function, only accessible inside class #
                PyBCM2835.i2c_setSlaveAddress(self.ADDRESS)
        def writeReg(self,register,value):
		try :
		    function_call = inspect.stack()[1][4][0].strip()

		    # See if the function_call has "self." in the begining
		    matched = re.match( '^self\.', function_call )
		    if not matched :
		        print 'This is Private Function, Go Away'
		        return
		except :
		    print 'This is Private Function, Go Away'
		    return

		# This is the real Function, only accessible inside class #
		self.setSlaveAddress()
                PyBCM2835.i2c_write(chr(register)+chr(value),2)
        def readReg(self,register):
		try :
		    function_call = inspect.stack()[1][4][0].strip()

		    # See if the function_call has "self." in the begining
		    matched = re.match( '^self\.', function_call )
		    if not matched :
		        print 'This is Private Function, Go Away'
		        return
		except :
		    print 'This is Private Function, Go Away'
		    return

		# This is the real Function, only accessible inside class #
		self.setSlaveAddress()
                data=""+chr(0)
                PyBCM2835.i2c_read_register_rs(chr(register),data,1)
                return ord(data[0])
	def convertShort(self,value):
		try :
		    function_call = inspect.stack()[1][4][0].strip()

		    # See if the function_call has "self." in the begining
		    matched = re.match( '^self\.', function_call )
		    if not matched :
		        print 'This is Private Function, Go Away'
		        return
		except :
		    print 'This is Private Function, Go Away'
		    return

		# This is the real Function, only accessible inside class #
		if (value>32767):
			value = value - 65535
		return value
	def readCalibration(self):
		try :
		    function_call = inspect.stack()[1][4][0].strip()

		    # See if the function_call has "self." in the begining
		    matched = re.match( '^self\.', function_call )
		    if not matched :
		        print 'This is Private Function, Go Away'
		        return
		except :
		    print 'This is Private Function, Go Away'
		    return

		# This is the real Function, only accessible inside class #
		self.setSlaveAddress()
		self.AC1 = self.convertShort((self.readReg(0xAA)<<8)|self.readReg(0xAB))
		self.AC2 = self.convertShort((self.readReg(0xAC)<<8)|self.readReg(0xAD))
		self.AC3 = self.convertShort((self.readReg(0xAE)<<8)|self.readReg(0xAF))
		self.AC4 = (self.readReg(0xB0)<<8)|self.readReg(0xB1)
		self.AC5 = (self.readReg(0xB2)<<8)|self.readReg(0xB3)
		self.AC6 = (self.readReg(0xB4)<<8)|self.readReg(0xB5)
		self.B1 = self.convertShort((self.readReg(0xB6)<<8)|self.readReg(0xB7))
		self.B2 = self.convertShort((self.readReg(0xB8)<<8)|self.readReg(0xB9))
		self.MB = self.convertShort((self.readReg(0xBA)<<8)|self.readReg(0xBA))
		self.MC = self.convertShort((self.readReg(0xBC)<<8)|self.readReg(0xBD))
		self.MD = self.convertShort((self.readReg(0xBE)<<8)|self.readReg(0xBF))

		#print "AC1 = " + str(self.AC1)
		#print "AC2 = " + str(self.AC2)
		#print "AC3 = " + str(self.AC3)
		#print "AC4 = " + str(self.AC4)
		#print "AC5 = " + str(self.AC5)
		#print "AC6 = " + str(self.AC6)
		#print "B1 = " + str(self.B1)
		#print "B2 = " + str(self.B2)
		#print "MB = " + str(self.MB)
		#print "MC = " + str(self.MC)
		#print "MD = " + str(self.MD)



        def startTempConversion(self):
		try :
		    function_call = inspect.stack()[1][4][0].strip()

		    # See if the function_call has "self." in the begining
		    matched = re.match( '^self\.', function_call )
		    if not matched :
		        print 'This is Private Function, Go Away'
		        return
		except :
		    print 'This is Private Function, Go Away'
		    return

		# This is the real Function, only accessible inside class #
		self.setSlaveAddress()
                self.writeReg(self.CONFIG_REG,self.CONFIG_CMD_TEMP_CNV)		
		PyBCM2835.delay(8)
		self.UT = (self.readReg(self.MSB_REG)<<8) | self.readReg(self.LSB_REG)
		#print "UT = " + str(self.UT)
        def startPressureConversion(self):
		try :
		    function_call = inspect.stack()[1][4][0].strip()

		    # See if the function_call has "self." in the begining
		    matched = re.match( '^self\.', function_call )
		    if not matched :
		        print 'This is Private Function, Go Away'
		        return
		except :
		    print 'This is Private Function, Go Away'
		    return

		# This is the real Function, only accessible inside class #
		self.setSlaveAddress()
	        self.writeReg(self.CONFIG_REG,self.CONFIG_CMD_PRESSURE_CNV | (self.oversampling<<6))
		if (self.oversampling == 0):
			PyBCM2835.delay(6)
		elif (self.oversampling == 1):
			PyBCM2835.delay(10)
		elif (self.oversampling == 2):
			PyBCM2835.delay(16)
		elif (self.oversampling == 3):
			PyBCM2835.delay(30)			
		self.UP = (((self.readReg(self.MSB_REG)<<16) | (self.readReg(self.LSB_REG)<<8) | self.readReg(self.XLSB_REG))>>(8-self.oversampling))
		#print "UP = " + str(self.UP)
      
	def calculateTemperature(self):	
		try :
		    function_call = inspect.stack()[1][4][0].strip()

		    # See if the function_call has "self." in the begining
		    matched = re.match( '^self\.', function_call )
		    if not matched :
		        print 'This is Private Function, Go Away'
		        return
		except :
		    print 'This is Private Function, Go Away'
		    return

		# This is the real Function, only accessible inside class #
		self.X1 = (self.UT - self.AC6) * self.AC5 / (2**15)
		#print "X1 =" + str(self.X1)
		self.X2 = self.MC * (2**11) / (self.X1 + self.MD)
		#print "X2 =" + str(self.X2)
		self.B5 = self.X1 + self.X2
		#print "B5 =" + str(self.B5)
		self.T = (self.B5 + 8) / (2**4)
		#print "T =" + str(self.T)
	def calculatePressure(self):
		try :
		    function_call = inspect.stack()[1][4][0].strip()

		    # See if the function_call has "self." in the begining
		    matched = re.match( '^self\.', function_call )
		    if not matched :
		        print 'This is Private Function, Go Away'
		        return
		except :
		    print 'This is Private Function, Go Away'
		    return

		# This is the real Function, only accessible inside class #
		self.B6 = self.B5 - 4000
		#print "B6 =" + str(self.B6)
		self.X1 = (self.B2 * (self.B6*self.B6/(2**12)))/(2**11)
		#print "X1 =" + str(self.X1)
		self.X2 = self.AC2 * self.B6 / (2**11)
		#print "X2 =" + str(self.X2)
		self.X3 = self.X1 + self.X2
		#print "X3 =" + str(self.X3)
		self.B3 = (((self.AC1 * 4 + self.X3)<<self.oversampling) + 2) / 4
		#print "B3 =" + str(self.B3)
		self.X1 = self.AC3  * self.B6 / (2**15)
		#print "X1 =" + str(self.X1)
		self.X2 = self.B1 * (self.B6*self.B6/(2**12))/(2**16)
		#print "X2 =" + str(self.X2)
		self.X3 =  ((self.X1 + self.X2) + 2) / 4
		#print "X3 =" + str(self.X3)
		self.B4 = self.AC4 * (self.X3 + 32768)/(2**15)
		#print "B4 =" + str(self.B4)
		self.B7 = (self.UP - self.B3) * (50000 >> self.oversampling)

		if (self.B7 < 0x80000000):
			self.P = (self.B7 * 2)/self.B4
		else:
			self.P = (self.B7/self.B4)*2
		self.X1 = (self.P / (2**8))*(self.P/(2**8))
		#print "X1 =" + str(self.X1)
		self.X1 = (self.X1 * 3038)/(2**16)
		#print "X1 =" + str(self.X1)
		self.X2 = (-7357 * self.P)/(2**16)
		#print "X2 =" + str(self.X2)
		self.P = self.P + (self.X1+self.X2+3791)/(2**4)
		#print "P =" + str(self.P)
