import streamlit as st
import requests

gemini_api_key = "AIzaSyDa7tTO-H2l1OqNbhVK4r6I_1hTcdhXi58"  # Replace with your actual API key

def generate_bio(profession, bio_style, social_media_platform):
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {gemini_api_key}"
    }
    data = {
        "prompt": f"Generate a bio for a {profession} on {social_media_platform} in {bio_style} style, including emojis.",
        "temperature": 0.7,  # Adjust temperature for creativity vs. formality
        "max_tokens": 150,  # Adjust maximum token length
        "n": 1  # Generate one bio
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        return "Error generating bio."

def main():
    st.title("BioBoost")

    profession = st.selectbox("Select your profession:", ["Programmer", "Doctor", "Businessman", "Student", "Retired", 'Lawyer', 'Engineer', 'Real Estate Agent', 'Data Scientist', 'Chef' "Other"])
    bio_style = st.selectbox("Select a bio type:", ["Professional Bio", "Creative/Artistic Bio", "Humorous Bio", "Minimalist Bio", "Inspirational Bio", "Storytelling Bio"])
    social_media_platform = st.selectbox("Select a social media platform:", ["Twitter", "Facebook", "LinkedIn", "Instagram", "TikTok"])

    if st.button("Generate Bio"):
        generated_bio = generate_bio(profession, bio_style, social_media_platform)
        st.text_area("Generated Bio:", value=generated_bio, height=200)

if __name__ == "__main__":
    main()
