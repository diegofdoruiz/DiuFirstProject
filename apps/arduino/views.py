from django.shortcuts import render, redirect, get_object_or_404
import serial
import time
# Create your views here.

def home(request):
	return render(request, 'home.html', {})

def test(request):
	ser = serial.Serial()
	ser.baudrate = 9600
	ser.port = '/dev/cu.usbmodem14201'
	ser.open()
	time.sleep(2)
	ser.write(b'2test')
	time.sleep(2)
	rawString = ser.readline()
	print(rawString)
	ser.close()
	return render(request, 'arduino.html', {'ser':ser, 'respuesta':rawString})