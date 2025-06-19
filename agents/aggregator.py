from typing import List, Dict
import pandas as pd
from .highlighter import (
    AffordabilityHighlighter,
    AccessibilityHighlighter,
    AvailabilityHighlighter,
    AcceptabilityHighlighter,
    AccommodationHighlighter,
)
from .chunker import Chunker


class Analyzer:
    def __init__(self):
        self.chunker = Chunker()
        self.highlighters = [
            AffordabilityHighlighter(),
            AccessibilityHighlighter(),
            AvailabilityHighlighter(),
            AcceptabilityHighlighter(),
            AccommodationHighlighter(),
        ]

    def analyze(self, text: str) -> Dict[str, List[str]]:
        chunks = self.chunker.chunk(text)
        results: Dict[str, List[str]] = {h.name: [] for h in self.highlighters}
        for chunk in chunks:
            for h in self.highlighters:
                hits = h.highlight_sentences(chunk)
                results[h.name].extend(hits)
        return results

    def to_dataframe(self, results: Dict[str, List[str]]) -> pd.DataFrame:
        rows = []
        for theme, sents in results.items():
            for sent in sents:
                rows.append({"theme": theme, "sentence": sent})
        return pd.DataFrame(rows)
