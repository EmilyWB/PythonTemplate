
#include <stdlib.h>
#include <stdint.h>
#include <math.h>

uint32_t LeftShift(uint32_t value, uint32_t shift) 
{
    uint32_t output;
    output = value << shift;
    return output;
}

uint8_t GetHighNibble(uint8_t value)
{
    return ((value & 0xF0) >> 4);
}

