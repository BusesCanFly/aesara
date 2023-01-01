#! /usr/bin/python3

import atheris
import sys

with atheris.instrument_imports():
    import aesara
    from aesara import tensor as at

@atheris.instrument_func
def test_input(input_bytes):
    fdp = atheris.FuzzedDataProvider(input_bytes)
    input_string = fdp.ConsumeUnicodeNoSurrogates(sys.maxsize)
    # input_str_w_surrogates = fdp.ConsumeUnicode(sys.maxsize)
    # input_int = fdp.ConsumeInt(sys.maxsize)
    try:
        # a = at.dscalar(input_string)
        # f_c = aesara.function([input_string, input_string], input_string)
        # dc = aesara.grad(input_string, input_string)
        # f_dc = aesara.function([input_string, input_string], input_string)
        # v = at.vector(input_string)
        # M = at.matrix(input_string)
        # aesara.dprint(input_string)
        # f_d = aesara.function([input_string, input_string, input_string], input_string)
        aesara.dprint(input_string)
    except TypeError:
        pass

def main():
    atheris.Setup(sys.argv, test_input)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
