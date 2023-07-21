"""var = 17
var_right = var >> 1
var_left = var << 2
var_recover = var_right << 1
print(var, var_left, var_right, var_recover)

#set carry flag to 1
flag_register = 0b100

#Set zero flag to 1
flag_register |= 0b010

#Set the overflow flag to 1

flag_register &= ~0b001

# Set the carry flag to 1
flag_register = 0b000
result = 255 + 1  # This will cause the carry flag to be set
if result > 255 & flag_register != 0b100:
    flag_register = 0b100
    print("Carry flag is set to 1")


print (bin(0b001 + 0b111))"""
# Define some flag values
FLAG_A = 0b00000001  # The first bit is set
FLAG_B = 0b00000010  # The second bit is set
FLAG_C = 0b00000100  # The third bit is set
FLAG_D = 0b00001000  # The fourth bit is set

# Set some flags
flags = 0  # Start with all flags unset
flags |= FLAG_A  # Set flag A
flags |= FLAG_C  # Set flag C

# Check if a flag is set
if flags & FLAG_A:
    print("Flag A is set!")

# Clear a flag
flags &= ~FLAG_C  # Clear flag C

# Check if multiple flags are set
if flags & (FLAG_B | FLAG_D):
    print("Either flag B or flag D is set!")

