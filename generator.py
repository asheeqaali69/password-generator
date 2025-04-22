import streamlit as st
import random
import string
import re

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))


def evaluate_password_strength(password):
    score = 0
    feedback = []
    
   
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if len(password) >= 16:
        score += 1
    
  
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
   
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
 
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers")
    
    # Check for special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    else:
        feedback.append("Add special characters")
    

    strength_percentage = (score / 7) * 100
    

    if strength_percentage < 40:
        strength_level = "Weak"
        color = "red"
    elif strength_percentage < 70:
        strength_level = "Moderate"
        color = "orange"
    elif strength_percentage < 90:
        strength_level = "Strong"
        color = "lightgreen"
    else:
        strength_level = "Very Strong"
        color = "green"
    
    return strength_percentage, strength_level, color, feedback

st.title("Password Generator")

length = st.slider("Select Length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Charachters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")
    
    # Display password strength
    strength_percentage, strength_level, color, feedback = evaluate_password_strength(password)
    
    st.write("### Password Strength")
    st.progress(int(strength_percentage))
    st.markdown(f"<h4 style='color: {color};'>{strength_level} ({int(strength_percentage)}%)</h4>", unsafe_allow_html=True)
    
    if feedback:
        st.write("### Suggestions to improve:")
        for suggestion in feedback:
            st.write(f"- {suggestion}")
