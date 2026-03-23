class ConversionAgent:

    def generate_email(self, lead):
        return f"""
Hi {lead['name']},

I noticed your interest in {lead['interest']}.

We help businesses grow using AI-driven solutions like automation, marketing, and lead generation.

Would you be open to a quick discussion?

Best regards,  
AI Growth Team
"""