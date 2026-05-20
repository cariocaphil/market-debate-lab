import sys
from pathlib import Path

import gradio as gr

sys.path.append(str(Path(__file__).parent / "src"))

from market_debate_lab.crew import MarketDebateCrew


FIXED_MARKET = "The German travel guide book market in the age of AI"

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


def read_output_file(filename: str) -> str:
    path = OUTPUT_DIR / filename

    if path.exists():
        return path.read_text(encoding="utf-8")

    return "_No output generated yet._"


def run_market_debate():
    result = MarketDebateCrew().crew().kickoff(
        inputs={"market": FIXED_MARKET}
    )

    return (
        str(result.raw),
        read_output_file("research.md"),
        read_output_file("bull_case.md"),
        read_output_file("bear_case.md"),
        read_output_file("judge_verdict.md"),
        read_output_file("final_report.md"),
    )


with gr.Blocks(title="Market Debate Lab") as demo:
    gr.Markdown("# Market Debate Lab")

    gr.Markdown("""
    A CrewAI-powered market research and debate app.

    **Current scenario:**  
    The German travel guide book market in the age of AI.
    """)

    gr.Markdown("""
    ## Agent Flow

    🔎 Researcher  
    → 📈 Bull Analyst  
    → ⚠️ Bear Analyst  
    → ⚖️ Judge  
    → 📝 Report Writer
    """)

    run_button = gr.Button("Run market debate")

    with gr.Tabs():
        with gr.Tab("Final Result"):
            final_result = gr.Markdown()

        with gr.Tab("Research"):
            research_output = gr.Markdown()

        with gr.Tab("Bull Case"):
            bull_output = gr.Markdown()

        with gr.Tab("Bear Case"):
            bear_output = gr.Markdown()

        with gr.Tab("Judge"):
            judge_output = gr.Markdown()

        with gr.Tab("Final Report"):
            report_output = gr.Markdown()

    run_button.click(
        fn=run_market_debate,
        inputs=[],
        outputs=[
            final_result,
            research_output,
            bull_output,
            bear_output,
            judge_output,
            report_output,
        ],
    )


if __name__ == "__main__":
    demo.launch()