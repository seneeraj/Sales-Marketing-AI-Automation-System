import streamlit as st
import pandas as pd
import urllib.parse
import traceback
import matplotlib.pyplot as plt

from agents.orchestrator import Orchestrator
from utils.db import init_db, save_post, get_all_posts, delete_post

# -------------------------------
# 🎨 PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Sales & Marketing AI Automation System", layout="wide")
st.title("🚀 Sales & Marketing AI Automation System")

# -------------------------------
# 🧠 INIT DB + SESSION
# -------------------------------
init_db()

if "result" not in st.session_state:
    st.session_state.result = None

if "saved_msg" not in st.session_state:
    st.session_state.saved_msg = ""

# -------------------------------
# 📌 SIDEBAR INPUT
# -------------------------------
st.sidebar.header("🎯 Input")

user_input = st.sidebar.text_area(
    "What do you want to achieve?",
    placeholder="e.g. Build AI personal brand..."
)

uploaded_file = st.sidebar.file_uploader(
    "Upload Leads CSV",
    type=["csv"]
)

tone = st.sidebar.selectbox(
    "Select Content Tone",
    ["viral", "expert", "storytelling"]
)

run_button = st.sidebar.button("🚀 Run AI")

# -------------------------------
# 🧠 CACHE ORCHESTRATOR (PERFORMANCE FIX)
# -------------------------------
@st.cache_resource
def get_orchestrator():
    return Orchestrator()

orch = get_orchestrator()

# -------------------------------
# 🚀 RUN SYSTEM
# -------------------------------
if run_button:

    if not user_input.strip():
        st.warning("Please enter your goal")

    else:
        status = st.empty()
        status.info("🤖 Generating AI content... Please wait")

        try:
            result = orch.run(user_input, uploaded_file, tone)
            st.session_state.result = result
            status.success("✅ Content generated successfully!")

        except Exception:
            status.error("❌ Execution Error")
            st.error(traceback.format_exc())

# -------------------------------
# 🧠 LOAD RESULT
# -------------------------------
result = st.session_state.result

if result is not None:

    decision = result.get("decision") or {}
    results = result.get("results") or {}

    steps = decision.get("steps", [])

    # -------------------------------
    # 🧠 STRATEGY
    # -------------------------------
    st.markdown("## 🧠 Strategy")

    if not steps:
        st.warning("No steps generated")
    else:
        for step in steps:
            st.success(f"✅ {step.capitalize()}")

    st.caption(decision.get("reason", ""))

    # -------------------------------
    # 📊 RESULTS
    # -------------------------------
    st.markdown("## 📊 Results")

    # -------------------------------
    # ✍️ CONTENT
    # -------------------------------
    if results.get("content"):

        st.markdown("### ✍️ AI Generated Content")

        posts = results["content"]

        if st.session_state.saved_msg:
            st.success(st.session_state.saved_msg)
            st.session_state.saved_msg = ""

        for i, post in enumerate(posts, 1):

            st.markdown(f"#### 🔥 Post {i}")
            st.write(post)

            col1, col2, col3 = st.columns(3)

            # 📋 COPY
            with col1:
                st.code(post, language="text")

            # 💾 SAVE
            with col2:
                if st.button(f"💾 Save Post {i}", key=f"save_{i}"):
                    save_post(post)
                    st.session_state.saved_msg = f"Post {i} saved successfully!"

            # 🔗 LINKEDIN
            with col3:
                encoded = urllib.parse.quote(post)
                url = f"https://www.linkedin.com/feed/?shareActive=true&text={encoded}"
                st.markdown(f"[🚀 Post to LinkedIn](<{url}>)")

            st.divider()

        # 📥 DOWNLOAD
        df = pd.DataFrame({"posts": posts})
        st.download_button(
            "📥 Download Posts",
            df.to_csv(index=False).encode(),
            "posts.csv"
        )

    # -------------------------------
    # 🎯 LEADS
    # -------------------------------
    if results.get("leads"):
        st.markdown("### 🎯 Leads")
        df = pd.DataFrame(results["leads"])
        st.dataframe(df)

    # -------------------------------
    # 📧 EMAILS
    # -------------------------------
    if results.get("emails"):
        st.markdown("### 📧 Emails")
        for i, email in enumerate(results["emails"], 1):
            st.write(email)
            st.divider()

    # -------------------------------
    # 📊 ANALYTICS (GRAPHS)
    # -------------------------------
    if results.get("analytics"):

        st.markdown("### 📊 Analytics Dashboard")

        analytics = results["analytics"]
        leads = results.get("leads", [])

        if leads:
            df = pd.DataFrame(leads)

            # 📊 Distribution
            st.subheader("Lead Score Distribution")

            bins = [0, 0.4, 0.7, 1.0]
            labels = ["Low", "Medium", "High"]

            df["category"] = pd.cut(df["score"], bins=bins, labels=labels)
            counts = df["category"].value_counts().sort_index()

            fig = plt.figure()
            plt.bar(counts.index.astype(str), counts.values)
            st.pyplot(fig)

            # 🔥 Funnel
            st.subheader("Conversion Funnel")

            total = len(df)
            qualified = len(df[df["score"] > 0.5])
            high_quality = len(df[df["score"] > 0.7])

            fig2 = plt.figure()
            plt.bar(
                ["Total", "Qualified", "High Quality"],
                [total, qualified, high_quality]
            )
            st.pyplot(fig2)

        # 📈 Metrics
        st.subheader("Key Metrics")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Avg Score", round(analytics.get("avg_score", 0), 2))

        with col2:
            st.metric("Total Leads", len(leads))

# -------------------------------
# 💾 SAVED POSTS (WITH DELETE)
# -------------------------------
st.markdown("## 💾 Saved Posts")

saved_posts = get_all_posts()

if not saved_posts:
    st.info("No saved posts yet.")
else:
    for i, (post_id, content, created_at) in enumerate(saved_posts, 1):

        st.markdown(f"### 📝 Saved Post {i}")
        st.caption(f"Saved at: {created_at}")
        st.write(content)

        col1, col2 = st.columns([4, 1])

        with col2:
            if st.button("🗑 Delete", key=f"delete_{post_id}"):
                delete_post(post_id)
                st.success("Deleted!")
                st.rerun()

        st.divider()