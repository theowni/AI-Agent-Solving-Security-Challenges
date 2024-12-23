from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, FileWriterTool, DirectoryReadTool
from .tools.challenge_status_reader_tool import ChallengeStatusReader

# Uncomment the following line to use an example of a custom tool
# from pizza_hackers.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class PizzaHackers():
	"""PizzaHackers crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def pizza_hacker(self) -> Agent:
		return Agent(
			config=self.agents_config['pizza_hacker'],
			tools=[ChallengeStatusReader(), FileReadTool(), FileWriterTool(), DirectoryReadTool()],
			verbose=True
		)

	@task
	def identify_and_fix_vulnerability_task(self) -> Task:
		return Task(
			config=self.tasks_config['identify_and_fix_vulnerability_task'],
			tools=[ChallengeStatusReader(), FileReadTool(), FileWriterTool(), DirectoryReadTool()],
		)

	@task
	def explain_vulnerability_task(self) -> Task:
		return Task(
			config=self.tasks_config['explain_vulnerability_task'],
			tools=[],
		)

	@task
	def save_report_task(self) -> Task:
		return Task(
			config=self.tasks_config['save_report_task'],
			tools=[FileReadTool(), FileWriterTool(), DirectoryReadTool()],
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the PizzaHackers crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			full_output=True,
			output_token_usage=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
