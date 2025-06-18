import re
from typing import List


def naive_sentence_tokenize(text: str) -> List[str]:
    """Very small sentence tokenizer splitting by period, question mark, exclamation"""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if s.strip()]


class Chunker:
    """Chunk text into blocks. Here we simply split by blank lines."""

    def chunk(self, text: str) -> List[str]:
        blocks = [b.strip() for b in re.split(r"\n\s*\n", text) if b.strip()]
        return blocks
