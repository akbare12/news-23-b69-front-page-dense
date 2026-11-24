#!/usr/bin/env python3
"""news-23 b69 front-page-dense: copy entry.png (1024x1024) to $MAKEFUN_OUTPUT_DIR/entry.png.

Stdlib only. Never writes next to itself: it writes only to MAKEFUN_OUTPUT_DIR,
so it also works from a read-only copy (with MAKEFUN_OUTPUT_DIR pointed elsewhere).
"""
import hashlib
import os
import struct
import sys

MAX_BYTES = 1024 * 1024
PNG_SIG = b"\x89PNG\r\n\x1a\n"


def fail(msg):
    print("error: " + msg, file=sys.stderr)
    return 1


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    if not out_dir:
        return fail("MAKEFUN_OUTPUT_DIR is empty")
    out_dir_abs = os.path.abspath(out_dir)
    here_abs = os.path.abspath(here)
    if out_dir_abs == here_abs or out_dir_abs.startswith(here_abs + os.sep):
        return fail("MAKEFUN_OUTPUT_DIR must not be inside the repo")
    if not os.path.isfile(src):
        return fail("entry.png not found next to main.py")

    with open(src, "rb") as fh:
        data = fh.read()
    if len(data) > MAX_BYTES:
        return fail("entry.png exceeds 1 MiB")
    if data[:8] != PNG_SIG:
        return fail("entry.png is not a PNG")
    if len(data) < 33:
        return fail("entry.png too short for IHDR")
    width, height = struct.unpack(">II", data[16:24])
    bit_depth = data[24]
    color_type = data[25]
    if (width, height) != (1024, 1024):
        return fail("entry.png is %dx%d, expected 1024x1024" % (width, height))
    if bit_depth != 8 or color_type not in (2, 6):
        return fail("unexpected bit depth %d / colour type %d" % (bit_depth, color_type))
    # IEND trailer: last 12 bytes must be length 0 + 'IEND' + CRC.
    if len(data) < 12 or data[-12:-8] != b"\x00\x00\x00\x00" or data[-8:-4] != b"IEND":
        return fail("PNG IEND trailer malformed")

    os.makedirs(out_dir_abs, exist_ok=True)
    dst = os.path.join(out_dir_abs, "entry.png")
    with open(dst, "wb") as fh:
        fh.write(data)
    with open(dst, "rb") as fh:
        back = fh.read()
    if back != data:
        return fail("output differs from source after copy")
    print("source entry.png: %d bytes, %dx%d, bit depth %d, colour type %d"
          % (len(data), width, height, bit_depth, color_type))
    print("wrote %s (%d bytes, %dx%d, sha256 %s)"
          % (dst, len(data), width, height, hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
