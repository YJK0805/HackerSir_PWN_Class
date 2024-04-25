all: src/bof.c
	gcc src/bof.c -o ./bof/share/bof -fno-stack-protector
	gcc src/ret2code.c -o ./ret2code/share/ret2code -fno-stack-protector -no-pie
	gcc src/got.c -o ./got/share/got -fno-stack-protector -no-pie

clean:
	rm bof/share/bof ret2code/share/ret2code got/share/got
