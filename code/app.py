import streamlit as st
import time

# Page config
st.set_page_config(page_title="DevOps Portal", layout="wide")

# Custom CSS for UI
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}
.stButton>button {
    background-color: #00c6ff;
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.title("🚀 DevOps Registration Portal")
st.write("Unlock exclusive DevOps projects after registration!")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Register", "About"])

# About Page
if page == "About":
    st.subheader("About This App")
    st.write("This is a DevOps onboarding platform built using Streamlit.")
    st.write("Register and unlock real-world DevOps projects!")

# Registration Page
if page == "Register":
    st.subheader("📝 Registration Form")

    with st.form("registration_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        role = st.selectbox("Select Role", ["DevOps Engineer", "Cloud Engineer", "SRE", "Student"])
        experience = st.slider("Years of Experience", 0, 10, 1)
        skills = st.multiselect("Skills", ["Docker", "Kubernetes", "AWS", "Terraform", "Jenkins", "Linux"])
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Register")

    if submit:
        if name and email and password:
            st.success(f"Welcome {name}! 🎉 Registration Successful")

            # Loading animation
            with st.spinner("Unlocking your DevOps projects..."):
                time.sleep(2)

            # Exciting reveal
            st.balloons()
            st.subheader("🔥 You Unlocked Exclusive DevOps Projects!")

            st.markdown("""
            ### 🚀 Your Projects:
            - CI/CD Pipeline using Jenkins
            - Kubernetes Deployment with Helm
            - Terraform AWS Infrastructure
            - Dockerized Microservices App
            - Monitoring with Prometheus & Grafana
            """)

            st.info("Start building now and boost your DevOps career!")
        else:
            st.error("Please fill all required fields!")

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")
