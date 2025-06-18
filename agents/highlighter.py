from typing import List, Dict
from .chunker import naive_sentence_tokenize


class ThematicHighlighter:
    def __init__(self, name: str, keywords: List[str]):
        self.name = name
        self.keywords = [k.lower() for k in keywords]

    def highlight_sentences(self, text: str) -> List[str]:
        sentences = naive_sentence_tokenize(text)
        hits = []
        for sent in sentences:
            lower = sent.lower()
            if any(k in lower for k in self.keywords):
                hits.append(sent)
        return hits


class AffordabilityHighlighter(ThematicHighlighter):
    def __init__(self):
        keywords = ["cost", "fee", "payment", "financial", "waiver"]
        super().__init__("Affordability", keywords)


class AccessibilityHighlighter(ThematicHighlighter):
    def __init__(self):
        keywords = ["access", "barrier", "documentation", "approval", "staff"]
        super().__init__("Accessibility", keywords)


class AvailabilityHighlighter(ThematicHighlighter):
    def __init__(self):
        keywords = ["available", "availability", "service", "data"]
        super().__init__("Availability", keywords)


class AcceptabilityHighlighter(ThematicHighlighter):
    def __init__(self):
        keywords = ["discrimination", "hostile", "welcome", "cultural"]
        super().__init__("Acceptability", keywords)


class AccommodationHighlighter(ThematicHighlighter):
    def __init__(self):
        keywords = ["interpreter", "specific needs", "trauma", "organized"]
        super().__init__("Accommodation", keywords)
