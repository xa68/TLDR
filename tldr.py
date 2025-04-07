import streamlit as st

def user_id_entry():
    """Creates a user id entry grid in the sidebar."""

    st.sidebar.subheader('Enter user id:')

    # Initialize user id in session state if it doesn't exist
    if "user_id" not in st.session_state:
        st.session_state.user_id = ""

    st.session_state.user_id = st.sidebar.text_input("🆔 ", "your_id")  

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


from google import genai

client = genai.Client(api_key=st.secrets["api_key"])

def formatted_response(response):
    return {
        "text": response.text,
        "n_input_tokens": response.usage_metadata.prompt_token_count,
        "n_output_tokens": response.usage_metadata.candidates_token_count,
    }


def bullet_points(url, n_bullet_points):
    prompt = f"""give me the tl;dr of the article at url 
    {url} 
    in {n_bullet_points} bullet points. 
    Each bullet point should have a title (maximum 5 words) 
    and a short sentence to describe the content."""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return formatted_response(response)
    

def display_responses(responses):
    for response in reversed(responses):
        st.markdown("---")
        st.markdown(response['text'])
        st.markdown(f"""<p class='small-gray'>Input tokens: {response['n_input_tokens']}
                <br>
                    Output tokens: {response['n_output_tokens']}
            </p>""", unsafe_allow_html=True)

    
# --- Main App ---
# st.set_page_config(layout="wide")
st.title("TL;DR")

# Add a user entry grid in the side bar
user_id_entry()

# Create a list of llm responses as a state variable
if "llm_responses" not in st.session_state:
    st.session_state.llm_responses = []

# Create a session token counter as a state variable
if "session_tokens" not in st.session_state:
    st.session_state.session_tokens = 0
    
# Add a URL entry field
url_label_css = """<style>
    .stTextInput>label:before { content: ""; font-size: 20px;}
    .stTextInput>label>div { font-size: 20px; }
    .stTextInput>div>div>input  {color: #999999; opacity: 0.7; font-size: 20px; }
    </style>"""
st.markdown(url_label_css, unsafe_allow_html=True)
url_input = st.text_input("🔗 URL", "https://example.com/")

# Add a slider to set the number of bullet points
slider_label_css = "<style>.stSlider>label>div { font-size: 20px; }</style>"
st.markdown(slider_label_css, unsafe_allow_html=True)
n_bullet_points = st.slider('Nr. of bullet points', 1, 5, 3)
hide_responses = True

# Make 2 columns, one for the Get tldr button and ome for the Get session summary button
col1, col2 = st.columns(2)
with col1:
    # Get the bullet points and append them to the list of responses
    if st.button("⏩ Get the TL;DR") and st.session_state.get("user_status") == "OK":
        bullet_points_response = bullet_points(url_input, n_bullet_points)
        st.session_state.llm_responses.append(bullet_points_response)

        # Update the session token counter
        n_input_tokens = bullet_points_response['n_input_tokens']
        n_output_tokens = bullet_points_response['n_output_tokens']
        st.session_state.session_tokens += n_input_tokens + n_output_tokens
        # display the session token counter
        token_count_css = "<style> .small-gray {font-size: 16px; color: #999999; } </style>"
        st.markdown(f"""<p class='small-gray'>Session tokens: {st.session_state.session_tokens}
                </p>""", unsafe_allow_html=True)
        hide_responses = False

with col2:
    # Get the session summary and append it to the list of responses
    if st.button("📄 Get session summary") and st.session_state.llm_responses:
        responses_concat = "\\n".join(response['text'] for response in st.session_state.llm_responses)
        summary_prompt = f"""Summarize the following text: \\n{responses_concat}"""
        summary = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=summary_prompt
        )

        st.session_state.llm_responses.append(formatted_response(summary))
        hide_responses = False
        
# display all responses
if not hide_responses:
    display_responses(st.session_state.llm_responses)
