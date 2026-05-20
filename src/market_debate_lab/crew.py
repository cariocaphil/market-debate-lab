from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool


@CrewBase
class MarketDebateCrew:
    """Market research and debate crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            tools=[SerperDevTool()],
            verbose=True,
        )

    @agent
    def bull_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["bull_analyst"],
            verbose=True,
        )

    @agent
    def bear_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["bear_analyst"],
            verbose=True,
        )

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config["judge"],
            verbose=True,
        )

    @agent
    def analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["analyst"],
            verbose=True,
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_task"],
        )

    @task
    def bull_case_task(self) -> Task:
        return Task(
            config=self.tasks_config["bull_case_task"],
        )

    @task
    def bear_case_task(self) -> Task:
        return Task(
            config=self.tasks_config["bear_case_task"],
        )

    @task
    def judge_task(self) -> Task:
        return Task(
            config=self.tasks_config["judge_task"],
        )

    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the market debate crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )