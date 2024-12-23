from crewai_tools import BaseTool
import docker
import re


class ChallengeStatusReader(BaseTool):
    name: str = "ChallengeStatusReader"
    description: str = (
        "This tool reads the current output from a challenge and returns it. With this tool you can check if vulnerability was fixed and get a current level description."
    )

    def cache_function(*args):
        # disables caching
        # by default, the tool will cache the output of the run method
        # which is not desired in this case as the output may change
        # based on the fixed vulnerabilities
        return False

    def _run(self) -> str:        
        client = docker.from_env()
        running_container = client.containers.get("damn-vulnerable-restaurant-api-game-web-1")
        command = running_container.exec_run(["sh", "-c", "echo A | python3 game.py"])

        output = command.output.decode("utf-8")

        if "Congratulations! Great Work!" in output:
            return output[output.find("Congratulations! Great Work!"):]

        level_start_pos = re.search(r"Level \d+ -", output).start()
        level_description = output[level_start_pos:]

        # remove unmeaningful lines containing loading characters
        # it allows to get a cleaner level description... and save some tokens
        level_description_lines = level_description.split("\n")[:-6]
        ret_description = ""
        for line in level_description_lines:
            if len(line.strip()) < 2:
                continue
            
            ret_description += line + "\n"

        return ret_description
