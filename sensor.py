from sense_hat import SenseHat
import time

sense = SenseHat()

# Define the color orange (Red, Green, Blue)
orange = (255, 165, 0)
blue = (5,5,255)
red = (255, 5,5)

colors = [orange,blue,red] 

i=len(colors)

sense.clear()


while True:
    # Get sensor readings
    temp = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()
    
    if i<0:
        i=len(colors)
    
    i -= 1
    sense.clear(colors[i])

    # Orientation data
    #orientation = sense.get_orientation()
    #pitch = orientation['pitch']
    #roll = orientation['roll']
    #yaw = orientation['yaw']

    # Accelerometer, gyroscope, and magnetometer data
    #acceleration = sense.get_accelerometer_raw()
    #gyro = sense.get_gyroscope_raw()
    #mag = sense.get_compass_raw()

    # Print the data
    print(f"\r{i} Temperature: {temp:04.1f}C, Humidity: {humidity:03.0f}%, Pressure: {pressure:4.0f} Millibars",end='', flush=True)
    #print(f"Pitch: {pitch}, Roll: {roll}, Yaw: {yaw}")
    #print(f"Acceleration: {acceleration}, Gyro: {gyro}, ")
    
    time.sleep(1)
