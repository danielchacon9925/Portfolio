#define SegEn_ADDR    0x80001038
#define SegDig_ADDR   0x8000103C

.globl main
main:
  
    li t0, 0x80001400   # base address of GPIO memory-mapped registers
    li t1, 0xFFFF       # set direction of GPIOs
                      # upper half = switches (inputs)  (=0)
                      # lower half = outputs (LEDs)     (=1)
    sw t1, 8(t0)        # GPIO_INOUT = 0xFFFF
    
    li t2, SegEn_ADDR   # Load direction to enable 7SegDisplay
    li t6, 0xF0         # Enable las 4 digits
    sb t6, 0(t2)	    # Enable the 7SegDisplays


repeat:



    li t3, SegDig_ADDR  # Print direction
    lw   t6, 0(t0)      # read switches: t1 = GPIO_SWs
    srli t6, t6, 16     # shift val to the right by 16 bits
    sw t6, 0(t3)        # Save in print direction value in switches

    j    repeat         # repeat loop


# next:	beq zero, zero, next

# .end
