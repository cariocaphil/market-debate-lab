from pathlib import Path

import gradio as gr

from market_debate_lab.crew import MarketDebateCrew
from market_debate_lab.settings import FIXED_MARKET

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)


def read_output_file(filename: str) -> str:
    path = OUTPUT_DIR / filename

    if path.exists():
        return path.read_text(encoding="utf-8")

    return "_No output generated yet._"


def set_loading_state():
    return (
        gr.update(value="⏳ Generating market debate report...", visible=True),
        gr.update(interactive=False, value="Running..."),
    )


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
        gr.update(value="✅ Generation finished.", visible=True),
        gr.update(interactive=True, value="Run market debate"),
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
    status = gr.Markdown(visible=False)

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
        fn=set_loading_state,
        inputs=[],
        outputs=[status, run_button],
    ).then(
        fn=run_market_debate,
        inputs=[],
        outputs=[
            final_result,
            research_output,
            bull_output,
            bear_output,
            judge_output,
            report_output,
            status,
            run_button,
        ],
    )


def run():
    demo.queue().launch()


if __name__ == "__main__":
    run()