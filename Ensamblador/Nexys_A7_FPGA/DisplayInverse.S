// memory-mapped I/O addresses
# GPIO_SWs = 0x80001400
# GPIO_LEDs = 0x80001404
# GPIO_INOUT = 0x80001408

.data
A: .word 0

.global main

main:
li t0, 0x80001400 # base address of GPIO memory-mapped registers 
li t1, 0xFFFF # set direction of GPIOs
# upper half = switches (inputs) (=0)
# lower half = outputs (LEDs) (=1)
sw t1, 8(t0) # GPIO_INOUT = 0xFFFF


repeat:

li t2, 0xFFFFFFFF

lw t1, 0(t0) # read switches: t1 = GPIO_SWs

xor t1, t1, t2

sw t1, 4(t0)

srli t1, t1, 16 # shift val to the right by 16 bits

sw t1, 4(t0) # write value to LEDs: GPIO_LEDs = t1
j repeat # repeat loop