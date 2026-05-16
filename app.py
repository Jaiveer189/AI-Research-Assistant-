import streamlit as st
import requests

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🧠",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.stTextArea textarea {
    border-radius: 12px;
    font-size: 16px;
}

.stButton button {
    width: 100%;
    border-radius: 10px;
    height: 50px;
    font-size: 16px;
    font-weight: bold;
}

.report-box {
    background-color: #1E1E1E;
    padding: 25px;
    border-radius: 15px;
    margin-top: 20px;
    border: 1px solid #333;
}

.section-title {
    font-size: 22px;
    font-weight: bold;
    margin-top: 20px;
    color: #FFFFFF;
}

</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("⚙️ Settings")

model = st.sidebar.selectbox(
    "Select AI Model",
    [
        "GPT-4o",
        "Claude 3.5",
        "Gemini 2.5",
        "DeepSeek"
    ]
)

report_length = st.sidebar.selectbox(
    "Report Length",
    [
        "Short",
        "Medium",
        "Detailed"
    ]
)

export_button = st.sidebar.button("📄 Export Report")

# ---------------- MAIN AREA ---------------- #
st.title("🧠 AI Research Assistant")
st.caption("Generate AI-powered research reports using n8n workflows.")

topic = st.text_area(
    "Enter Research Topic",
    placeholder="Example: Future of AI Agents in Healthcare",
    height=180
)

generate = st.button("🚀 Generate Report")

# ---------------- GENERATE REPORT ---------------- #
if generate:

    if topic.strip() == "":
        st.warning("Please enter a research topic.")

    else:

        with st.spinner("Generating research report..."):

            try:

                # ---------------- WEBHOOK REQUEST ---------------- #


                response = requests.post(
    "https://jaiveershekhawat.app.n8n.cloud/webhook-test/test123",
    json={"hello": "world"}
)

                print(response.status_code)
                print(response.text)

                # ---------------- DEBUG STATUS ---------------- #
                st.write("Status Code:", response.status_code)

                # ---------------- CHECK RESPONSE ---------------- #
                if response.status_code == 200:

                    data = response.json()

                    # Debug JSON
                    # st.json(data)

                    if "report" in data:

                        st.success("Research Report Generated!")

                        st.markdown(f"""
                        <div class="report-box">
                        <div class="section-title">📘 AI Research Report</div>
                        <br>
                        {data["report"]}
                        </div>
                        """, unsafe_allow_html=True)

                    else:
                        st.error("No 'report' key found in API response.")
                        st.json(data)

                else:
                    st.error(f"Request Failed: {response.status_code}")
                    st.text(response.text)

            except requests.exceptions.Timeout:
                st.error("Request timed out.")

            except requests.exceptions.ConnectionError:
                st.error("Connection error. Check your webhook URL.")

            except Exception as e:
                st.error(f"Error: {e}")

# ---------------- EXPORT BUTTON ---------------- #
if export_button:
    st.sidebar.info("Export feature coming in Version 2.")