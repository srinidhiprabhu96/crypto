all: compile

compile:
	gcc encrypt.c -o encrypt.out
	gcc decrypt.c -o decrypt.out
	gcc plot_encrypt.c -o plot_encrypt.out -lm
	gcc plot_decrypt.c -o plot_decrypt.out -lm

plot_encrypt:
	./plot_encrypt.out | plotter.py

plot_decrypt:
	./plot_decrypt.out | plotter.py

clean:
	rm *.out
