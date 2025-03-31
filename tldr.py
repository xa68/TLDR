import streamlit as st

def user_id_entry():
    """Creates a user entry interface with a grid."""

    st.subheader("Enter user id")

    # Initialize user id in session state if it doesn't exist
    if "user_id" not in st.session_state:
        st.session_state.user_id = ""

    # Display the entered id (masked for security)
    masked_id = "*" * len(st.session_state.user_id)
    st.write(f"User id: {masked_id}")

    # Create a container for the grid
    grid_container = st.container()

        # CSS to control button widths and container width
    container_css = """
    <style>
        div[data-testid="column"] button {
            width: 100%; /* Make buttons fill the column width */
            margin-bottom: 5px; /* Add some spacing between buttons */
        }
        div[data-testid="stVerticalBlock"] {
            width: 300px; /* Adjust the width of the container as needed */
            margin: 0 auto; /* Center the container horizontally */
        }
    </style>
    """
    st.markdown(container_css, unsafe_allow_html=True)
    
    # Create the number grid within the container
    with grid_container:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            if st.button('a', key='a'):
                st.session_state.user_id += 'a'
            if st.button('b', key='b'):
                st.session_state.user_id += 'b'
            if st.button('c', key='c'):
                st.session_state.user_id += 'c'
        with col2:
            if st.button("d", key="d"):
                st.session_state.user_id += "d"
            if st.button("e", key="e"):
                st.session_state.user_id += "e"
            if st.button("f", key="f"):
                st.session_state.user_id += "f"  
        with col3:
            if st.button("1", key="1"):
                st.session_state.user_id += "1"
            if st.button("4", key="4"):
                st.session_state.user_id += "4"
            if st.button("7", key="7"):
                st.session_state.user_id += "7"
        with col4:
            if st.button("2", key="2"):
                st.session_state.user_id += "2"
            if st.button("5", key="5"):
                st.session_state.user_id += "5"
            if st.button("8", key="8"):
                st.session_state.user_id += "8"
            if st.button("0", key="0"):
                st.session_state.user_id += "0"
        with col5:
            if st.button("3", key="3"):
                st.session_state.user_id += "3"
            if st.button("6", key="6"):
                st.session_state.user_id += "6"
            if st.button("9", key="9"):
                st.session_state.user_id += "9"      
            if st.button("Clear", key="clear"):
                st.session_state.user_id = ""

    # Enter button
    if st.button("Enter", key="enter"):
        # Here you would add your pin validation logic
        if st.session_state.user_id == "1234":  # Example: Check against a correct pin
            st.success("ID entered successfully.")
        else:
            st.error("ID entered incorrectly.")
        st.session_state.user_id = ""  # Clear the pin after submission

# --- Main App ---
st.title("TL;DR")

st.title("User id entry")
user_id_entry()

# Add a URL entry field
url_label_css = """<style>
    .stTextInput>label:before { content: "🔗"; font-size: 24px;}
    .stTextInput>label>div { font-size: 20px; }
    </style>"""
st.markdown(url_label_css, unsafe_allow_html=True)
url = st.text_input("URL", "")


# CSS to target the slider label
slider_label_css = "<style>.stSlider>label>div { font-size: 24px; }</style>"
st.markdown(slider_label_css, unsafe_allow_html=True)
bullet_points = st.slider('Nr. of bullet points', 1, 5, 3)
