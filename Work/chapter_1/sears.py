"""sears.py calculates the number of dollar bills needed to equal the height of the Sears Tower"""

BILL_THICKNESS = 0.11 * 0.001    # Meters (0.11 mm)
SEARS_HEIGHT = 442             # Height (meters)
NUM_BILLS = 1
DAY = 1

while NUM_BILLS * BILL_THICKNESS < SEARS_HEIGHT:
    print(DAY, NUM_BILLS, NUM_BILLS * BILL_THICKNESS)
    DAY = DAY + 1
    NUM_BILLS = NUM_BILLS * 2

print('Number of days', DAY)
print('Number of bills', NUM_BILLS)
print('Final height', NUM_BILLS * BILL_THICKNESS)
