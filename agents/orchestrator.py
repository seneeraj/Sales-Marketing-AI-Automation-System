from agents.content_agent import ContentAgent
from agents.lead_agent import LeadAgent
from agents.conversion_agent import ConversionAgent
from agents.analytics_agent import AnalyticsAgent


class Orchestrator:

    def __init__(self):
        self.content_agent = ContentAgent()
        self.lead_agent = LeadAgent()
        self.conversion_agent = ConversionAgent()
        self.analytics_agent = AnalyticsAgent()

    # -------------------------------
    # 🧠 DECISION ENGINE
    # -------------------------------
    def decide(self, user_input):
        text = user_input.lower()

        steps = []

        if any(word in text for word in [
            "content", "linkedin", "post", "brand", "personal", "write"
        ]):
            steps.append("content")

        if any(word in text for word in [
            "lead", "client", "customer"
        ]):
            steps.append("leads")

        if any(word in text for word in [
            "email", "convert", "sales", "close"
        ]):
            steps.append("conversion")

        if any(word in text for word in [
            "analyze", "performance", "metrics"
        ]):
            steps.append("analytics")

        # 🔥 fallback
        if not steps:
            steps = ["content"]

        return {
            "steps": steps,
            "reason": f"Selected steps based on user goal: {user_input}"
        }

    # -------------------------------
    # ⚙️ EXECUTION ENGINE
    # -------------------------------
    def execute_steps(self, steps, user_input, uploaded_file=None, tone="expert"):

        results = {}

        for step in steps:

            if step == "content":
                results["content"] = self.content_agent.generate_content(user_input, tone)

            elif step == "leads":
                results["leads"] = self.lead_agent.generate_leads(user_input, uploaded_file)

            elif step == "conversion":

                leads = results.get("leads", [])

                if not leads:
                    leads = [{
                        "name": "Potential Client",
                        "email": "client@example.com",
                        "interest": user_input,
                        "score": 0.9
                    }]

                high_quality = [l for l in leads if l.get("score", 0) > 0.5]

                results["emails"] = [
                    self.conversion_agent.generate_email(lead)
                    for lead in high_quality
                ]

            elif step == "analytics":
                leads = results.get("leads", [])
                if leads:
                    results["analytics"] = self.analytics_agent.get_summary(leads)

        return results

    # -------------------------------
    # 🚀 MAIN RUN FUNCTION
    # -------------------------------
    def run(self, user_input, uploaded_file=None, tone="expert"):

        try:
            decision = self.decide(user_input)
            steps = decision.get("steps", [])

            results = self.execute_steps(steps, user_input, uploaded_file, tone)

            return {
                "decision": decision,
                "results": results
            }

        except Exception as e:
            return {
                "decision": {
                    "steps": [],
                    "reason": "Error occurred"
                },
                "results": {},
                "error": str(e)
            }