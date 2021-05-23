.text
main:
sub $sp $sp 120
move $fp $sp 
# This is a code func : integer:=  
lw $t1 12($sp) 
li $t1 23 
sw $t1 12($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : integer:=  
lw $t1 0($sp) 
lw $t2 12($sp) 
move $t1 $t2 
sw $t1 0($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : integer:=  
lw $t1 16($sp) 
li $t1 0 
sw $t1 16($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : integer:=  
lw $t1 4($sp) 
lw $t2 16($sp) 
move $t1 $t2 
sw $t1 4($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : integer:=  
lw $t1 20($sp) 
li $t1 1 
sw $t1 20($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : integer:=  
lw $t1 8($sp) 
lw $t2 20($sp) 
move $t1 $t2 
sw $t1 8($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : label  
label_1 :  
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : integer:=  
lw $t1 24($sp) 
li $t1 10 
sw $t1 24($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : intmod  
lw $t1 28($sp) 
lw $t2 0($sp) 
lw $t3 24($sp) 
rem $t1 $t2 $t3
sw $t1 28($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : int+  
lw $t1 32($sp) 
lw $t2 4($sp) 
lw $t3 28($sp) 
add $t1 $t2 $t3
sw $t1 32($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : integer:=  
lw $t1 4($sp) 
lw $t2 32($sp) 
move $t1 $t2 
sw $t1 4($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : integer:=  
lw $t1 36($sp) 
li $t1 10 
sw $t1 36($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : intmod  
lw $t1 40($sp) 
lw $t2 0($sp) 
lw $t3 36($sp) 
rem $t1 $t2 $t3
sw $t1 40($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : int*  
lw $t1 44($sp) 
lw $t2 8($sp) 
lw $t3 40($sp) 
mul $t1 $t2 $t3
sw $t1 44($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : integer:=  
lw $t1 8($sp) 
lw $t2 44($sp) 
move $t1 $t2 
sw $t1 8($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : integer:=  
lw $t1 48($sp) 
li $t1 10 
sw $t1 48($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : intdiv  
lw $t1 52($sp) 
lw $t2 0($sp) 
lw $t3 48($sp) 
div $t1 $t2 $t3
sw $t1 52($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : integer:=  
lw $t1 0($sp) 
lw $t2 52($sp) 
move $t1 $t2 
sw $t1 0($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : integer:=  
lw $t1 56($sp) 
li $t1 0 
sw $t1 56($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : int>  
lw $t1 60($sp) 
lw $t2 0($sp) 
lw $t3 56($sp) 
slt $t1 $t3 $t2
sw $t1 60($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : IF_TRUE_GOTO  
lw $t1 60($sp) 
bne $t1 $zero label_1
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : string:=  
lw $t1 64($sp) 
la $t1 t17 
sw $t1 64($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : WRITE_STRING  
li $v0 4 
lw $a0 64($sp) 
syscall   
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : WRITE_INT  
li $v0 1 
lw $a0 4($sp) 
syscall   
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : WRITE_NL  
li $v0 11 
li $a0 10 
syscall   
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : string:=  
lw $t1 68($sp) 
la $t1 t18 
sw $t1 68($sp) 
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : WRITE_STRING  
li $v0 4 
lw $a0 68($sp) 
syscall   
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : WRITE_INT  
li $v0 1 
lw $a0 8($sp) 
syscall   
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
# This is a code func : WRITE_NL  
li $v0 11 
li $a0 10 
syscall   
# *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*  
li $v0, 10
syscall
.data
t17: .asciiz "Sum of digits = "
t18: .asciiz "Multiplication of digits = "
