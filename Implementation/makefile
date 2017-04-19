all: compile

compile:
	gcc encrypt.c -o encrypt.out -O3
	gcc decrypt.c -o decrypt.out -O3
	gcc plot_encrypt.c -o plot_encrypt.out -lm -O3
	gcc plot_decrypt.c -o plot_decrypt.out -lm -O3

plot_encrypt:
	./plot_encrypt.out | python plotter.py

plot_decrypt:
	./plot_decrypt.out | python plotter.py

clean:
	rm *.out
