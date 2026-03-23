import time
from agents.orchestrator import Orchestrator


class AutonomousAgent:
    def __init__(self):
        self.orch = Orchestrator()

    def run_cycle(self):
        print("\n🚀 Running Autonomous Growth Cycle...\n")

        task = "Grow my AI business and get more customers"

        result = self.orch.run(task)

        print("✅ Cycle Completed")
        print(result)

    def start(self, interval=60):
        # interval in seconds

        while True:
            self.run_cycle()
            time.sleep(interval)