import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/WhatsApp Image 2024-04-28 at 12.13.17_86c31cd8.jpg")
img_lottie_animation = Image.open("images/Screenshot 2024-04-28 120214.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am krishna :wave:")
    st.title("An ML Engineer From Chennai")
    st.write(
        "Passionate Junior ML Engineer at SRM Valliammai Engineering College | Versatile developer excelling in hardware, software, and web solutions."
    )
    st.write("[Learn More >](https://www.linkedin.com/in/krishnarv07/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            My name is Krishna, and I'm from Chennai. I recently graduated with a B.Tech in Information Technology from SRM Valliammai Engineering College. Throughout my academic journey, I've developed a strong foundation in various IT concepts, including programming languages like cloud computing, Python, and ML.

Beyond academics, I've actively participated in extracurricular activities such as coding competitions and tech workshops, which have honed my problem-solving and teamwork skills. Additionally, I've completed internships where I've had the opportunity to apply my theoretical knowledge to real-world projects.

          - Completed a 12-week course in Cloud Computing through NPTEL.
    - Successfully completed a 3-month project in Machine Learning.
    - Completed a Python course on Udemy.
            
            """
        )
        st.write("[Instagram >](https://www.instagram.com/krizs.54321?igsh=eGEwZ21pcWM0Z2pn)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("EFFICIENT CNN-BASED FRAMEWORK FOR FRUITS & VEGETABLES RECOGNITION")
        st.write(
            """
           An efficient CNN-based framework for fruits and vegetables recognition is
        designed with several key objectives in mind it includes are high accuracy, fast
        processing, robustness, scalability, low resource consumption, generalization,
        interpretability, transfer learning capabilities, integration, user-friendly interface.
            """
        )
        st.markdown("[GetHub link...](https://github.com/krishnarv07/Fruit_veg_webapp.git)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("TEXT TO BRAILLE CONVERTING COMMUNICATION DEVICE FOR THE VISUAL AND HEARING IMPAIRED PERSONS")
        st.write(
            """
            The primary goal of this project is to provide a comprehensive solution addressing various communication challenges faced by visually impaired individuals. Notably, India currently has the largest population of blind people in the world.
            """
        )
        st.markdown("[GetHUb link](https://github.com/krishnarv07/braille-system.git)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/r.v.krishna2k4@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
