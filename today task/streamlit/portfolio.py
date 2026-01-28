import streamlit as st
import base64

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="INNO_CORES | IMMORTAL",
    page_icon="♾",
    layout="wide"
)

# ================= IMMORTAL CSS =================
st.markdown("""
<style>
:root {
    --neon: #38bdf8;
    --glass: rgba(255,255,255,0.07);
    --border: rgba(255,255,255,0.18);
    --soft: #cbd5f5;
}

body {
    background: radial-gradient(circle at top, #020617, #000);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

@keyframes rise {
    from {opacity:0; transform: translateY(40px);}
    to {opacity:1; transform: translateY(0);}
}

.hero-title {
    font-size: 74px;
    font-weight: 900;
    background: linear-gradient(90deg, #38bdf8, #818cf8, #38bdf8);
    background-size: 200%;
    -webkit-background-clip: text;
    color: transparent;
}

.hero-sub {
    font-size: 28px;
    color: var(--soft);
}

.glass {
    background: var(--glass);
    border: 1px solid var(--border);
    backdrop-filter: blur(20px);
    padding: 34px;
    border-radius: 26px;
    transition: 0.4s;
}

.skill-card {
    background: linear-gradient(145deg, rgba(56,189,248,0.12), rgba(129,140,248,0.08));
    border: 1px solid rgba(56,189,248,0.4);
    padding: 22px;
    border-radius: 22px;
    margin-bottom: 22px;
}

.skill-bar {
    background: rgba(255,255,255,0.1);
    border-radius: 999px;
    overflow: hidden;
    margin-top: 10px;
}

.skill-fill {
    height: 10px;
    background: linear-gradient(90deg, #38bdf8, #818cf8);
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 100px;
}
</style>
""", unsafe_allow_html=True)

# ================= SIDEBAR =================
st.sidebar.markdown("## ♾ INNO_CORES")
menu = st.sidebar.radio(
    "Navigate",
    ["Home", "About", "Skills", "Projects", "Contact"]
)

# ================= HOME =================
if menu == "Home":
    st.markdown("""
    <div class="hero">
        <div class="hero-title">INNO_CORES</div>
        <div class="hero-sub">Code. Craft. Legacy.</div>
    </div>
    """, unsafe_allow_html=True)

    # 🔹 HERO IMAGE
    st.image(
        "https://images.unsplash.com/photo-1518770660439-4636190af475",
        caption="Building timeless systems",
        use_column_width=True
    )

    st.button("🚀 Enter the Legacy")

# ================= ABOUT =================
elif menu == "About":
    st.markdown("## About")
    st.markdown("""
    <div class="glass">
    I don’t follow trends — I build <b>timeless systems</b>.<br><br>
    🔹 Python • C • Streamlit<br>
    🔹 Web & App Development<br>
    🔹 Long-term thinking
    </div>
    """, unsafe_allow_html=True)

# ================= SKILLS =================
elif menu == "Skills":
    st.markdown("## Core Expertise")

    skills = {
        "Python": 85,
        "Streamlit": 80,
        "C Programming": 70,
        "HTML & CSS": 75,
        "Git & GitHub": 70,
        "UI / UX Thinking": 78
    }

    for skill, level in skills.items():
        st.markdown(f"""
        <div class="skill-card">
            <b>{skill}</b>
            <div class="skill-bar">
                <div class="skill-fill" style="width:{level}%"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # 🔹 SKILLS IMAGE
    st.image(
        "https://images.unsplash.com/photo-1620712943543-bcc4688e7485",
        caption="AI • Code • Innovation",
        use_column_width=True
    )

# ================= PROJECTS =================
elif menu == "Projects":
    st.markdown("## Selected Work")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1555949963-aa79dcee981c",
            use_column_width=True
        )
        st.markdown("<div class='glass'><b>Student Feedback System</b><br>Academic insight platform</div>", unsafe_allow_html=True)

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
            use_column_width=True
        )
        st.markdown("<div class='glass'><b>Travel Content App</b><br>Immersive travel experience</div>", unsafe_allow_html=True)

    with col3:
        st.image(
            "https://images.unsplash.com/photo-1517694712202-14dd9538aa97",
            use_column_width=True
        )
        st.markdown("<div class='glass'><b>GitHub Portfolio</b><br>Version-controlled identity</div>", unsafe_allow_html=True)

# ================= CONTACT =================
elif menu == "Contact":
    st.markdown("## Contact")

    with st.form("contact"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        msg = st.text_area("Message")

        if st.form_submit_button("Send ♾"):
            if name and email and msg:
                st.success("Message sent successfully 🚀")
            else:
                st.error("Complete all fields")

# ================= FOOTER =================
st.markdown("""
<div class="footer">
© 2026 INNO_CORES • IMMORTAL BUILD ♾
</div>
""", unsafe_allow_html=True)
