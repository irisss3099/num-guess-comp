import random
import streamlit as st

# ------------------ Page Setup ------------------
st.set_page_config(page_title="🎯 Guess the Number Game", page_icon="🎮", layout="centered")

# Background styling using HTML & CSS
st.markdown("""
    <style>
        
        body {
            background-color: #ffe6f0;
        }
        .stApp {
            background-color: #fff0f5;
            padding: 2rem;
            border-radius: 12px;
        }
        h1 {
            color: #d63384;
            text-align: center;
        }
        .footer {
            margin-top: 2rem;
            text-align: center;
            color: #888;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------ Title ------------------
st.markdown("<h1>🎯 Guess the Number Game</h1>", unsafe_allow_html=True)
st.write("I'm thinking of a number between **1 and 100**. Can you guess it? 🤔")

# ------------------ Game Logic ------------------
if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.guessed = False

with st.container():
    st.markdown('<div class="guess-box">', unsafe_allow_html=True)

    if not st.session_state.guessed:
        guess = st.number_input("🔢 Enter your guess:", min_value=1, max_value=100, step=1, key="guess_input")

        if st.button("💌 Submit Guess"):
            st.session_state.attempts += 1

            if guess < st.session_state.number_to_guess:
                st.warning("📉 Too low! Try a higher number.")
            elif guess > st.session_state.number_to_guess:
                st.warning("📈 Too high! Try a lower number.")
            else:
                st.success(f"🎉 Woohoo! You guessed it right! It was **{st.session_state.number_to_guess}**.")
                st.balloons()
                st.session_state.guessed = True
                st.write(f"💡 You found it in **{st.session_state.attempts} attempts**.")

    # Restart Option
    if st.session_state.guessed:
        st.markdown("---")
        if st.button("🔄 Play Again"):
            st.session_state.number_to_guess = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.guessed = False
            st.experimental_rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------ Footer ------------------
st.markdown('<div class="footer">Developed by Sabila Aleem ❤</div>', unsafe_allow_html=True)





