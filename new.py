import streamlit as st
import datetime
import time

st.title("Surprise Surprise⁉️⁉️")
st.divider()
st.markdown(
    """ 
    I cant wait for you to see this!! 

    There's :red[SO MUCH] you HAVE TO SEE!!!
    """
)

#---------- STYLING ----------
st.markdown("""
 <style> 

/* Countdown Clock */
.clock-container {
    text-align: center;
    background-color: black;
    padding: 20px 30px;
    border-radius: 20px;
    width: 450px;
    margin: 40px auto;
    box-shadow: 0 0 25px #FF3366;
}
.clock-days {
    font-size: 55px;
    font-family: 'Courier New', monospace;
    color: white;
    margin-bottom: 15px;
}
.clock-time {
    font-size: 75px;
    font-family: 'Courier New', monospace;
    color: #FF3366;
    text-shadow: 0 0 20px #FF3366, 0 0 40px #FF0066;
}

/* Unlocked Page */
.unlocked {
    text-align: center;
    padding: 40px;
    background: linear-gradient(135deg, #ff99cc, #ff3366);
    border-radius: 25px;
    margin-top: 40px;
    color: white;
    box-shadow: 0 0 40px #FF3366;
}
.unlocked h1 {
    font-size: 50px;
    margin-bottom: 20px;
}
.unlocked p {
    font-size: 22px;
}
.emoji {
    width: 40px;
    height: 40px;
    vertical-align: middle;
}
</style>
""", unsafe_allow_html=True)

# --------- COUNTDOWN ---------
target_date = datetime.datetime(2025, 10, 2, 0, 0, 0)
now = datetime.datetime.now()
diff = target_date - now

if diff.total_seconds() <= 0:
    st.markdown(
        """
        <h2 style='text-align:center; color:green;'>
        <img class='emoji' src='https://em-content.zobj.net/thumbs/160/apple/354/party-popper_1f389.png'>
        The day has arrived! Happy 2nd October 💝
        <img class='emoji' src='https://em-content.zobj.net/thumbs/160/apple/354/birthday-cake_1f382.png'>
        </h2>
        """,
        unsafe_allow_html=True
    )
else:
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    st.markdown(
        f"""
        <div class="clock-container">
            <div class="clock-days">{days} days</div>
            <div class="clock-time">{hours:02d}:{minutes:02d}:{seconds:02d}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


# Password section
st.markdown("<h3 style='text-align:center;'>Enter Password</h3>", unsafe_allow_html=True)
st.write("")

password = st.text_input("", type="password", placeholder="Enter password here...")

if password:
    if password == "oct2special":  # change password
        st.success("Unlocked! 🎉 Here’s your surprise 💝")
        st.markdown("<h2 style='text-align:center; color:#FF1493;'>Happy Birthday Love! 🎂💌</h2>", unsafe_allow_html=True)
    else:
        st.markdown(
            """
            <div style="color: red; border: 1px solid red; 
            padding: 12px; border-radius: 8px; text-align:center; margin-top:15px;">
                🚫 Wrong password! Only my gf gets access on 2/10 😉
            </div>
            """,
            unsafe_allow_html=True

        )

