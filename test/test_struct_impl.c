#include "rte_ethdev.h"
#include "rte_mempool.h"

void struct_struct_rte_mempool_print(struct rte_mempool *t, char *buf, int sz)
{
    int ret;
    char *p=buf;
    int left = sz;
    ret = snprintf(p, left, "struct rte_mempool: \n");p += ret;left -= ret;
    ret = snprintf(p, left, "    name: \n", t->name);p += ret;left -= ret;
    ret = snprintf(p, left, "    pool_config: %p\n", t->pool_config);p += ret;left -= ret;
    ret = snprintf(p, left, "    mz: %p\n", t->mz);p += ret;left -= ret;
    ret = snprintf(p, left, "    flags: %x\n", t->flags);p += ret;left -= ret;
    ret = snprintf(p, left, "    socket_id: %x\n", t->socket_id);p += ret;left -= ret;
    ret = snprintf(p, left, "    size: %x\n", t->size);p += ret;left -= ret;
    ret = snprintf(p, left, "    cache_size: %x\n", t->cache_size);p += ret;left -= ret;
    ret = snprintf(p, left, "    elt_size: %x\n", t->elt_size);p += ret;left -= ret;
    ret = snprintf(p, left, "    header_size: %x\n", t->header_size);p += ret;left -= ret;
    ret = snprintf(p, left, "    trailer_size: %x\n", t->trailer_size);p += ret;left -= ret;
    ret = snprintf(p, left, "    private_data_size: %x\n", t->private_data_size);p += ret;left -= ret;
    ret = snprintf(p, left, "    ops_index: %x\n", t->ops_index);p += ret;left -= ret;
    ret = snprintf(p, left, "    local_cache: %p\n", t->local_cache);p += ret;left -= ret;
    ret = snprintf(p, left, "    populated_size: %x\n", t->populated_size);p += ret;left -= ret;
    ret = snprintf(p, left, "    elt_list: \n");p += ret;left -= ret;
    ret = snprintf(p, left, "        stqh_first: %p\n", t->elt_list.stqh_first);p += ret;left -= ret;
    ret = snprintf(p, left, "        stqh_last: %p\n", t->elt_list.stqh_last);p += ret;left -= ret;
    ret = snprintf(p, left, "    nb_mem_chunks: %x\n", t->nb_mem_chunks);p += ret;left -= ret;
    ret = snprintf(p, left, "    mem_list: \n");p += ret;left -= ret;
    ret = snprintf(p, left, "        stqh_first: %p\n", t->mem_list.stqh_first);p += ret;left -= ret;
    ret = snprintf(p, left, "        stqh_last: %p\n", t->mem_list.stqh_last);p += ret;left -= ret;
}

void struct_struct_rte_eth_dev_portconf_print(struct rte_eth_dev_portconf *t, char *buf, int sz)
{
    int ret;
    char *p=buf;
    int left = sz;
    ret = snprintf(p, left, "struct rte_eth_dev_portconf: \n");p += ret;left -= ret;
    ret = snprintf(p, left, "    burst_size: %x\n", t->burst_size);p += ret;left -= ret;
    ret = snprintf(p, left, "    ring_size: %x\n", t->ring_size);p += ret;left -= ret;
    ret = snprintf(p, left, "    nb_queues: %x\n", t->nb_queues);p += ret;left -= ret;
}

void struct_struct_rte_eth_dev_info_print(struct rte_eth_dev_info *t, char *buf, int sz)
{
    int ret;
    char *p=buf;
    int left = sz;
    ret = snprintf(p, left, "struct rte_eth_dev_info: \n");p += ret;left -= ret;
    ret = snprintf(p, left, "    device: %p\n", t->device);p += ret;left -= ret;
    ret = snprintf(p, left, "    driver_name: %p\n", t->driver_name);p += ret;left -= ret;
    ret = snprintf(p, left, "    if_index: %x\n", t->if_index);p += ret;left -= ret;
    ret = snprintf(p, left, "    dev_flags: %p\n", t->dev_flags);p += ret;left -= ret;
    ret = snprintf(p, left, "    min_rx_bufsize: %x\n", t->min_rx_bufsize);p += ret;left -= ret;
    ret = snprintf(p, left, "    max_rx_pktlen: %x\n", t->max_rx_pktlen);p += ret;left -= ret;
    ret = snprintf(p, left, "    max_rx_queues: %x\n", t->max_rx_queues);p += ret;left -= ret;
    ret = snprintf(p, left, "    max_tx_queues: %x\n", t->max_tx_queues);p += ret;left -= ret;
    ret = snprintf(p, left, "    max_mac_addrs: %x\n", t->max_mac_addrs);p += ret;left -= ret;
    ret = snprintf(p, left, "    max_hash_mac_addrs: %x\n", t->max_hash_mac_addrs);p += ret;left -= ret;
    ret = snprintf(p, left, "    max_vfs: %x\n", t->max_vfs);p += ret;left -= ret;
    ret = snprintf(p, left, "    max_vmdq_pools: %x\n", t->max_vmdq_pools);p += ret;left -= ret;
    ret = snprintf(p, left, "    rx_offload_capa: %lx\n", t->rx_offload_capa);p += ret;left -= ret;
    ret = snprintf(p, left, "    tx_offload_capa: %lx\n", t->tx_offload_capa);p += ret;left -= ret;
    ret = snprintf(p, left, "    rx_queue_offload_capa: %lx\n", t->rx_queue_offload_capa);p += ret;left -= ret;
    ret = snprintf(p, left, "    tx_queue_offload_capa: %lx\n", t->tx_queue_offload_capa);p += ret;left -= ret;
    ret = snprintf(p, left, "    reta_size: %x\n", t->reta_size);p += ret;left -= ret;
    ret = snprintf(p, left, "    hash_key_size: %x\n", t->hash_key_size);p += ret;left -= ret;
    ret = snprintf(p, left, "    flow_type_rss_offloads: %lx\n", t->flow_type_rss_offloads);p += ret;left -= ret;
    ret = snprintf(p, left, "    default_rxconf: \n");p += ret;left -= ret;
    ret = snprintf(p, left, "        rx_thresh: \n");p += ret;left -= ret;
    ret = snprintf(p, left, "            pthresh: %x\n", t->default_rxconf.rx_thresh.pthresh);p += ret;left -= ret;
    ret = snprintf(p, left, "            hthresh: %x\n", t->default_rxconf.rx_thresh.hthresh);p += ret;left -= ret;
    ret = snprintf(p, left, "            wthresh: %x\n", t->default_rxconf.rx_thresh.wthresh);p += ret;left -= ret;
    ret = snprintf(p, left, "        rx_free_thresh: %x\n", t->default_rxconf.rx_free_thresh);p += ret;left -= ret;
    ret = snprintf(p, left, "        rx_drop_en: %x\n", t->default_rxconf.rx_drop_en);p += ret;left -= ret;
    ret = snprintf(p, left, "        rx_deferred_start: %x\n", t->default_rxconf.rx_deferred_start);p += ret;left -= ret;
    ret = snprintf(p, left, "        offloads: %lx\n", t->default_rxconf.offloads);p += ret;left -= ret;
    ret = snprintf(p, left, "    default_txconf: \n");p += ret;left -= ret;
    ret = snprintf(p, left, "        tx_thresh: \n");p += ret;left -= ret;
    ret = snprintf(p, left, "            pthresh: %x\n", t->default_txconf.tx_thresh.pthresh);p += ret;left -= ret;
    ret = snprintf(p, left, "            hthresh: %x\n", t->default_txconf.tx_thresh.hthresh);p += ret;left -= ret;
    ret = snprintf(p, left, "            wthresh: %x\n", t->default_txconf.tx_thresh.wthresh);p += ret;left -= ret;
    ret = snprintf(p, left, "        tx_rs_thresh: %x\n", t->default_txconf.tx_rs_thresh);p += ret;left -= ret;
    ret = snprintf(p, left, "        tx_free_thresh: %x\n", t->default_txconf.tx_free_thresh);p += ret;left -= ret;
    ret = snprintf(p, left, "        tx_deferred_start: %x\n", t->default_txconf.tx_deferred_start);p += ret;left -= ret;
    ret = snprintf(p, left, "        offloads: %lx\n", t->default_txconf.offloads);p += ret;left -= ret;
    ret = snprintf(p, left, "    vmdq_queue_base: %x\n", t->vmdq_queue_base);p += ret;left -= ret;
    ret = snprintf(p, left, "    vmdq_queue_num: %x\n", t->vmdq_queue_num);p += ret;left -= ret;
    ret = snprintf(p, left, "    vmdq_pool_base: %x\n", t->vmdq_pool_base);p += ret;left -= ret;
    ret = snprintf(p, left, "    rx_desc_lim: \n");p += ret;left -= ret;
    ret = snprintf(p, left, "        nb_max: %x\n", t->rx_desc_lim.nb_max);p += ret;left -= ret;
    ret = snprintf(p, left, "        nb_min: %x\n", t->rx_desc_lim.nb_min);p += ret;left -= ret;
    ret = snprintf(p, left, "        nb_align: %x\n", t->rx_desc_lim.nb_align);p += ret;left -= ret;
    ret = snprintf(p, left, "        nb_seg_max: %x\n", t->rx_desc_lim.nb_seg_max);p += ret;left -= ret;
    ret = snprintf(p, left, "        nb_mtu_seg_max: %x\n", t->rx_desc_lim.nb_mtu_seg_max);p += ret;left -= ret;
    ret = snprintf(p, left, "    tx_desc_lim: \n");p += ret;left -= ret;
    ret = snprintf(p, left, "        nb_max: %x\n", t->tx_desc_lim.nb_max);p += ret;left -= ret;
    ret = snprintf(p, left, "        nb_min: %x\n", t->tx_desc_lim.nb_min);p += ret;left -= ret;
    ret = snprintf(p, left, "        nb_align: %x\n", t->tx_desc_lim.nb_align);p += ret;left -= ret;
    ret = snprintf(p, left, "        nb_seg_max: %x\n", t->tx_desc_lim.nb_seg_max);p += ret;left -= ret;
    ret = snprintf(p, left, "        nb_mtu_seg_max: %x\n", t->tx_desc_lim.nb_mtu_seg_max);p += ret;left -= ret;
    ret = snprintf(p, left, "    speed_capa: %x\n", t->speed_capa);p += ret;left -= ret;
    ret = snprintf(p, left, "    nb_rx_queues: %x\n", t->nb_rx_queues);p += ret;left -= ret;
    ret = snprintf(p, left, "    nb_tx_queues: %x\n", t->nb_tx_queues);p += ret;left -= ret;
    ret = snprintf(p, left, "    default_rxportconf: \n");p += ret;left -= ret;
    ret = snprintf(p, left, "        burst_size: %x\n", t->default_rxportconf.burst_size);p += ret;left -= ret;
    ret = snprintf(p, left, "        ring_size: %x\n", t->default_rxportconf.ring_size);p += ret;left -= ret;
    ret = snprintf(p, left, "        nb_queues: %x\n", t->default_rxportconf.nb_queues);p += ret;left -= ret;
    ret = snprintf(p, left, "    default_txportconf: \n");p += ret;left -= ret;
    ret = snprintf(p, left, "        burst_size: %x\n", t->default_txportconf.burst_size);p += ret;left -= ret;
    ret = snprintf(p, left, "        ring_size: %x\n", t->default_txportconf.ring_size);p += ret;left -= ret;
    ret = snprintf(p, left, "        nb_queues: %x\n", t->default_txportconf.nb_queues);p += ret;left -= ret;
    ret = snprintf(p, left, "    dev_capa: %lx\n", t->dev_capa);p += ret;left -= ret;
    ret = snprintf(p, left, "    switch_info: \n");p += ret;left -= ret;
    ret = snprintf(p, left, "        name: %p\n", t->switch_info.name);p += ret;left -= ret;
    ret = snprintf(p, left, "        domain_id: %x\n", t->switch_info.domain_id);p += ret;left -= ret;
    ret = snprintf(p, left, "        port_id: %x\n", t->switch_info.port_id);p += ret;left -= ret;
}

