"""=============================================================================
                                    IMPORTS
============================================================================="""
from cffi import FFI


"""=============================================================================
                            MODULE-LEVEL VARIABLES
============================================================================="""
# See https://cffi.readthedocs.io/en/latest/index.html for cffi docs

ffibuilder = FFI()

builddir = "cext/build"

# matches header demo.h
ffibuilder.cdef(
"""
uint32_t LeftShift(uint32_t value, uint32_t shift);
uint8_t GetHighNibble(uint8_t value);
""")


ffibuilder.set_source("cffi_demo",  # name of the output C extension
"""
    #include "../demo.h"
""",
    sources=['../demo.c'])

"""=============================================================================
                                    MAIN
============================================================================="""
if __name__ == "__main__":
    result = ffibuilder.compile(verbose=True, tmpdir=builddir)
    
