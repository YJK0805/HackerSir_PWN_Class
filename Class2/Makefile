all: src/ret2sc.c src/orw.c src/rop.c src/format_string1.c src/format_string2.c
	gcc src/ret2sc.c -o ./ret2sc/share/ret2sc -fno-stack-protector -no-pie
	gcc src/orw.c -o ./orw/share/orw -fno-stack-protector -no-pie
	gcc src/rop.c -o ./rop/share/rop -fno-stack-protector -no-pie --static
	gcc src/format_string1.c -o ./format_string1/share/format_string1 -fno-stack-protector -no-pie -m32
	gcc src/format_string2.c -o ./format_string2/share/format_string2 -fstack-protector -m32
clean:
	rm ret2sc/share/ret2sc orw/share/orw rop/share/rop format_string1/share/format_string1 format_string2/share/format_string2
