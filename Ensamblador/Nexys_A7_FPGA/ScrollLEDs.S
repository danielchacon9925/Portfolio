// memory-mapped I/O addresses
# GPIO_SWs   = 0x80001400
# GPIO_LEDs  = 0x80001404
# GPIO_INOUT = 0x80001408

.globl main


main:
    jal condicionesiniciales
    jal scrollLEDs


condicionesiniciales:

    li s0, 0        # s1 = contador de ciclo
    li s1, 0x00000001   # s2 = Valor de inicio de subida
    li s2, 0x80000000   # s3 = valor de inicio de bajada
    li s3, 16       # s3 = límite de subida(16)
    li s4, 32       # s4 = límite de bajada(32)
    li s5, 1        # Iteración(inicia en 1)

    li t0, 0x80001400   # base address of GPIO memory-mapped registers
    li t1, 0xFFFF       # set direction of GPIOs
                      # upper half = switches (inputs)  (=0)
                      # lower half = outputs (LEDs)     (=1)
    sw t1, 8(t0)  
    li s6, 0        # Contador de ciclo = 0

    jal scrollLEDs

scrollLEDs: 

    # Abro la pila
    addi sp, sp, -36
    sw  s6, 32(sp)  # Puntero de regreso
    sw  s5, 28(sp)  # Contador del ciclo
    sw  s4, 24(sp)  # Valor de inicio de subida
    sw  s3, 20(sp)  # Valor de inicio de bajada
    sw  s2, 16(sp)  # Límite de contador de subida para hacer branch
    sw  s1, 12(sp)  # Límite de contador de bajada para hacer branch
    sw  s0, 8(sp)   # Número de iteración n
    sw  ra, 4(sp)   # Contador 

    # Update 

    # ifs 
    blt s6, s3, subida
    bge s6, s3, bajada 

    # Valor de subida
    lw s1, 12(sp)
    addi t1, s5, 1  # (n+1)
    sll t2, s1, t1  # (1<<(n+1))
    addi s1, t2, -1 # (0x0001 << (n + 1)) - 1
    sw s1, 12(sp)

    # Valor final de bajada

    lw s2, 16(sp)
    srl t3, s2, s5     # (0x8000 >> n)
    add s2, t3, s2     # (0x8000 >> n) + final 
    sw s2, 16(sp)
 

    addi s5, s5, 1  # n++

    # Si se completan ciclos, se termina
    # beq s0, s3, end  
  


    lw  s6, 32(sp)  # Puntero de regreso
    lw  s5, 28(sp)  # Contador del ciclo
    lw  s4, 4(t0)  # Valor de inicio de subida
    lw  s3, 4(t0)  # Valor de inicio de bajada
    lw  s2, 16(sp)  # Límite de contador de subida para hacer branch
    lw  s1, 12(sp)  # Límite de contador de bajada para hacer branch
    lw  s0, 8(sp)   # Número de iteración
    lw  ra, 4(sp)   # Contador

    addi sp, sp, 36


    jal scrollLEDs
    

# end:
    # lw  s6, 32(sp)  # Puntero de regreso
    # lw  s5, 28(sp)  # Contador del ciclo
    # lw  s4, 4(t0)  # Valor de inicio de subida
    # lw  s3, 4(t0)  # Valor de inicio de bajada
    # lw  s2, 16(sp)  # Límite de contador de subida para hacer branch
    # lw  s1, 12(sp)  # Límite de contador de bajada para hacer branch
    # lw  s0, 8(sp)   # Número de iteración
    # lw  ra, 4(sp)   # Contador        


    

subida: 

    # Mostrar valor
    add a1, zero, s1    # valor de subida es de escritura
    sll s1, s1, 1      # subida << 1
    sw  s1, 12(sp)

    # lw   t1, 0(t0)    
    mv t1, a1           # t1 = a1
    sw t1, 4(t0)
    slli t1, t1, 16


    srli t1, t1, 16     # shift val to the right by 16 bits
    lw   t1, 0(t0)

    lw s6, 32(sp)
    addi s6, s6, 1      # j++
    sw s6, 32(sp)        # se guarda j
    jr ra


bajada: 
    # Mostrar valor
    add a1, zero, s2    # valor de subida es de escritura
    srli s2, s2, 1      # bajada >> 1
    sw s2, 16(sp)
  

    
    mv t1, a1           # t1 = a1
    sw t1, 4(t0)
    # slli t1, t1, 16

    srli t1, t1, 16     # shift val to the right by 16 bits
    lw   t1, 0(t0)

    lw s6, 32(sp)
    addi s6, s6, 1      # j++
    sw s6, 32(sp)        # se guarda j
    jr ra

