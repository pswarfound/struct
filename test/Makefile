RTE_SDK ?= ERROR
PJ_ROOT ?= ERROR
RTE_TARGET ?= x86_64-native-linuxapp-gcc

include $(RTE_SDK)/mk/rte.vars.mk
include $(RTE_SDK)/mk/internal/rte.compile-pre.mk
include $(RTE_SDK)/mk/internal/rte.install-pre.mk
include $(RTE_SDK)/mk/internal/rte.clean-pre.mk
include $(RTE_SDK)/mk/internal/rte.build-pre.mk


all:
	@echo -n > $(PJ_ROOT)/rte_cflags.mk
	@echo -n > $(PJ_ROOT)/rte_ldflags.mk
ifneq ($(CFLAGS), )
	@echo -n $(CFLAGS) > $(PJ_ROOT)/rte_cflags.mk
endif
ifneq ($(EXTRA_CFLAGS), )
	echo $(EXTRA_CFLAGS) >> $(PJ_ROOT)/rte_cflags.mk
endif
ifneq ($(LDFLAGS), )
	@echo $(LDFLAGS) > $(PJ_ROOT)/rte_ldflags.mk
endif
ifneq ($(EXTRA_LDFLAGS), )
	@echo $(EXTRA_LDFLAGS) >> $(PJ_ROOT)/rte_ldflags.mk
endif