#include <stdio.h>

const __uint8_t sbox[8][256] = {{103,23,239,232,248,159,255,119,135,247,111,239,143,144,112,240,136,111,23,231,104,103,144,255,103,135,111,16,24,16,31,136,16,255,232,224,247,31,7,135,224,31,247,119,111,31,231,143,232,15,135,23,112,240,119,248,136,15,232,8,240,96,255,112,152,0,16,232,255,16,255,0,248,120,128,31,0,24,255,255,152,103,120,255,31,7,152,135,255,7,128,135,224,152,127,152,24,24,152,231,128,127,103,0,128,0,231,24,103,247,239,239,247,152,128,239,8,152,111,255,255,103,111,239,111,239,255,24,103,16,119,231,144,152,16,152,8,16,231,136,152,120,239,143,239,96,135,96,248,127,0,247,111,96,24,135,103,111,232,23,232,23,159,255,159,135,231,104,8,96,16,112,0,0,8,159,128,144,247,8,255,16,111,0,135,103,135,144,232,159,7,15,248,104,7,128,8,104,24,31,96,104,144,255,128,231,224,31,119,135,96,144,96,8,127,7,247,144,7,127,119,128,119,240,143,24,120,119,16,120,127,112,136,119,128,31,119,136,16,96,151,143,23,0,144,24,136,240,152,255,144,120,119,111,239,248},
{66,238,238,238,255,82,66,12,239,78,61,156,61,194,161,255,206,198,20,37,49,214,28,57,136,20,103,136,70,37,53,136,165,251,247,251,169,210,45,218,82,4,255,90,4,161,245,229,239,16,163,247,225,175,76,175,179,233,80,225,66,212,59,115,74,189,92,237,8,189,30,167,14,245,173,14,191,229,20,22,22,177,163,90,66,158,249,253,167,196,37,235,59,2,72,112,99,200,242,71,160,46,221,208,43,204,54,246,35,223,223,67,151,223,171,79,149,130,73,49,115,33,125,164,216,215,175,90,95,119,139,7,165,6,242,217,81,253,242,221,213,120,133,8,139,252,2,162,125,136,248,9,171,121,9,248,106,180,244,145,214,152,41,188,180,216,212,10,10,11,104,10,185,230,185,255,218,245,245,40,181,138,148,0,180,94,190,116,171,180,43,32,192,11,97,65,223,42,225,53,191,171,117,94,20,4,47,225,80,0,218,43,101,214,82,24,208,14,88,76,18,107,212,214,247,173,33,6,57,251,78,16,215,2,239,206,32,118,71,51,126,152,3,0,56,8,35,59,207,207,84,35,223,68,85,32},
{51,55,251,55,55,4,55,55,200,51,4,255,255,4,255,243,247,4,0,12,255,243,0,255,196,0,55,243,59,255,59,251,247,255,204,204,243,59,63,8,0,255,4,8,251,251,12,243,255,12,251,8,60,255,4,0,60,0,255,195,247,8,8,243,255,251,255,251,255,0,4,4,4,4,248,11,251,7,8,247,203,12,4,8,0,255,243,243,247,4,56,252,255,192,255,204,55,204,4,0,192,251,251,196,63,11,251,4,251,192,255,51,63,4,63,255,55,8,192,251,255,192,196,199,12,8,63,8,8,200,55,200,204,51,51,8,8,12,196,204,251,59,51,200,196,251,8,243,200,243,4,251,55,4,0,59,192,192,251,0,196,63,63,192,192,63,63,63,63,255,192,192,192,192,255,63,243,243,243,0,0,0,243,255,12,255,255,12,204,243,0,51,63,63,192,0,63,63,0,0,4,0,0,192,0,0,196,192,255,0,192,255,192,196,192,63,4,4,243,196,55,255,251,255,251,255,59,196,63,4,0,255,255,4,255,248,0,251,0,204,255,251,0,255,255,0,0,255,204,4,51,4,8,4,12,0},
{117,254,239,0,21,252,7,250,251,3,237,254,253,0,22,19,23,5,20,250,251,250,21,1,255,0,0,119,0,136,136,119,0,119,136,137,142,153,23,17,157,7,239,248,6,233,0,142,97,3,112,17,237,153,18,19,99,249,16,0,119,136,16,255,102,136,102,102,3,155,0,103,1,252,255,6,152,250,153,100,5,103,0,255,0,253,118,0,0,2,255,255,3,255,255,255,3,253,253,1,2,116,254,255,143,158,158,158,116,96,97,97,1,97,96,255,96,0,1,255,255,254,140,255,115,253,0,252,252,0,254,112,1,113,143,142,0,0,0,158,113,239,16,159,238,156,99,0,0,1,236,18,19,16,98,98,239,154,255,113,154,159,158,254,158,17,255,239,239,96,118,138,255,239,255,0,128,239,16,238,3,254,237,19,253,229,255,253,253,1,253,234,1,1,20,254,254,0,129,128,159,1,139,116,255,4,158,240,148,124,155,107,112,244,97,11,254,158,123,10,132,11,158,149,98,255,238,97,159,0,97,0,2,112,142,140,3,2,236,2,236,253,124,153,23,107,105,235,238,0,239,254,234,253,1,238},
{111,239,0,255,255,111,144,16,128,127,111,128,83,16,44,160,156,243,243,176,0,172,243,115,16,140,28,128,99,0,243,188,127,16,18,28,79,227,65,62,178,17,145,28,226,175,129,65,128,65,111,156,0,77,144,16,140,220,47,179,163,76,239,192,239,255,239,191,115,175,80,220,18,140,173,142,125,127,127,2,222,111,161,144,241,28,0,115,140,111,239,255,99,33,61,195,172,108,17,127,17,145,34,146,34,179,0,179,110,92,110,92,253,253,237,253,177,177,78,239,161,78,78,161,177,0,16,128,144,239,12,28,255,1,114,115,12,77,144,158,81,239,161,32,223,142,225,127,65,223,144,142,95,142,62,14,207,99,243,156,67,111,95,67,83,241,111,32,65,142,193,142,207,204,207,147,255,236,127,178,51,0,204,108,16,108,220,50,50,93,76,255,178,145,178,127,0,109,77,147,253,239,126,76,18,254,19,128,110,144,108,97,108,204,92,79,177,130,51,179,94,204,95,35,146,176,32,178,239,125,178,17,112,142,226,95,204,147,111,76,34,2,18,175,255,16,252,128,111,255,144,0,176,63,175,240},
{255,159,96,0,159,0,132,255,4,224,252,251,227,131,100,100,155,227,131,28,28,3,231,231,99,231,251,0,103,152,99,103,156,0,227,28,28,251,124,4,0,116,128,11,4,112,127,0,0,0,0,0,255,255,0,127,127,127,255,255,127,127,132,4,255,0,123,16,255,159,228,0,159,24,24,231,0,255,135,247,255,96,151,247,247,96,8,0,0,0,0,16,239,0,16,255,0,239,0,0,0,155,116,96,235,235,20,235,28,239,16,235,147,4,100,159,0,108,255,4,159,251,100,255,0,139,255,139,4,143,255,8,247,255,251,255,108,108,247,159,255,255,155,100,251,4,255,100,96,100,4,255,255,251,155,96,24,28,255,28,24,24,20,239,159,255,155,100,4,100,155,139,96,20,235,112,139,159,143,159,227,247,235,227,20,159,96,159,131,96,96,243,143,16,0,0,159,239,143,131,151,104,159,0,120,4,0,100,251,120,143,116,96,139,20,120,120,120,135,151,104,0,155,155,139,159,147,120,148,239,159,251,4,120,159,124,227,112,119,20,116,0,0,155,116,232,0,123,15,244,224,155,235,144,240,236},
{8,48,199,56,255,184,64,119,248,0,63,120,200,112,79,135,0,127,63,52,132,0,71,115,255,115,184,180,132,8,243,132,127,124,251,15,243,123,131,112,131,255,252,115,136,0,255,8,247,0,192,48,248,7,123,184,4,207,180,55,255,7,79,55,120,180,207,131,76,0,255,76,247,255,207,207,59,0,56,0,48,48,244,188,75,120,207,120,136,127,112,183,64,199,0,179,251,247,52,247,195,60,60,243,48,0,60,195,207,207,12,4,56,251,12,255,12,207,207,48,60,195,207,207,255,243,195,255,243,195,60,60,207,207,0,203,4,56,12,251,195,56,207,12,195,180,132,132,132,79,176,71,255,247,8,255,48,184,128,184,71,0,56,120,64,184,184,184,135,128,120,255,56,64,135,64,56,191,191,135,240,112,176,15,127,128,255,128,75,4,0,131,135,127,203,4,183,251,60,75,124,15,135,255,0,51,76,59,120,119,176,203,64,128,60,8,187,135,64,75,123,135,0,199,3,71,196,64,71,51,123,12,179,11,112,207,196,51,3,247,140,180,8,188,207,0,255,207,0,79,127,199,12,247,203,180},
{63,247,35,204,218,45,239,247,14,255,115,0,235,14,28,152,128,138,154,128,134,101,99,125,255,130,144,97,113,144,237,142,14,239,227,192,222,238,255,0,194,115,112,210,32,2,173,172,127,82,115,33,7,115,86,219,162,210,34,0,93,127,13,128,240,128,34,128,32,93,255,61,231,39,229,253,194,191,130,253,38,36,2,81,8,130,18,146,253,50,46,14,255,35,12,79,64,26,199,255,58,42,213,127,143,0,80,239,189,189,157,141,253,114,175,34,2,255,128,240,240,13,127,13,162,246,221,162,221,0,230,56,253,128,251,255,121,157,2,2,253,155,159,2,0,255,96,255,159,2,253,96,146,249,96,111,144,96,157,13,240,255,9,11,159,107,246,9,159,98,121,2,144,157,15,96,146,146,15,109,13,141,125,146,0,26,253,247,245,8,245,8,247,16,239,114,159,112,156,253,2,156,99,140,72,18,237,151,0,181,0,34,239,112,112,191,112,2,80,66,13,253,64,2,253,95,31,160,255,191,64,64,188,29,174,66,237,81,64,67,173,175,81,81,16,253,255,66,92,76,237,92,237,253,94,253}};

__uint64_t fbox(__uint64_t in){
  __uint64_t out = 0, temp = 0;
  int i;
  for(i = 0; i < 8; i++){
    out = out | ((sbox[i][(in>>(56-8*i)) & 0xff])<<(56-8*i));
  }
  return out;
}

__uint128_t rnd(__uint128_t in, __uint128_t key){
  __uint64_t right = in & 0xffffffffffffffff,
             left = (in>>64) & 0xffffffffffffffff;
  __uint128_t out = 0;
  out = fbox(left) ^ right;
  out = out<<64;
  out = out | left;
  out = out ^ key;
  return out;
}

__uint128_t dec_rnd(__uint128_t in, __uint128_t key){
  __uint128_t out=0;
  in = in ^ key;
  __uint128_t right = in & 0xffffffffffffffff,
             left = (in>>64) & 0xffffffffffffffff;
   out = right;
   out = out<<64;
   out = out | (fbox(right) ^ left);
   return out;
}

__uint128_t diff(__uint128_t in){
  __uint128_t out = 0;
  __uint128_t temp = 0;
  int i,j,new_bit,new_byte;
  for(i = 0; i < 16; i++){
    for(j = 0; j < 8; j++){
      temp = in>>(128-8*i);   //get i'th byte
      temp = (temp>>j) & 1;   //get j'th bit in lsb
      new_bit = ((i*8)+j)/16;
      new_byte = ((i*8)+j)%16;
      temp = temp<<new_bit;
      temp = temp<<(new_byte*8);
      out = out | temp;
    }
  }
  return out;
}

__uint128_t diff_inv(__uint128_t in){
  __uint128_t out = 0;
  __uint128_t temp = 0;
  int i,j,new_bit,new_byte;
  for(i = 0; i < 16; i++){
    for(j = 0; j < 8; j++){
      temp = in>>(128-8*i);   //get i'th byte
      temp = (temp>>j) & 1;   //get j'th bit in lsb
      if(i < 8){
        new_bit = i;
        new_byte = 2*j;
      }
      else{
        new_bit = i-8;
        new_byte = 2*j+1;
      }
      temp = temp<<new_bit;
      temp = temp<<(new_byte*8);
      out = out | temp;
    }
  }
  return out;
}

__uint128_t encrypt(__uint128_t in, __uint128_t key){   //didnt implement round key algo
  __uint128_t temp1,temp2;
  int i;
  temp1 = in;
  for(i = 0; i < 18; i++){
    temp2 = rnd(temp1, key);
    // temp1 = diff(temp2);
    temp1 = temp2;
  }
  for(i = 0; i < 2; i++){
    temp1 = rnd(temp1, key);
  }
  return temp1;
}

__uint128_t decrypt(__uint128_t in, __uint128_t key){   //didnt implement round key algo
  __uint128_t temp1,temp2;
  int i;
  temp2 = in;
  for(i = 0; i < 2; i++){
    temp2 = dec_rnd(temp2, key);
  }
  for(i = 0; i < 18; i++){
    // temp1 = diff_inv(temp2);
    temp1 = temp2;
    temp2 = dec_rnd(temp1, key);
  }
  return temp2;
}

// int main(){
//   printf("%lu\n",sizeof(sbox));
//   return 0;
// }
