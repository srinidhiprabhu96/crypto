#include<stdio.h>
#include<stdint.h>
#include "common.c"
#include<time.h>
#include<math.h>


// For plotting
int main()
{
	FILE *fp,*fpw;
	char buffer;
	char file_pt[100],file_ct[100];
	int i;
	union bits128 cptxt,value;
	for(i=5;i<=20;i++)
	{
		sprintf(file_pt,"plaintext/%d.txt",i);
		sprintf(file_ct,"ciphertext/%d_ct.txt",i);
		fp = fopen(file_pt,"rb");
		fpw = fopen(file_ct,"wb");
		int size,j;
		fseek(fp, 0L, SEEK_END);
		size = ftell(fp);
		rewind(fp);
		clock_t time = 0,start,end;
		for(j=0;j<size/16;j++)
		{
			value = read_16_bytes(fp);
			start = clock();
			cptxt.integer = encrypt(value.integer, 0xabcdef0987654321);
			end = clock();
			time += (end - start);
			write_16_bytes(fpw,cptxt);
		}
		printf("%lf\n",pow(2,i));
		printf("%lf\n",(double)(time)/CLOCKS_PER_SEC);
	}
	return 0;
}
