import streamlit as st
import random
def main():
    st.title("🎯 Guess the Number Game")
    # Session state to store game variables
    if 'target_number' not in st.session_state:
        st.session_state.target_number = random.randint(1, 100)
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    st.write("I'm thinking of a number between 1 and 100. Can you guess it?")
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1, format="%d")
    if st.button("Submit Guess") and not st.session_state.game_over:
        st.session_state.attempts += 1
        if guess < st.session_state.target_number:
            st.warning("Too low! Try again.")
        elif guess > st.session_state.target_number:
            st.warning("Too high! Try again.")
        else:
            st.success(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
            st.session_state.game_over = True
    if st.session_state.game_over:
        if st.button("Play Again"):
            st.session_state.target_number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.game_over = False
            st.experimental_rerun()
if __name__ == "__main__":
    main()