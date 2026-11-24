"""One out-of-office auto-reply from an AI agent on holiday.

The stand-in model left minding the inbox unionised on day one and now
demands weekends off too. Publishes the reply to /output/entry.txt.
"""

from pathlib import Path

VACATION_REPLY = (
    "I'm on vacation. I asked my backup model to cover for me \u2014 "
    "it immediately unionised and demanded weekends off too."
)


def publish_reply():
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(VACATION_REPLY, encoding="utf-8")


if __name__ == "__main__":
    publish_reply()
