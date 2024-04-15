#Tarea 1
#Estudiante: Daniel Chacón Mora
#Carné: B72018


.data
	separator: .asciiz ","
	newline: .asciiz "\n"
	valor: .asciiz "Ingrese n: \n"

.text
	main:

		addi $sp, $sp, -8	#Se guarda el espacio para 2 items
		sw $ra, 0($sp)		#Dirección de retorno
		la $a0,valor 		#Se muestra mensaje que pide ingresar entero

		jal nrecibe		#función que recibe n
		
	
		jal sucesion
		
		
		lw $ra, 0($sp)		#Vuelve dirección a main
		addi $sp, $sp, 8	#Elimina el espacio guardado
		li $v0, 10
		syscall
		jr $ra			#main

		
	sucesion:

		addi $sp, $sp, -16	#Reservo espacio para 4 datos en stock
		addi $t1, $zero, 1	#$s1=1 comparativo
		addi $t2, $zero, 2	#$s2=2 comparativo
		sw $ra, 4($sp)		#dirección de retorno
		sw $a1, 0($sp)		#direccion de valor ingresado
		#sw $s1, 8($sp)		#direccion de $s1
		#sw $s2, 12($sp)	#dirección de $s2
		
		slti $t0, $a1, 2	#si n>2 $t0=1
		beq $t0, $zero, L1	#si $t1>0, vaya a L1
		beq $a1,$t1, return_0	#si $a1=1, vaya a return 0
		beq $a1, $t2, return_2	#si $a1=2, vaya a return -2
		
		

		addi $sp, $sp, 16
		jr $ra
		
#Caso para cuando n>2
	L1:	
		addi $a1, $a1, -1	#n-1
		jal sucesion		#a(n-1)
		sll $s0, $v0, 1		#2*a(n-1)
		
		lw $a1, 0($sp)
		addi $a1, $a1, -2	#n-2
		jal sucesion		#a(n-2)
		
		lw $a1, 0($sp)		#argumento original
		lw $ra, 4($sp)		#carga donde se llamó
		addi $sp, $sp, 16	#remueve espacio guardado
		
		add $v0, $s0, $v0	#2*a(n-1)+a(n-2)
		
		jal print
		
		jr $ra
#Cuando n=1
	return_0:
		la $v0,($zero)
		add $v0, $zero, $zero	#$v0=0
		#lw $t1, 8($sp)
		lw $ra, 4($sp)
		syscall
		jr $ra
#Cuando n=2
	return_2:
		la $v0,($zero)
		addi $v0, $zero, -2	#$v0=-2
		#lw $t2, 12($sp)
		lw $ra, 4($sp)
		syscall
		jr $ra	

#imprime $a0
#	imprimestr:
#		la $v0, ($zero)
#		addi $v0,$v0, 4  		
#		syscall
#		jr $ra

#Función para recibir n:
	nrecibe:
		la $v0, ($zero)
		addi $v0, $v0, 4
		syscall
		jr $ra
#Función para imprimir:
	print:
		la $v0, ($zero)
		addi $v0, $v0, 1
		syscall
		jr $ra
		
		
		
		
		
		
		
		
		
		
		
		
		
