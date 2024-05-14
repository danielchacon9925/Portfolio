// memory-mapped I/O addresses
# GPIO_SWs   = 0x80001400
# GPIO_LEDs  = 0x80001404
# GPIO_INOUT = 0x80001408

.globl main


main:

    li t0, 0x80001400   # base address of GPIO memory-mapped registers
    li t1, 0xFFFF       # set direction of GPIOs
    sw t1, 8(t0)        # GPIO_INOUT = 0xFFFF

    # Máscaras
    li s0, 0x000F0000   # mask a
    li s1, 0xF0000000   # mask b

    sw s0, 12(t0)       # Guardo valores de máscara a
    sw s1, 16(t0)       # Guardo valores de máscara b

repeat:

    # Hago lectra de máscaras

    lw s0, 12(t0)
    lw s1, 16(t0)

    # Se lee el ingreso de usuario
    lw   t1, 0(t0)      # read switches: t1 = GPIO_SWs

    # Leer switch menos significativo (a)
    and t2, t1, s0

    # Leer switch más significativo (b)
    and t3, t1, s1

    # Se pasa el b del otro lado
    srli t3, t3, 12 # shift val to the right by 12 bits

    # Num = a + b 
    add t4, t2, t3

    srli t4, t4, 16 # shift val to the right by 16 bits

    sw   t4, 4(t0)      # write value to LEDs: GPIO_LEDs = t1
    j    repeat         # repeat loop

