import streamlit as st
import re
import random
import string
from streamlit_lottie import st_lottie
import requests

# Function to load Lottie animations from a URL
def load_lottieurl(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to load Lottie animation from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"An error occurred while loading Lottie animation: {e}")
        return None

# Load Lottie animations
lottie_animation = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_3rwasyjy.json")  # Main animation
lottie_heading = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_2glqweqs.json")  # Heading animation
lottie_sidebar = load_lottieurl("https://raw.githubusercontent.com/fatii0999/myanimations/refs/heads/main/Animation%20-%201741573899249.json")  # Sidebar animation

# Custom CSS for styling and animations
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .fadeIn {
        animation: fadeIn 1.5s ease-in-out;
    }
    /* Updated button styling with purple-blue gradient */
    .stButton>button {
        background: linear-gradient(90deg, #6A0DAD 0%, #1E3A8A 100%) !important;  /* Purple to dark blue gradient */
        color: white !important;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #1E3A8A 0%, #6A0DAD 100%) !important;  /* Reverse gradient on hover */
        transform: scale(1.05);
    }
    .stTextInput>div>div>input {
        border-radius: 5px;
        padding: 10px;
        font-size: 16px;
    }
    /* Updated header styling with purple-blue gradient */
    .app-header {
        background: linear-gradient(90deg, #6A0DAD 0%, #1E3A8A 100%);  /* Purple to dark blue gradient */
        padding: 12px 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
        flex-wrap: wrap;
    }
    .header-text-container {
        flex: 1;
        min-width: 200px;
        text-align: center;
    }
    .header-text {
        color: #ffffff;  /* White text color */
        font-family: 'Arial', sans-serif;
        font-size: 28px;
        font-weight: bold;
        margin: 0;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        display: inline-block;
    }
    .header-animation {
        min-width: 150px;  /* Increased width */
        max-width: 150px;  /* Increased width */
        margin: 0 auto;
    }
    .stMarkdown h2 {
        color: #4CAF50;
        font-family: 'Arial', sans-serif;
    }
    .stMarkdown h3 {
        color: #4CAF50;
        font-family: 'Arial', sans-serif;
    }
    /* Ensure Lottie animation is visible in both light and dark themes */
    .lottie-container {
        background-color: transparent;
    }
    /* Updated footer styling with purple-blue gradient */
    .amazing-footer {
        width: 100%;
        padding: 20px;
        margin-top: 30px;
        border-radius: 8px;
        background: linear-gradient(135deg, #6A0DAD 0%, #1E3A8A 100%);  /* Purple to dark blue gradient */
        color: white;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        animation: fadeIn 1.5s ease-in-out;
    }
    .footer-quote {
        font-style: italic;
        font-size: 18px;
        margin-bottom: 15px;
        color: #f5f6fa;
    }
    .designer-credit {
        font-weight: bold;
        color: #ffffff;  /* White text color */
        font-size: 16px;
    }
    /* Password Strength Meter */
    .password-strength-meter {
        width: 100%;
        height: 10px;
        background-color: #e0e0e0;
        border-radius: 5px;
        margin-top: 10px;
        overflow: hidden;
    }
    .password-strength-meter-fill {
        height: 100%;
        transition: width 0.5s ease-in-out;
    }
    .strength-0 { background-color: #ff5252; width: 25%; }
    .strength-1 { background-color: #ff5252; width: 50%; }
    .strength-2 { background-color: #ffd740; width: 75%; }
    .strength-3 { background-color: #69f0ae; width: 100%; }
    /* Sidebar Heading Styling */
    .sidebar .stMarkdown h2 {
        color: #FFD700 !important;  /* Golden color */
        font-family: 'Arial', sans-serif;
        font-size: 24px;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    }
    .sidebar .stMarkdown h3 {
        color: #FFD700 !important;  /* Golden color */
        font-family: 'Arial', sans-serif;
        font-size: 20px;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    }
    /* Improved responsive adjustments for mobile view */
    @media (max-width: 768px) {
        .app-header {
            flex-direction: column;
            padding: 12px;
        }
        .header-text-container {
            width: 100%;
            margin-bottom: 10px;
        }
        .header-text {
            font-size: 22px;
            text-align: center;
            display: block;
        }
        .header-animation {
            width: 100%;
            min-width: auto;
            margin: 0 auto;
        }
        .stMarkdown h2 {
            font-size: 20px;
        }
        .stMarkdown h3 {
            font-size: 18px;
        }
        .stTextInput>div>div>input {
            font-size: 14px;
        }
        .stButton>button {
            font-size: 14px;
            padding: 8px 16px;
        }
        .lottie-container {
            text-align: center;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least **8 characters** long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include **both uppercase and lowercase** letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least **one number (0-9)**.")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least **one special character (!@#$%^&*)**.")

    return score, feedback

# Function to generate a random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit App
def main():
    # Sidebar with notes and animation
    with st.sidebar:
        st.markdown("## 📝 Project Notes")
        st.markdown("""
            - **Project Name**: Stronghold Password Meter
            - **Purpose**: To help users create and check strong passwords.
            - **Features**:
                - Password Strength Checker
                - Password Generator
                - Visual Feedback
            - **Designed By**: Sana Ishaq
        """)
        if lottie_sidebar:
            st_lottie(lottie_sidebar, height=200, key="sidebar")

        # Additional Features in Sidebar
        st.markdown("---")
        st.markdown("## 🚀 Additional Features")
        st.markdown("""
            - **Password History**: View previously generated passwords.
            - **Security Tips**: Get tips on how to keep your accounts secure.
            - **Dark Mode**: Switch between light and dark themes.
            - **Export Passwords**: Export generated passwords to a CSV file.
            - **Multi-Language Support**: Use the app in multiple languages.
        """)

        # Security Tips Section
        st.markdown("---")
        st.markdown("## 🔒 Security Tips")
        st.markdown("""
            - Use unique passwords for each account.
            - Enable two-factor authentication (2FA) wherever possible.
            - Avoid using easily guessable information like birthdays or names.
            - Regularly update your passwords.
            - Use a password manager to store your passwords securely.
        """)

    # Improved responsive header
    st.markdown(
        """
        <div class="app-header">
            <div class="header-text-container">
                <span class="header-text">🔐 Stronghold Password Meter🌐 </span>
            </div>
            <div class="header-animation">
        """,
        unsafe_allow_html=True,
    )
    if lottie_heading:
        st_lottie(lottie_heading, height=150, key="heading")  # Increased height
    st.markdown("</div></div>", unsafe_allow_html=True)

    # Description with Animation
    st.markdown(
        """
        <div class="fadeIn">
            <p>Welcome to <strong>Stronghold Password Meter!</strong>  
            Ensure your password is secure by checking:</p>
            <ul>
                <li>✅ Length</li>
                <li>✅ Upper & Lowercase letters</li>
                <li>✅ Numbers</li>
                <li>✅ Special Characters</li>
            </ul>
            <blockquote>⚡ <em>Improve your online security by creating strong passwords!</em></blockquote>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Input Field
    password = st.text_input("🔑 Enter your password:", type="password")

    # Password Strength Meter
    if password:
        score, _ = check_password_strength(password)
        st.markdown(f'<div class="password-strength-meter"><div class="password-strength-meter-fill strength-{score}"></div></div>', unsafe_allow_html=True)

    # Button to Check Password
    if st.button("🔍 Check Password Strength"):
        if password:
            score, feedback = check_password_strength(password)

            st.subheader("🔒 Password Strength Result:")

            if score == 4:
                st.success("✅ Strong Password! Your password is secure.", icon="🎉")
            elif score == 3:
                st.warning("⚠️ Moderate Password - Consider adding more security features.", icon="⚠️")
            else:
                st.error("❌ Weak Password - Improve it using the suggestions below.", icon="🚨")

            if feedback:
                st.info("💡 Suggestions to improve your password:")
                for tip in feedback:
                    st.write(tip)
        else:
            st.error("🚨 Please enter a password to check.")

    # Password Generator Section
    st.markdown("---")
    st.subheader("🔧 Password Generator")
    password_length = st.slider("Select password length:", min_value=8, max_value=32, value=12)
    if st.button("Generate Password"):
        generated_password = generate_password(password_length)
        st.success(f"🔐 Generated Password: `{generated_password}`")

    # Ensure Lottie Animation is always rendered
    if lottie_animation:
        st.markdown('<div class="lottie-container">', unsafe_allow_html=True)
        st_lottie(lottie_animation, height=300, key="animation")
        st.markdown('</div>', unsafe_allow_html=True)

    # Amazing Footer with Animation
    st.markdown(
        """
        <div class="amazing-footer">
            <p class="footer-quote">"The only way to do great work is to love what you do."</p>
            <p class="designer-credit">Designed by Sana</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Run the app
if __name__ == "__main__":
    main()
