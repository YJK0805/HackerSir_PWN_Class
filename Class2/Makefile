all: src/ret2sc.c src/orw.c src/rop.c src/FormatString1.c src/FormatString2.c
	gcc src/ret2sc.c -o ./ret2sc/share/ret2sc -fno-stack-protector -no-pie
	gcc src/orw.c -o ./orw/share/orw -fno-stack-protector -no-pie
	gcc src/rop.c -o ./rop/share/rop -fno-stack-protector -no-pie --static
	gcc src/FormatString1.c -o ./FormatString1/share/FormatString1 -fno-stack-protector -no-pie -m32
	gcc src/FormatString2.c -o ./FormatString2/share/FormatString2 -fstack-protector -m32
clean:
	rm ret2sc/share/ret2sc orw/share/orw rop/share/rop FormatString1/share/FormatString1 FormatString2/share/FormatString2
