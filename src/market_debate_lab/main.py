from market_debate_lab.crew import MarketDebateCrew


def run():
    inputs = {
        "market": "The German travel guide book market in the age of AI"
    }

    result = MarketDebateCrew().crew().kickoff(inputs=inputs)

    print("\n\nFINAL RESULT:\n")
    print(result.raw)


if __name__ == "__main__":
    run()