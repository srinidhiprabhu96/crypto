#include<stdio.h>

__uint128_t read_16_bytes(FILE *fp)
{
	__uint128_t ret_val = 0;
	char buffer;
	int i;
	for(i=0;i<16;i++)
	{
		fread(&buffer, 1, 1, fp);
		ret_val = ret_val*256 + buffer;
		//ret_val += buffer;
		printf("%d\n",(256+(int)buffer)%256);
	}
	return ret_val;
}

void print_16_bytes(__uint128_t value)
{
	__uint128_t temp;
	int i,byte;
	for(i=0;i<16;i++)
	{
		byte = (int)value%256;
		printf("%d\n",(256+(int)byte)%256);
		value = value/256;
	}
}

// For testing
int main()
{
	FILE *fp;
	fp = fopen("../File Generator/5.txt","rb");
	char buffer;
	__uint128_t value;
	value = read_16_bytes(fp);
	printf("YO!\n");
	print_16_bytes(value);
	return 0;
}
