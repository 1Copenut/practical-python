"""
bounce.py
Exercise 1.5
"""

HEIGHT = 100  # meters
BOUNCES = 0  # number of bounces

while BOUNCES < 10:
    BOUNCES = BOUNCES + 1
    HEIGHT = HEIGHT * (3/5)
    # print(height)
    print(round(HEIGHT, 4))
