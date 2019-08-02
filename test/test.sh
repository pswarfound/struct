#!/bin/sh
ST_NAME=test_struct
python gen.py ${ST_NAME}.json ${ST_NAME}.c
gcc -E ${ST_NAME}.c -m64 -pthread -march=native -DRTE_MACHINE_CPUFLAG_SSE -DRTE_MACHINE_CPUFLAG_SSE2 -DRTE_MACHINE_CPUFLAG_SSE3 -DRTE_MACHINE_CPUFLAG_SSSE3 -DRTE_MACHINE_CPUFLAG_SSE4_1 -DRTE_MACHINE_CPUFLAG_SSE4_2 -DRTE_MACHINE_CPUFLAG_AES -DRTE_MACHINE_CPUFLAG_PCLMULQDQ -DRTE_MACHINE_CPUFLAG_AVX -DRTE_MACHINE_CPUFLAG_RDRAND -DRTE_MACHINE_CPUFLAG_FSGSBASE -DRTE_MACHINE_CPUFLAG_F16C -I/mnt/sda7/project/ppe/ppe/src/3rd/dpdk/build/include -I/mnt/sda7/project/ppe/ppe/src/3rd/dpdk/src/x86_64-native-linuxapp-gcc/include -include /mnt/sda7/project/ppe/ppe/src/3rd/dpdk/src/x86_64-native-linuxapp-gcc/include/rte_config.h -D_GNU_SOURCE > ${ST_NAME}.e
python st.py ${ST_NAME}.json ${ST_NAME}.e ${ST_NAME}_impl.c
