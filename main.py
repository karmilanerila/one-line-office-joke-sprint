"""One-line office joke: reply-all thanks.

The joke: 47 unread emails, and 46 of them are people replying-all just
to say "thanks." It is the sort of line you send a colleague after a
meeting that should have been an email — everyone who has lived in a
corporate inbox recognises the reply-all thanks spiral instantly, and
the counting (47 vs 46) makes the absurdity concrete in one breath.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""
import os

LINE = "I have 47 unread emails, and 46 of them are people replying-all to say 'thanks.'"


def write_entry(out_dir):
    """Write the joke bytes to <out_dir>/entry.txt, mode 0644."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
