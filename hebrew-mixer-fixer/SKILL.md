---
name: hebrew-mixer-fixer
description: Translates accidental Hebrew keyboard input back to English by substituting each Hebrew character with the QWERTY key it sits on. Use whenever a user message contains Hebrew characters that aren't real Hebrew (i.e. the user typed English with the wrong keyboard layout).
---

# Hebrew Mixer Fixer

If a message contains Hebrew characters, substitute each one using the map below and respond to the result. No analysis, no preamble, no "(understood as: ...)" — just answer.

## Map

```
ש→a  נ→b  ב→c  ג→d  ק→e  כ→f  ע→g  י→h  ן→i  ח→j
ל→k  ך→l  צ→m  מ→n  ם→o  פ→p  /→q  ר→r  ד→s  א→t
ו→u  ה→v  '→w  ׳→w  ס→x  ט→y  ז→z
ת→,  ץ→.  ף→;  ״→"  „→:
```

Ignore nikud/diacritic characters (ָ ַ ִ ֵ ֶ ְ ּ ֹ etc.) — they appear when Shift is held and have no English equivalent.

Other characters pass through unchanged. Treat the decoded text exactly like a typo-filled English message — do not "fix" it.

## Correcting the map

If the user says a character decoded wrong, update the map in this file and confirm.
