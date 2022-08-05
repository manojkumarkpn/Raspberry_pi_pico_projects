# Pin connections 
* Connect external supply for ULN2003 Driver module  
* ULN2003 board and Raspberry Pi Pico

    IN1 - GP2
    IN2 - GP3, 
    IN3 - GP4, 
    IN4 - GP5

# 28BYJ-48 stepper motor Specifications
 * Rated voltage	5 V
 * Coil Resistance	50 Ohms
 * Coil Type	Unipolar
 * Diameter – shaft	0.197″ (5.00 mm
 * Length – shaft and bearing	0.394″ (10 mm
 * Features	Flatted shaft
 * Size/dimension	Round – 1.100″ dia (28.00 mm
 * Mounting hole spacing	Flatted Shaft
 * Gear reduction	1/64 (see note
 * Step angle	Half step mode (recommended): 0.0879
 * Full step mode: 0.176
 * Steps per revolution
     * Half step mode: 4096 (see note
     * Full step mode: 2048
 * Termination style	Wire leads with connector
 * Motor type	Permanent Magnet Gear Motor
 * Number of phases	4

# Half mode steps calculation
 * Steps  per revolution : 4096sequeces steps : 8
 * Number of steps to be passed for 360 degree:  4096/8 = 512 steps
 * Number of steps to be passed for 180 degree :  4096/8/2 = 256 steps
 * Number of steps to be passed per degree : 360/512 = 0.703125 degree
 * Number of steps to be passed per 10 degree : 10/0.703125 = 14.2222

# Full mode steps calculation
 * steps  per revolution : 4096
 * sequeces steps : 8
 * Number of steps to be passed for 360 degree:  2048/4 = 512 steps
 * Number of steps to be passed for 180 degree :  2048/4/2 = 256 steps
 * degree per Number of steps : 360/512 = 0.703125 degree
 * Number of steps to be passed per 10 degree : 10/0.703125 = 14.2222
