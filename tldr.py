import streamlit as st

def user_id_entry():
    """Creates a user id entry grid in the sidebar."""

    st.sidebar.subheader('Enter user id:')

    # Initialize user id in session state if it doesn't exist
    if "user_id" not in st.session_state:
        st.session_state.user_id = ""

    st.session_state.user_id = st.sidebar.text_input("🆔 ", "your id goes here")

    # # Create a container for the grid
    # grid_container = st.sidebar.container()

    #     # CSS to control button widths and container width
    # container_css = """
    # <style>
    #     div[data-testid="column"] button {
    #         width: 100%; /* Make buttons fill the column width */
    #         margin-bottom: 5px; /* Add some spacing between buttons */
    #     }
    #     div[data-testid="stVerticalBlock"] {
    #         width: 300px; /* Adjust the width of the container as needed */
    #         margin: 0 auto; /* Center the container horizontally */
    #     }
    # </style>
    # """
    # st.markdown(container_css, unsafe_allow_html=True)
    
    # # Create the number grid within the container
    # with grid_container:
    #     col1, col2, col3 = st.columns(3)
    #     with col1:
    #         if st.button('a', key='a'):
    #             st.session_state.user_id += 'a'
    #         if st.button("d", key="d"):
    #             st.session_state.user_id += "d"
    #         if st.button("1", key="1"):
    #             st.session_state.user_id += "1"
    #         if st.button("4", key="4"):
    #             st.session_state.user_id += "4"
    #         if st.button("7", key="7"):
    #             st.session_state.user_id += "7"
            

    #     with col2:
    #         if st.button('b', key='b'):
    #             st.session_state.user_id += 'b'
    #         if st.button("e", key="e"):
    #             st.session_state.user_id += "e"
    #         if st.button("2", key="2"):
    #             st.session_state.user_id += "2"
    #         if st.button("5", key="5"):
    #             st.session_state.user_id += "5"
    #         if st.button("8", key="8"):
    #             st.session_state.user_id += "8"
    #         if st.button("0", key="0"):
    #             st.session_state.user_id += "0"

    #     with col3:
    #         if st.button('c', key='c'):
    #             st.session_state.user_id += 'c'
    #         if st.button("f", key="f"):
    #             st.session_state.user_id += "f"
    #         if st.button("3", key="3"):
    #             st.session_state.user_id += "3"
    #         if st.button("6", key="6"):
    #             st.session_state.user_id += "6"
    #         if st.button("9", key="9"):
    #             st.session_state.user_id += "9"      
    #         if st.button("Clear", key="clear"):
    #             st.session_state.user_id = ""              

        # # Display the entered id (masked for security)
        # masked_id = "*" * len(st.session_state.user_id)
        # st.write(f"Keyed in: {masked_id}")

    # Enter button
    if st.sidebar.button("Check ID", key="check"):
        # user id validation
        if st.session_state.user_id in st.secrets["user_ids"]: 
            st.sidebar.success("ID entered successfully.")
            st.session_state.user_status = "OK"
        else:
            st.sidebar.error("ID entered incorrectly.")
            st.session_state.user_status = "KO"
        st.session_state.user_id = ""  # Clear the user id after submission

# --- Main App ---
# st.set_page_config(layout="wide")
st.title("⚡  TL;DR")

# Add a user entry grid in the side bar
user_id_entry()

# Add a URL entry field
url_label_css = """<style>
    .stTextInput>label:before { content: ""; font-size: 20px;}
    .stTextInput>label>div { font-size: 20px; }
    .stTextInput>div>div>input  {color: #999999; opacity: 0.8; }
    </style>"""
st.markdown(url_label_css, unsafe_allow_html=True)
url_input = st.text_input("🔗 URL", "https://example.com/")

# Add a slider to set the number of bullet points
slider_label_css = "<style>.stSlider>label>div { font-size: 20px; }</style>"
st.markdown(slider_label_css, unsafe_allow_html=True)
n_bullet_points = st.slider('Nr. of bullet points', 1, 5, 3)

# Display the bullet points
if st.button("⏩ Get the TL;DR") and st.session_state.get("user_status") == "OK":
    # Get the bullet points
    texts = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse 
        pharetra tortor non lobortis vulputate. Maecenas a tempus ipsum, ut 
        sodales enim. Etiam id tincidunt odio. Nunc ultrices commodo ipsum nec 
        blandit. Quisque vitae dapibus lacus. Proin interdum aliquet arcu. 
        Sed quam magna, pretium ac felis vel, scelerisque maximus ante.
        """
    texts_to_display = []
    for text in texts.split("."):
        texts_to_display.append("• "+text.strip()+".")
    
    # Display the bullet points in a text area
    text_area_content = "\n".join(texts_to_display)
    st.text_area(" ", value=text_area_content, height=n_bullet_points *100)