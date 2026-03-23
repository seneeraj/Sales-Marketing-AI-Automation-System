import pandas as pd
from sentence_transformers import SentenceTransformer, util


class LeadAgent:

    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2', device = 'cpu')

    def generate_leads(self, user_input, uploaded_file=None):

        # 📁 Use uploaded file if available
        if uploaded_file is not None:
            print("📁 Using uploaded CSV")
            df = pd.read_csv(uploaded_file)
        else:
            print("📂 Using default CSV")
            df = pd.read_csv("Test_Lead.csv")

        # Fix format if needed
        if len(df.columns) == 1:
            df = df[df.columns[0]].str.split(",", expand=True)
            df.columns = ["name", "email", "interest"]

        # Normalize
        df.columns = df.columns.str.lower().str.strip()

        leads = df.to_dict(orient="records")

        # 🧠 AI Scoring
        user_embedding = self.model.encode(user_input, convert_to_tensor=True)

        for lead in leads:
            interest = lead.get("interest", "")

            emb = self.model.encode(interest, convert_to_tensor=True)
            score = util.cos_sim(user_embedding, emb).item()

            lead["score"] = round((score + 1) / 2, 2)

        return leads