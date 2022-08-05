from machine import Pin
import utime

# constants
HALF_STEP_MODE = True
PINS = [2,3,4,5] # Raspberry Pi Pico GP2, GP3, GP4, GP5 pins
INTERVAL = 0.001 # Deplay between the sequence

FULL_STEP_TABLE_SEQ = [
        [1,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,1]
]

HALF_STEP_SEQ = [
    [0, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
]

# Check for step mode
step_table = HALF_STEP_SEQ if HALF_STEP_MODE else FULL_STEP_TABLE_SEQ

# make pico pins as output
pins = [Pin(p, Pin.OUT, 0) for p in PINS]

def __reset():
    """ Set all output pins to 0 to stop setpper motor """
    for pin in pins:
        pin.value(0)
        
def move(steps: int=1, direction: int=1):
    """
    Move the stepper motor a specific number of steps in one direction.

    ### Arguments
    - steps : int (Default: 1)
      How many steps to move in the specified direction.
    - direction : int (Default: 1)
      The direction to move. Must be either: 1 for forward, or -1 for backwards.
    """
    for _ in range(steps):
        for state in step_table[::direction]:
            for p in range(4):
                pins[p].value(state[p])
            utime.sleep(INTERVAL)
    __reset()
    
while True:
    move(512)
    __reset()
    utime.sleep(1)
