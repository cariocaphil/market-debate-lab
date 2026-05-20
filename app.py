import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

from market_debate_lab.main import demo


if __name__ == "__main__":
    demo.queue().launch()