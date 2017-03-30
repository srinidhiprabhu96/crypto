all: compile

compile:
	gcc encrypt.c -o encrypt.out
	gcc decrypt.c -o decrypt.out
	gcc plot_encrypt.c -o plot_encrypt.out -lm
	gcc plot_decrypt.c -o plot_decrypt.out -lm

plot_encrypt:
	./plot_encrypt.out | python plotter.py

plot_decrypt:
	./plot_decrypt.out | python plotter.py
	
check_diff:
	for i in 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20; do \
		diff plaintext/$${i}.txt decryptedtext/$${i}_dt.txt; \
	done

clean:
	rm *.out
	
removefiles:
	rm plaintext/*.txt
	rm ciphertext/*.txt
	rm decryptedtext/*.txt 
