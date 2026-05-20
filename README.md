# Market Debate Lab

A multi-agent market analysis pipeline built with [CrewAI](https://docs.crewai.com/). Five specialized agents research a market, argue bull and bear cases, reach a verdict, and produce an executive report. A [Gradio](https://www.gradio.app/) UI runs the crew and displays each stage of the output.

The default market is **the German travel guide book market in the age of AI**.

## How it works

Agents run in sequence:

1. **Researcher** — web search (Serper) and a structured research brief
2. **Bull analyst** — strongest case for entering the market
3. **Bear analyst** — strongest case against entering
4. **Judge** — compares both sides and issues a recommendation
5. **Analyst** — polished final report from research and debate

Each task writes markdown to the `output/` directory:

| File | Agent |
|------|--------|
| `output/research.md` | Researcher |
| `output/bull_case.md` | Bull analyst |
| `output/bear_case.md` | Bear analyst |
| `output/judge_verdict.md` | Judge |
| `output/final_report.md` | Analyst |

## Requirements

- Python 3.10–3.12
- API keys (see [Environment variables](#environment-variables))

## Setup

```bash
cd market-debate-lab
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
```

Copy your keys into a `.env` file in the project root (this file is gitignored):

```env
OPENAI_API_KEY=your_openai_key
SERPER_API_KEY=your_serper_key
```

## Run the UI

From the project root:

```bash
debate
```

Or:

```bash
python -m market_debate_lab.main
```

Gradio opens in the browser. Click **Run market debate** to start the crew. Tabs show the final result plus each artifact (research, bull, bear, judge, report).

## Project layout

```
market-debate-lab/
├── src/market_debate_lab/
│   ├── main.py              # Gradio app and entry point
│   ├── crew.py              # CrewAI agents and tasks
│   └── config/
│       ├── agents.yaml      # Agent roles, goals, LLMs
│       └── tasks.yaml       # Task prompts and output files
├── output/                  # Generated markdown (created at runtime)
├── pyproject.toml
└── .env                     # API keys (not committed)
```

## Customization

- **Market topic** — edit `FIXED_MARKET` in `src/market_debate_lab/main.py`, or extend the app to pass a user-defined `{market}` into `kickoff(inputs={"market": ...})`.
- **Agents and tasks** — adjust `src/market_debate_lab/config/agents.yaml` and `tasks.yaml`.
- **Models** — each agent sets `llm: openai/gpt-4o-mini` in `agents.yaml`; change as needed for your provider setup.

## Tech stack

- [CrewAI](https://docs.crewai.com/) — agent orchestration (sequential process)
- [crewai-tools SerperDevTool](https://docs.crewai.com/en/tools/search-research/serperdevtool) — web search for the researcher
- [Gradio](https://www.gradio.app/) — local web UI
- [python-dotenv](https://pypi.org/project/python-dotenv/) — load `.env` (via CrewAI / tooling conventions)

## License

Add a license file if you plan to distribute this project.
