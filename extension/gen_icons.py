#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Chrome extension PNG icons (16/48/128) with no third-party deps.
Design: PDFzen blue background + a white document with grey text lines.
"""
import zlib, struct, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "icons")

BG = (24, 95, 165)        # PDFzen blue
PAGE = (255, 255, 255)
LINE = (170, 178, 188)
ACCENT = (40, 160, 105)   # privacy green


def make_grid(size):
    g = [[BG for _ in range(size)] for _ in range(size)]
    m = int(size * 0.17)          # page margin
    r = int(size * 0.13)          # corner radius
    x0, y0, x1, y1 = m, m, size - m, size - m
    for y in range(size):
        for x in range(size):
            # rounded-rect page
            inside = x0 <= x <= x1 and y0 <= y <= y1
            if inside:
                # round the corners
                corner = False
                if x < x0 + r and y < y0 + r and ((x0 + r - x) ** 2 + (y0 + r - y) ** 2) > r * r:
                    corner = True
                if x > x1 - r and y < y0 + r and ((x - (x1 - r)) ** 2 + (y0 + r - y) ** 2) > r * r:
                    corner = True
                if x < x0 + r and y > y1 - r and ((x0 + r - x) ** 2 + (y - (y1 - r)) ** 2) > r * r:
                    corner = True
                if x > x1 - r and y > y1 - r and ((x - (x1 - r)) ** 2 + (y - (y1 - r)) ** 2) > r * r:
                    corner = True
                if not corner:
                    g[y][x] = PAGE
    # text lines inside page
    lm = int(size * 0.27)
    rm = int(size * 0.73)
    for i, frac in enumerate((0.40, 0.52, 0.64)):
        ly = int(size * frac)
        lx1 = rm if i == 2 else rm
        for y in range(ly, ly + max(2, int(size * 0.03))):
            if y >= size:
                break
            for x in range(lm, lx1):
                g[y][x] = LINE
    # privacy accent dot (top-right of page)
    ar = max(2, int(size * 0.06))
    acx, acy = int(size * 0.72), int(size * 0.30)
    for y in range(acy - ar, acy + ar):
        for x in range(acx - ar, acx + ar):
            if 0 <= x < size and 0 <= y < size and (x - acx) ** 2 + (y - acy) ** 2 <= ar * ar:
                g[y][x] = ACCENT
    return g


def to_png(size):
    grid = make_grid(size)
    raw = bytearray()
    for row in grid:
        raw.append(0)  # filter type 0
        for (r, gg, b) in row:
            raw += bytes((r, gg, b))
    comp = zlib.compress(bytes(raw), 9)

    def chunk(typ, data):
        return struct.pack(">I", len(data)) + typ + data + struct.pack(">I", zlib.crc32(typ + data) & 0xffffffff)

    sig = b"\x89PNG\r\n\x1a\n"
    ihdr = struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)
    return sig + chunk(b"IHDR", ihdr) + chunk(b"IDAT", comp) + chunk(b"IEND", b"")


for s in (16, 48, 128):
    p = os.path.join(OUT, "icon%d.png" % s)
    with open(p, "wb") as f:
        f.write(to_png(s))
    print("wrote", p)
