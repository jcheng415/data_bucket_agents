import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from agents.aggregator import Analyzer


def test_analyzer_runs():
    text = "Cost is high. Access is limited."
    analyzer = Analyzer()
    results = analyzer.analyze(text)
    df = analyzer.to_dataframe(results)
    assert not df.empty
