#!/usr/bin/env python
# -*- coding: utf-8 -*-
import BMP180
import PyBCM2835

def main():
        myBMP180 = BMP180.BMP180()
        while(1):
		myBMP180.conversion()
                pressure = myBMP180.readPressure()
                temp = myBMP180.readTemperature()
                PyBCM2835.delay(1000)
                print "Temp = " + str(temp) + " C, pressure = " + str(pressure)


if __name__ == '__main__':
    main()
