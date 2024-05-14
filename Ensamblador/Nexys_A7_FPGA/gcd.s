
# GPIO_SWs   = 0x80001400
# GPIO_LEDs  = 0x80001404
# GPIO_INOUT = 0x80001408

.globl main
main: 
    
    jal loaddata
    jal gcd


loaddata:
    li s2, 20   # Valor a
    li s1, 10   # Valor b

    jr ra

gcd:

 	addi	sp, sp, -24	# espacio en stack para 4 variables

	sw	a1, 20(sp)	# $ra en stack 
	sw	s2, 16(sp)	# a=$s0 en stack
	sw	s1, 12(sp)	# b=$s1 en stack
	sw	a0, 8(sp)	# a= user input 
	sw	ra, 4(sp)	# b= user input	
		
		
	beq	s2, zero, return_b	# if (a == 0): return b
		
	beq	s1, zero, return_a	# if (b == 0) return a
	
	div	t1, s2, s1	# a/b

	# mfhi	t1		# $t1 = residuo
		
	lw	s2, 16(sp)	# Leer datos de $s0
	add	s2, s1, zero	# b = a
	sw	s2, 8(sp)	# Sobreescribir $s0 con valor de b
		
	lw	s1, 12(sp)	# Leer datos de $s1
	add	s1, t1, zero	# residuo = b
	sw	s1, 4(sp)	# Sobreescribir $s1 con valor de residuo
		
	jal gcd	  


exit:
	lw	ra, 4(sp)
	lw	a0, 8(sp)
	lw	s1, 12(sp)
	lw	s2, 16(sp)
	lw	a1, 20(sp)
	add	sp, sp, 24
 
    jr ra    


return_b:
    	
    lw	s1, 12(sp)
    # print b		        
		
    j       exit
 
return_a:
     	
    lw	s2, 16(sp)
    # print a
      		
      		
    j       exit

