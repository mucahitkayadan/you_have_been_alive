import streamlit as st
from datetime import datetime, date


# Function to calculate days since birth
def calculate_days_since_birth(birthdate):
    current_date = datetime.now().date()  # Convert to date object
    days_since_birth = (current_date - birthdate).days
    return days_since_birth


# Main function to run the Streamlit app
def main():
    # Add custom CSS for the dynamic background
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://images.unsplash.com/photo-1542281286-9e0a16bb7366');
            background-size: cover;
            background-attachment: fixed;
        }
        .main {
            background: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("How Many Days Have You Been Alive?")

    # Create a container for the content
    with st.container():
        birthdate = st.date_input("Select your birthdate:", value=date(2000, 1, 1))

        if st.button("Calculate Days"):
            days = calculate_days_since_birth(birthdate)
            st.success(f"You have been alive for {days} days.")


# Run the main function
if __name__ == "__main__":
    main()
