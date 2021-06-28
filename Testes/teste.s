.global main

main:
push {ip, lr}
LDR R0, =format
LDR R1,= n1
BL scanf

LDR R0,=format
LDR R1,= n2
BL scanf

ldr r0, = n1
ldr r0, [r0]
push {r0}

ldr r0, = n2
ldr r0, [r0]
push {r0}

pop {r1}
pop {r0}

add r0, r0,r1
push {r0} @resultado contido em r0 empilhado

pop {r1}
LDR R0, =soma
STR R1,[R0]
LDR R0, = format
BL printf
pop {ip, pc}
.data
	.balign 8
	format: .asciz "%d"

	.balign 8
	n1: .word 0

	.balign 8
	n2: .word 0

	.balign 8
	soma: .word 0

.global printf
.global scanf

