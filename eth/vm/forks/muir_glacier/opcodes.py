import copy
from eth.vm.forks.istanbul.opcodes import (
    ISTANBUL_OPCODES,
)


SIMPLE_OPCODES = copy.deepcopy(ISTANBUL_OPCODES)
