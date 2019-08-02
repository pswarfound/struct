#include "rte_ethdev.h"
extern void struct_struct_rte_eth_dev_info_print(struct rte_eth_dev_info *t, char *buf, int sz);
int main(int argc, char **argv)
{
    char buf[4096] = {0};
    struct rte_eth_dev_info devinfo;

    struct_struct_rte_eth_dev_info_print(&devinfo, buf, sizeof(buf));
    printf(buf);
    return 0;
}