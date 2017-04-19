1) To compile:
      make compile
2) To generate the plaintext files of different sizes
	python file_gen.py
	These files will be saved in the "plaintext" folder.
3) To encrypt a file(using counter mode of operation):
      ./encrypt <path_to_plaintext_file> <path_to_output_file> <key_file>
      These files will be saved in the "ciphertext" folder.
4) To decrypt a file(using counter mode of operation):
      ./decrypt <path_to_ciphertext_file> <output_file> <key_file>
      These files will be saved in the "decryptedtext" folder.
5) To plot time vs file size graphs:
      make plot_encrypt
      make plot_decrypt      
6) To remove binaries:
	make clean
7) To remove the PT, CT and decrypted text files
	make removefiles
8) To check that the decryption of the cipher text gives the plaintext
	diff plaintext/$i.txt decryptedtext/$i.txt where $i is any number from 5 to 20.
	OR
	make check_diff
