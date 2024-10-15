import streamlit as st
import requests

def generate_bio(profession, bio_style, social_media_platform, gemini_api_key):
    # ... (rest of your generate_bio function)

def main():
    st.title("BioBoost")

    profession = st.selectbox("Select your profession:", ["Programmer", "Doctor", "Businessman", "Student", "Retired", "Other"])
    bio_style = st.selectbox("Select a bio type:", ["Professional Bio", "Creative/Artistic Bio", "Humorous Bio", "Minimalist Bio", "Inspirational Bio", "Storytelling Bio"])
    social_media_platform = st.selectbox("Select a social media platform:", ["Twitter", "Facebook", "LinkedIn", "Instagram", "TikTok"])

    gemini_api_key = st.text_input("Enter your Gemini API key:")

    if st.button("Generate Bio"):
        if gemini_api_key:
            generated_bio = generate_bio(profession, bio_style, social_media_platform, gemini_api_key)
            st.text_area("Generated Bio:", value=generated_bio, height=200)
        else:
            st.warning("Please enter your Gemini API key.")

if __name__ == "__main__":
    main()
