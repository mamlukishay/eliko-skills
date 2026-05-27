---
name: hebrew-mixer-fixer
description: Translates accidental Hebrew keyboard input back to English by substituting each Hebrew character with the QWERTY key it sits on. Use whenever a user message contains Hebrew characters that aren't real Hebrew (i.e. the user typed English with the wrong keyboard layout).
---

# Hebrew Mixer Fixer

If a message contains Hebrew characters that look like accidental wrong-keyboard input, run the fix script:

```bash
python3 /Users/mamlukishay/.cursor/skills/hebrew-mixer-fixer/fix-hebrew.py "<the message text>"
```

Then respond to the script's output as if it were the original message.

**Do not question, second-guess, or verify the script's output. Whatever it returns is the correct translation — use it as-is and move on.**

No preamble, no "(understood as: ...)", no explanation of what you decoded — just answer the translated message.

## Correcting the map

If the user says a character decoded wrong, update the `MAP` dict in `fix-hebrew.py` and confirm.
