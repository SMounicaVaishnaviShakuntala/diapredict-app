import streamlit as st
import pandas as pd
import joblib
import streamlit.components.v1 as components
import plotly.express as px

st.set_page_config(layout="wide")

# ===================== GLOBAL STYLES =====================
st.markdown("""
<style>

/* Background */
/* ===== FINAL MEDICAL DASHBOARD BACKGROUND ===== */
.stApp {
    background: linear-gradient(
        135deg,
        #f7fbff 0%,
        #e6f2ff 35%,
        #d9ecff 70%,
        #eef6ff 100%
    );
}

/* Container padding */

.block-container {
    padding: 4rem 3rem 2rem 3rem !important;
}


/* ===================== TABS STYLING ===================== */

/* Remove underline & move right */
div[data-testid="stTabs"] div[role="tablist"] {
    border-bottom: none !important;
    justify-content: flex-end !important;
}

div[data-testid="stTabs"] {
    border-bottom: none !important;
}

/* Tab button */
button[data-baseweb="tab"] {
    background-color: rgba(255,255,255,0.7) !important;
    padding: 10px 28px !important;
    border-radius: 30px !important;
    margin: 0 8px;
    font-weight: 600;
    border: none !important;
}

/* Active tab */
button[data-baseweb="tab"][aria-selected="true"] {
    background-color: #4a90e2 !important;
    color: white !important;
}

/* Hover = Hero Blue */
button[data-baseweb="tab"]:hover {
    background-color: #4a90e2 !important;
    color: white !important;
}

}
 /* ===== RESET FORM TO DEFAULT STREAMLIT LOOK ===== */
div[data-testid="stForm"] {
    background: transparent !important;
    box-shadow: none !important;
    border: none !important;
    padding: 0 !important;
    border-radius: 0 !important;
}



/* ===== SLIM & VERTICAL FORM ===== */

/* Center form and reduce width */
div[data-testid="stForm"] {
    max-width: 600px !important;
    margin: auto !important;
}

/* Make inputs slim */
div[data-testid="stNumberInput"] {
    margin-bottom: 18px !important;
}

/* Reduce input box width */
div[data-testid="stNumberInput"] input {
    height: 38px !important;
    font-size: 15px !important;
}

/* Make button centered */
div[data-testid="stFormSubmitButton"] {
    text-align: center !important;
}

/* ===== HERO STYLE FORM ===== */
div[data-testid="stForm"] {
    background: linear-gradient(90deg, #4a90e2, #6fb1fc) !important;  
    max-width: 720px !important;   /* Increased ~20% from 600px */
    margin: auto !important;
    padding: 45px 40px !important;
    border-radius: 30px !important;
    box-shadow: 0px 18px 40px rgba(0,0,0,0.15) !important;
}

/* Labels white */
label {
    color: white !important;
    font-weight: 500 !important;
}

/* Input boxes clean & contrasting */
div[data-testid="stNumberInput"] input {
    background-color: white !important;
    border-radius: 12px !important;
    height: 40px !important;
    border: none !important;
    font-size: 15px !important;
}

/* Space between inputs */
div[data-testid="stNumberInput"] {
    margin-bottom: 20px !important;
}

/* Center button */
div[data-testid="stFormSubmitButton"] {
    text-align: center !important;
}

.result-box {
    margin-top: 25px;
    padding: 20px;
    border-radius: 14px;
    text-align: center;
    color: white;
    font-size: 20px;
    font-weight: bold;
    width: 40%;
    margin-left: auto;
    margin-right: auto;
}

iframe {
    border-radius: 30px !important;
    overflow: hidden !important;
}

/* ===== MODERN CARD SECTION (Like Microsoft Style) ===== */

.section2-wrapper {
    margin-top: 60px;
}

.section2-title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    color: #1f2937;
    margin-bottom: 10px;
}

.section2-subtitle {
    text-align: center;
    font-size: 18px;
    color: #4b5563;
    margin-bottom: 50px;
}

.modern-card {
    background: #f3f4f6;
    border-radius: 28px;
    padding: 20px;
    transition: all 0.4s ease;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.08);
}

.modern-card:hover {
    transform: translateY(-8px);
    box-shadow: 0px 18px 40px rgba(0,0,0,0.18);
}

.modern-card img {
    width: 100%;
    height: 240px;
    object-fit: cover;
    border-radius: 20px;
}

.card-title {
    font-size: 22px;
    font-weight: 700;
    margin-top: 18px;
    color: #111827;
}

.card-desc {
    font-size: 16px;
    color: #4b5563;
    margin-top: 10px;
    line-height: 1.6;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 40px;
    margin-bottom: 25px;
    color: #1f2937;
}           
        

</style>
""", unsafe_allow_html=True)

# ===================== MODEL =====================
model = joblib.load("diabetes_lr_v1.pkl")

def risk_level(p):
    if p < 0.4:
        return "Low Risk", "#2ecc71"
    elif p < 0.7:
        return "Medium Risk", "#f39c12"
    else:
        return "High Risk", "#e74c3c"

# ===================== TOP TABS =====================

tab1, tab2, tab3 = st.tabs(["Home", "Predict", "Insights"])


# ===================== HOME =====================
with tab1:

    
# ===================== HERO SECTION =====================
    components.html("""
    <div style="
        background: linear-gradient(90deg, #4a90e2, #6fb1fc);
        padding: 35px 40px 25px 40px;
        border-radius: 30px;
        overflow: hidden;
        text-align: center;
        color: white;
        box-shadow: 0px 12px 28px rgba(0,0,0,0.2);
        font-family: Arial, sans-serif;
        height: 240px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
    ">

        <h1 style="
            margin-bottom:18px;
            font-size:48px;
            font-weight:700;
        ">
            DiaPredict
        </h1>

        <div id="typewriter" style="
            font-size:18px; 
            max-width:800px; 
            margin-left:auto; 
            margin-right:auto;
            line-height:1.7;
            height:100px;
            overflow:hidden;
        "></div>

    </div>

    <script>
    const text = "This system uses Machine Learning to analyze patient health parameters such as glucose level, BMI, insulin, and age. It predicts diabetes risk probability and provides personalized insights to support early detection and preventive care.";

    let i = 0;
    function typeWriter() {
        if (i < text.length) {
            document.getElementById("typewriter").innerHTML += text.charAt(i);
            i++;
            setTimeout(typeWriter, 18);
        }
    }
    typeWriter();
    </script>
    """, height=280)

    st.markdown('<div class="section-title"> Potential Complications of Undiagnosed Diabetes</div>', unsafe_allow_html=True)

    # Top Row (3 images)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("vision_loss.png", width=520)

        st.markdown(
            "<div style='font-size:20px; font-weight:700; margin-top:10px;'>Vision Loss</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div style='font-size:18px; color:#444;'>Damage to blood vessels in the retina affecting eyesight.</div>",
            unsafe_allow_html=True
        )

    with col2:
        st.image("kidney_damage.png", width=520)

        st.markdown(
            "<div style='font-size:20px; font-weight:700; margin-top:10px;'>Kidney Damage</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div style='font-size:18px; color:#444;'>Long-term high glucose levels can impair kidney function.</div>",
            unsafe_allow_html=True
        )

    # 3️⃣ Heart Disease
    with col3:
        st.image("heart_disease.png", width=520)

        st.markdown(
            "<div style='font-size:20px; font-weight:700; margin-top:10px;'>Heart Disease</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div style='font-size:18px; color:#444;'>Increased cardiovascular risk due to uncontrolled diabetes.</div>",
            unsafe_allow_html=True
        )

    st.markdown("<br><br>", unsafe_allow_html=True)

    col4, col5, col6, col7 = st.columns([1,2,2,1])


    with col5:
        st.image("nerve_damage.png", width=520)

        st.markdown(
            "<div style='font-size:20px; font-weight:700; margin-top:10px;'>Nerve Damage</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div style='font-size:18px; color:#444;'>High glucose causing nerve damage.</div>",
            unsafe_allow_html=True
        )

    with col6:
        st.image("chronic_fatigue.png", width=520)

        st.markdown(
            "<div style='font-size:20px; font-weight:700; margin-top:10px;'>Chronic Fatigue</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div style='font-size:18px; color:#444;'>Persistent tiredness caused by glucose imbalance.</div>",
            unsafe_allow_html=True
        )

    # SECTION 3

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("## Preventive Measures and Risk Reduction")
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns([2,3])

    with col1:
        st.image("healthy_diet.png", width=520)

    with col2:
        st.markdown(
            "<div style='font-size:26px; font-weight:700;'>Healthy Diet</div>",
            unsafe_allow_html=True
        )
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(
            "<div style='font-size:20px; line-height:1.7; color:#444;'>"
            "Maintaining a balanced diet with controlled sugar intake helps regulate blood glucose levels "
            "and reduces the risk of long-term complications. Including whole grains, vegetables, lean " \
            "proteins, and healthy fats supports overall metabolic health. Limiting processed foods and sugary beverages plays a key role in preventing sudden spikes in blood sugar. Consistent dietary habits contribute significantly to long-term diabetes prevention and management."       
            "</div>",
            unsafe_allow_html=True
        )


    st.markdown("<br><br>", unsafe_allow_html=True)

    col3, col4 = st.columns([3,2])

    with col3:
        st.markdown(
            "<div style='font-size:26px; font-weight:700;'>Regular Physical Activity</div>",
            unsafe_allow_html=True
        )
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(
            "<div style='font-size:20px; line-height:1.7; color:#444;'>"
            "Engaging in regular physical activity improves insulin sensitivity, supports weight management, "
            "and helps maintain stable blood sugar levels. Activities such as walking, jogging, or light " \
            "strength training enhance cardiovascular health and overall fitness. Even moderate daily movement can reduce the risk of developing diabetes-related complications. Consistency in physical activity is essential for maintaining long-term metabolic balance."
            "</div>",
            unsafe_allow_html=True
        )

    with col4:
        st.image("jogging.png", width=520)

    st.markdown("<br><br>", unsafe_allow_html=True)

    col5, col6 = st.columns([2,3])

    with col5:
        st.image("doc_consultation.png", width=520)

    with col6:
        st.markdown(
            "<div style='font-size:26px; font-weight:700;'>Regular Monitoring & Consultation</div>",
            unsafe_allow_html=True
        )
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(
            "<div style='font-size:20px; line-height:1.7; color:#444;'>"
            "Routine health checkups and timely medical consultation enable early detection and effective " \
            "management of diabetes. Regular blood glucose monitoring helps identify abnormal patterns before" \
            " complications arise. Professional medical guidance ensures appropriate lifestyle adjustments and treatment plans when necessary. Early intervention significantly reduces the risk of serious long-term health issues."
            "</div>",
            unsafe_allow_html=True
        )

# ===================== PREDICT =====================
with tab2:

    st.markdown("### Enter Patient Health Parameters")

    with st.form("patient_form"):
        col1, col2 = st.columns(2)

        with col1:
            preg = st.number_input("Pregnancies", step=1, value=0)
            glucose = st.number_input("Glucose", value=120)
            bp = st.number_input("Blood Pressure", value=70)

        with col2:
            insulin = st.number_input("Insulin", value=80)
            bmi = st.number_input("BMI", value=25.0, format="%.2f")
            age = st.number_input("Age", step=1, value=30)

        submit = st.form_submit_button("Predict Diabetes Risk")

    if submit:
        input_data = pd.DataFrame(
            [[preg, glucose, bp, 20, insulin, bmi, 0.5, age]],
            columns=[
                "Pregnancies", "Glucose", "BloodPressure",
                "SkinThickness", "Insulin", "BMI",
                "DiabetesPedigreeFunction", "Age"
            ]
        )

        st.session_state["last_input"] = input_data
        prob = model.predict_proba(input_data)[0][1]
        risk, color = risk_level(prob)

        # Show Risk Box
        st.markdown(
            f"""
            <div class='result-box' style='background-color:{color};'>
                Risk Level: {risk}<br>
                Probability: {prob*100:.2f}%
            </div>
            """,
            unsafe_allow_html=True
        )


    

# ===================== INSIGHTS =====================
with tab3:

    st.markdown("## Your AI Risk Insights")

    if "last_input" not in st.session_state:
        st.info("Please predict risk first.")
    else:
        user_data = st.session_state["last_input"]
        coefs = model.coef_[0]

        contributions = user_data.iloc[0].values * coefs

        insight_df = pd.DataFrame({
            "Feature": user_data.columns,
            "Contribution": contributions
        })

        # Remove unwanted features
        insight_df = insight_df[
            ~insight_df["Feature"].isin(["SkinThickness", "DiabetesPedigreeFunction"])
        ]

        # 🔥 ADD THIS HERE
        insight_df["Feature"] = insight_df["Feature"].apply(lambda x: f"<b>{x}</b>")


        # ================= GRAPH FIRST =================

        import plotly.express as px

        fig = px.bar(
            insight_df,
            x="Feature",
            y="Contribution",
            color_discrete_sequence=["#4a90e2"]
        )

        fig.update_layout(
            plot_bgcolor="#f7fbff",
            paper_bgcolor="#f7fbff",
            font=dict(color="#2c3e50", size=14),

            xaxis=dict(
                showgrid=False,
                title=dict(
                    text="<b>Feature</b>",
                    font=dict(size=16)
                )
            ),

            yaxis=dict(
                showgrid=True,
                gridcolor="#e6eef5",
                title=dict(
                    text="<b>Contribution</b>",
                    font=dict(size=16)
                )
            ),

            margin=dict(l=20, r=20, t=20, b=20)
        )


        fig.update_traces(
            marker_line_width=0
        )

        st.plotly_chart(
    fig,
    use_container_width=True,
    config={
        "displaylogo": False,   # Removes Plotly logo
        "modeBarButtonsToRemove": [
            "zoom2d",
            "pan2d",
            "select2d",
            "lasso2d",
            "zoomIn2d",
            "zoomOut2d",
            "autoScale2d",
            "resetScale2d",
            "toImage"
        ]
    }
)

        st.markdown(
            "<big><b>Note:</b> Positive bars indicate higher contribution towards diabetes risk, "
            "while negative bars indicate lower contribution.</big>",
            unsafe_allow_html=True
        )

        insight_df_sorted = insight_df.reindex(
        insight_df["Contribution"].abs().sort_values(ascending=False).index
)

        # Get top 3 factors
        
        top3 = insight_df_sorted.head(3)

        st.markdown("<br>", unsafe_allow_html=True)

        # ================= BOXES BELOW GRAPH =================
        col1, col2 = st.columns(2)

        # ----------- TOP FACTORS BOX -----------
        with col1:
            st.markdown(f"""
            <div style="
                background: linear-gradient(90deg, #4a90e2, #6fb1fc);
                padding: 30px;
                border-radius: 25px;
                color: white;
                box-shadow: 0px 12px 28px rgba(0,0,0,0.2);
                min-height: 220px;
            ">
                <h3>Top Factors Influencing</h3>
                <ul style="font-size:22px; line-height:1.8;">
                    <li>{top3.iloc[0]['Feature']}</li>
                    <li>{top3.iloc[1]['Feature']}</li>
                    <li>{top3.iloc[2]['Feature']}</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        # ----------- HEALTH INSIGHT BOX -----------
        with col2:

            main_factor = top3.iloc[0]['Feature']

            advice = {
                "Glucose": "Maintain balanced blood sugar levels through controlled diet and regular monitoring.",
                "BMI": "Focus on weight management with healthy diet and daily physical activity.",
                "Age": "Regular health checkups are important as risk increases with age.",
                "Insulin": "Monitor insulin levels and consult doctor if irregular.",
                "BloodPressure": "Control blood pressure with low-sodium diet and exercise.",
                "Pregnancies": "Post-pregnancy glucose monitoring is recommended."
            }

            suggestion = advice.get(
                main_factor,
                "Maintain healthy lifestyle and consult healthcare professional."
            )

            st.markdown(f"""
            <div style="
                background: linear-gradient(90deg, #4a90e2, #6fb1fc);
                padding: 30px;
                border-radius: 25px;
                color: white;
                box-shadow: 0px 12px 28px rgba(0,0,0,0.2);
                min-height: 220px;
            ">
                <h3>Health Insight</h3>
                <p style="font-size:22px; line-height:1.8;">
                    {suggestion}
                </p>
            </div>
            """, unsafe_allow_html=True)
