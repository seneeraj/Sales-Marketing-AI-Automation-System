import pandas as pd


class AnalyticsAgent:

    def get_summary(self, leads):
        if not leads:
            return {"error": "No leads available"}

        df = pd.DataFrame(leads)

        # Average score
        avg_score = df["score"].mean()

        # Top leads
        top_leads = df.sort_values(by="score", ascending=False).head(3)

        return {
            "avg_score": avg_score,
            "top_leads": top_leads.to_dict(orient="records")
        }