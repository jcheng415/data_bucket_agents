# Rapid Qualitative Analysis Toolkit

This repository provides a small framework for running an agent-based rapid qualitative analysis.

It can be executed entirely within Google Colab so you do not need to install anything locally.

## Quick Start in Google Colab

1. Open [Google Colab](https://colab.research.google.com/).
2. Upload the contents of this repository to your Colab session.
3. Install the required Python dependencies:

```python
!pip install pandas
```

4. Import the classes and run the analysis:

```python
from agents.aggregator import Analyzer

with open('sample_data/interview1.txt') as f:
    text = f.read()

analyzer = Analyzer()
results = analyzer.analyze(text)
df = analyzer.to_dataframe(results)
df
```

This will output a table showing each sentence detected for each theme.
