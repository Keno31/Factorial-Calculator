import streamlit as st
import factorial as fact

def main():
    st.title("FACTORIAL CALCULATOR")
    number = st.number_input("Enter a number:",
                             min_value=0,
                             max_value=999)
    if st.button("Calculate"):
        result = fact.fact(number)
        st.write(f"The factorial of {number} is {result}")
        st.balloons()

if __name__ == "__main__":
    main()