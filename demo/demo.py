import ctypes
import os

print("=== Step 1: Load shared libraries ===")

lib = ctypes.CDLL("./libdilithium_mode3.so", mode=ctypes.RTLD_GLOBAL)

PK_SIZE = 1952
SK_SIZE = 4032
SIG_SIZE = 3309

# keypair
lib.pqcrystals_dilithium3_ref_keypair.argtypes = [
    ctypes.POINTER(ctypes.c_uint8),
    ctypes.POINTER(ctypes.c_uint8)
]
lib.pqcrystals_dilithium3_ref_keypair.restype = ctypes.c_int

# signature
lib.pqcrystals_dilithium3_ref_signature.argtypes = [
    ctypes.POINTER(ctypes.c_uint8),    # sig
    ctypes.POINTER(ctypes.c_size_t),   # siglen
    ctypes.POINTER(ctypes.c_uint8),    # m
    ctypes.c_size_t,                   # mlen
    ctypes.POINTER(ctypes.c_uint8),    # ctx
    ctypes.c_size_t,                   # ctxlen
    ctypes.POINTER(ctypes.c_uint8)     # sk
]
lib.pqcrystals_dilithium3_ref_signature.restype = ctypes.c_int

# verify
lib.pqcrystals_dilithium3_ref_verify.argtypes = [
    ctypes.POINTER(ctypes.c_uint8),    # sig
    ctypes.c_size_t,                   # siglen
    ctypes.POINTER(ctypes.c_uint8),    # m
    ctypes.c_size_t,                   # mlen
    ctypes.POINTER(ctypes.c_uint8),    # ctx
    ctypes.c_size_t,                   # ctxlen
    ctypes.POINTER(ctypes.c_uint8)     # pk
]
lib.pqcrystals_dilithium3_ref_verify.restype = ctypes.c_int

print("=== Step 2: Allocate memory ===")

pk = (ctypes.c_uint8 * PK_SIZE)()
sk = (ctypes.c_uint8 * SK_SIZE)()
sig = (ctypes.c_uint8 * SIG_SIZE)()

siglen = ctypes.c_size_t()

print(f"pk size = {PK_SIZE}")
print(f"sk size = {SK_SIZE}")
print(f"sig size = {SIG_SIZE}")

print("=== Step 3: KeyGen ===")

ret = lib.pqcrystals_dilithium3_ref_keypair(pk, sk)
print("keypair ret =", ret)

if ret != 0:
    print("KeyGen failed")
    exit(1)

print("=== Step 4: Prepare message ===")

message = b"Hello Dilithium"
mlen = len(message)

msg_buf = (ctypes.c_uint8 * mlen).from_buffer_copy(message)

print("mlen =", mlen)

# ctx = NULL
ctx_ptr = ctypes.POINTER(ctypes.c_uint8)()
ctxlen = ctypes.c_size_t(0)

print("=== Step 5: Sign ===")

ret = lib.pqcrystals_dilithium3_ref_signature(
    sig,
    ctypes.byref(siglen),
    msg_buf,
    mlen,
    ctx_ptr,
    ctxlen,
    sk
)

print("sign ret =", ret)
print("siglen =", siglen.value)

if ret != 0:
    print("Sign failed")
    exit(1)

print("=== Step 6: Verify ===")

ret = lib.pqcrystals_dilithium3_ref_verify(
    sig,
    siglen.value,
    msg_buf,
    mlen,
    ctx_ptr,
    ctxlen,
    pk
)

print("verify ret =", ret)

if ret == 0:
    print("SUCCESS: signature verified")
else:
    print("VERIFY FAILED")