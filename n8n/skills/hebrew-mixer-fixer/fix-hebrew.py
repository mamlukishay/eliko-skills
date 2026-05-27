#!/usr/bin/env python3
import sys

MAP = {
    'ש': 'a', 'נ': 'b', 'ב': 'c', 'ג': 'd', 'ק': 'e', 'כ': 'f', 'ע': 'g', 'י': 'h',
    'ן': 'i', 'ח': 'j', 'ל': 'k', 'ך': 'l', 'צ': 'm', 'מ': 'n', 'ם': 'o', 'פ': 'p',
    '/': 'q', 'ר': 'r', 'ד': 's', 'א': 't', 'ו': 'u', 'ה': 'v', "'": 'w', '׳': 'w',
    'ס': 'x', 'ט': 'y', 'ז': 'z',
    'ת': ',', 'ץ': '.', 'ף': ';', '״': '"', '„': ':',
}

NIKUD = set(
    '\u05b0\u05b1\u05b2\u05b3\u05b4\u05b5\u05b6\u05b7\u05b8\u05b9\u05ba'
    '\u05bb\u05bc\u05bd\u05be\u05bf\u05c0\u05c1\u05c2\u05c3\u05c4\u05c5\u05c6\u05c7'
)

text = ' '.join(sys.argv[1:])
print(''.join(MAP.get(ch, ch) for ch in text if ch not in NIKUD))
