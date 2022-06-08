from w1thermsensor import W1ThermSensor

Array_ID = [0,0,0]
Array_T = [0,0,0]
Counter = 0

while True:
  for sensor in W1ThermSensor.get_available_sensors():
    
      print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))
      Array_ID[Counter] = sensor.id
      Array_T[Counter] = sensor.get_temperature()
    
      Counter = Counter +1
    