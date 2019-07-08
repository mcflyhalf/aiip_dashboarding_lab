#Data Format
#DateTime| Motor ID| Motor status | Motor Speed | Motor Torque| Motor Fault|

import csv
import time
import random
from datetime import datetime

motor_ids = ['m1','m2']
def get_fault():
	'''Pick a fault status code at random. Mostly status is fine (1) but 1% of the time status is Fault(-999)'''
	if random.randint(0,100) < 100:
		return 0
	return -999

def get_status():
	'''Mostly running (1), sometimes shut down (0)'''
	if random.randint(0,10) < 9:
		return 1
	return 0

def motor_params(mid=None, header=False):
	'''Get Parameters for a single motor with id mid. Or alternatively print the header row'''
	if header:
		return ['dtime','motor_id','motor status','speed','torque','fault']


	fault = get_fault()
	if fault < 0:
		status = "Nan"
		speed = "Nan"
		torque = "Nan"
	else:
		status = get_status()
		speed = random.randint(500,600)
		torque = random.randint(1200,1250)


	dtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		
	return [dtime,mid,status,speed,torque,fault]



def main():
	motor_states = []

	for mid in motor_ids:
		motor_states.append(motor_params(mid))
	
	with open('motor_logs.csv','a') as logfile:
		writer = csv.writer(logfile)
		if not logfile.tell():		#If logfile is empty
			writer.writerow(motor_params(header=True))
			
		writer.writerows(motor_states)
		



if __name__ == '__main__':
	while True:
		main()
		time.sleep(60)
