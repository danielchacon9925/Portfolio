#Tarea 1
#Estudiante: Daniel Chacón Mora
#Carné: B72018
#El programa siguiente tiene el objetivo de devolver el resultado de una función de sucesión recursiva

.data
	separator: .asciiz ","
	newline: .asciiz "\n"
	valor: .asciiz "Ingrese n: \n"
	space:  .asciiz   " "
	new_line:  .asciiz   "\n"

.text
	main:
		#la 	$a0, valor
		ori     $v0, $0, 5          # opcode to read user i/p
		syscall
    		ori     $a0, $v0, 0         # entrada de usuario en $a0
    		jal     sucesion            #llamada a la función de sucesión
    		jal     print
    		ori     $v0, $0, 10         #comando para detener programa
    		syscall 	

		
	sucesion:
    		addiu   $sp, $sp, -20        # espacio en stack
    		sw      $ra, 16($sp)         # $ra en stack
    		sw      $s0, 12($sp)         # $s0 en stack
    		sw      $s1, 8($sp)         # $s1 en stack
		sw 	$a0, 4($sp)
 		addiu   $t1, $zero, 1	    #$t1=1 comparativo
 		addiu   $t2, $zero, 2	    #$s2=2 comparativo		
 
 		
    		ori     $s0, $a0, 0         # guardo valor de n en $s0
    		beq     $s0, $t1, return_0  # if (n == 1) => return 1
    		beq     $s0, $t2, return_2  # if (n == 2) => return 2
    			
		addi    $a0, $s0, -1        #$a0 = n -1
      		jal     sucesion            # a(n - 1)
		sll     $s1, $v0, 1	    #$s1=2*a(n-1)
    		sw      $s1, 8($sp)         # $s1 en stack
		lw 	$a0, 4($sp)
		
		addi    $a0, $a0, -2	    #$a0=n-2
		jal     sucesion	    #a(n-2)
		

		lw 	$s1, 8($sp)	    #carga valor de #s1
		add 	$v0, $s1, $v0	    #2*a(n-1)+a(n-2)		

	
						
    	exit:

      		lw      $s1, 8($sp)        # restaura $s1
      		lw      $s0, 12($sp)       # restaura $s0
      		lw      $ra, 16($sp)       # restaura $ra
      		addi    $sp, $sp, 20       # restaura puntero $sp
 
      		jr      $ra                # return $v0
      		
	print:
		addiu	$sp, $sp, -8
		sw	$ra, 4($sp)
		sw	$v0, 0($sp)
 
    		ori     $a0, $v0, 0         # returned value into $a0
    		ori     $v0, $0, 1          # opcode to print an integer
    		syscall
    		la      $a0, space          # store base address in $a0
    		ori     $v0, $0, 4          # opcode to print string
    		syscall
    		la      $a0, new_line       # store base address in $a0
    		ori     $v0, $0, 4          # opcode to print string
    		syscall
 		
 		lw	$v0, 0($sp)
 		lw 	$ra, 4($sp)
 		addi	$sp, $sp, 8

    		jr      $ra                 # return
    		
    	return_0:
      		addi    $v0, $0, 0          # return 0
      		j       exit
 
     	return_2:
      		addi    $v0, $0, -2         # return 2
      		j       exit
