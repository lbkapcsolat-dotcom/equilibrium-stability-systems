#include <stdint.h>

uint32_t ess_accumulate(const uint16_t *values, uint32_t n) {
    uint32_t total = 0;
    for (uint32_t i = 0; i < n; ++i) {
        total += values[i];
    }
    return total;
}
