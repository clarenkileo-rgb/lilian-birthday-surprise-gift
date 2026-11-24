import streamlit as st
from pathlib import Path
import base64

# ============================================================
# LILIAN'S BIRTHDAY EXPERIENCE
# A long-form, elegant, K-drama-inspired birthday website.
# Run with: python -m streamlit run lilian_luxury_birthday.py
# ============================================================

st.set_page_config(
    page_title="A Day Made for Lilian",
    page_icon="🎀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------- DESIGN ----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --wine: #6e3047;
    --rose: #b97889;
    --gold: #c9a66b;
    --cream: #fffaf5;
    --ink: #34252b;
}
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    color: var(--ink);
}
.stApp {
    background:
      radial-gradient(circle at 8% 8%, rgba(226,188,190,.22), transparent 28%),
      radial-gradient(circle at 92% 18%, rgba(218,193,151,.20), transparent 25%),
      linear-gradient(135deg, #fffaf7 0%, #f9eff0 48%, #fffaf3 100%);
}
.block-container { max-width: 1120px; padding-top: 2rem; padding-bottom: 4rem; }
h1, h2, h3, .serif {
    font-family: 'Cormorant Garamond', serif !important;
    color: #633246;
}
.hero {
    padding: 4.2rem 2rem 3.7rem 2rem;
    border: 1px solid rgba(190,151,119,.38);
    border-radius: 28px;
    text-align: center;
    background: linear-gradient(135deg, rgba(255,255,255,.92), rgba(250,232,232,.82));
    box-shadow: 0 18px 55px rgba(100,49,66,.09);
    position: relative;
    overflow: hidden;
}
.eyebrow {
    letter-spacing: .34em;
    text-transform: uppercase;
    color: #a17b68;
    font-size: .72rem;
    font-weight: 600;
}
.hero h1 {
    font-size: clamp(3rem, 7vw, 5.6rem);
    line-height: .98;
    margin: .8rem 0 1rem 0;
}
.hero p { max-width: 680px; margin: auto; line-height: 1.9; color: #705b61; }
.gold-line { width: 82px; height: 1px; background: #c9a66b; margin: 1.4rem auto; }
.panel {
    background: rgba(255,255,255,.78);
    border: 1px solid rgba(201,166,107,.32);
    border-radius: 22px;
    padding: 1.5rem 1.6rem;
    box-shadow: 0 12px 35px rgba(87,48,61,.055);
    margin: .65rem 0 1rem 0;
}
.letter {
    background: linear-gradient(145deg, #fffdfb, #fff6f2);
    border-left: 3px solid #c9a66b;
    border-radius: 5px 18px 18px 5px;
    padding: 1.7rem 1.8rem;
    line-height: 2;
    color: #604c52;
    box-shadow: 0 10px 30px rgba(80,45,58,.06);
}
.small-cap {
    letter-spacing: .2em; text-transform: uppercase;
    color: #a17b68; font-size: .7rem; font-weight: 600;
}
div.stButton > button {
    border-radius: 999px;
    border: 1px solid #b98b77;
    color: #67374a;
    background: linear-gradient(120deg, #fff, #f8e9e8);
    padding: .55rem 1.25rem;
    transition: all .2s ease;
}
div.stButton > button:hover {
    border-color: #9c6375; color: #fff;
    background: linear-gradient(120deg, #9c6375, #704054);
}
div[data-testid="stTabs"] button {
    font-weight: 600;
    color: #805466;
}
hr { border-color: rgba(201,166,107,.35); }
.footer {
    text-align:center; color:#9a7c7e; font-size:.82rem;
    padding: 2.5rem 0 .5rem; letter-spacing:.06em;
}
blockquote {
    border-left: 2px solid #c9a66b !important;
    color: #765964 !important;
}

.party-strip {
    display:flex; justify-content:center; align-items:center; gap:1.2rem;
    padding:1.2rem .5rem; margin:1rem 0 1.5rem;
    border:1px solid rgba(201,166,107,.32); border-radius:18px;
    background:rgba(255,255,255,.58); overflow:hidden;
}
.party-balloon { font-size:2rem; display:inline-block; animation: floaty 3s ease-in-out infinite; }
.party-balloon:nth-child(2) { animation-delay:.35s; }
.party-balloon:nth-child(3) { animation-delay:.7s; }
.party-balloon:nth-child(4) { animation-delay:1.05s; }
.party-balloon:nth-child(5) { animation-delay:1.4s; }
@keyframes floaty {
    0%,100% { transform:translateY(5px) rotate(-5deg); }
    50% { transform:translateY(-12px) rotate(5deg); }
}

</style>
""", unsafe_allow_html=True)

# ------------------------- SESSION STATE ---------------------
if "opened_gifts" not in st.session_state:
    st.session_state.opened_gifts = set()
if "chosen_wish" not in st.session_state:
    st.session_state.chosen_wish = "A year filled with beautiful opportunities"
if "show_final" not in st.session_state:
    st.session_state.show_final = False

# ------------------------- HERO ------------------------------
st.markdown("""
<div class="hero">
  <div class="eyebrow">A little celebration • A beautiful new chapter</div>
  <h1>For Lilian</h1>
  <div class="gold-line"></div>
  <p>
    Today deserves more than an ordinary greeting. It deserves a pause,
    a little sparkle, a few thoughtful words, and a reminder that your
    presence makes the world around you a little brighter.
  </p>
  <p style="margin-top:1.35rem; font-family:'Cormorant Garamond',serif;
            font-size:1.35rem; color:#956b72;">
    A birthday experience, created especially for you.
  </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="party-strip">
  <span class="party-balloon">🎈</span>
  <span class="party-balloon">🎉</span>
  <span class="party-balloon">🎈</span>
  <span class="party-balloon">🥳</span>
  <span class="party-balloon">🎈</span>
</div>
""", unsafe_allow_html=True)

party_col1, party_col2, party_col3 = st.columns([1, 1.4, 1])
with party_col2:
    if st.button("🎊 LET THE BIRTHDAY PARTY BEGIN! 🎊", use_container_width=True):
        st.balloons()
        st.toast("Surprise, Lilian! Let the celebration begin! 🎉")
        st.success("🎈🎈🎈 HAPPY BIRTHDAY, LILIAN! 🎈🎈🎈")

st.write("")
left, right = st.columns([1.05, 1.2], gap="large")
with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="small-cap">The birthday portrait</div>', unsafe_allow_html=True)
    portrait_path = Path("lilian_birthday_portrait.png")
    if portrait_path.exists():
        st.image(str(portrait_path), use_container_width=True)
        st.caption("A decorative birthday portrait for this special page.")
    else:
        st.markdown("""
        <div style="height:330px;border-radius:18px;background:
        linear-gradient(145deg,#f4dfe0,#fff8ef);display:flex;
        align-items:center;justify-content:center;text-align:center;
        color:#8a5b6b;font-family:'Cormorant Garamond',serif;font-size:2rem;">
        A little portrait space<br>for a lovely celebration ✨
        </div>""", unsafe_allow_html=True)
        uploaded_portrait = st.file_uploader(
            "Add a portrait or birthday picture (optional)",
            type=["png", "jpg", "jpeg"],
            key="portrait_upload"
        )
        if uploaded_portrait:
            st.image(uploaded_portrait, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="small-cap">A note for your day</div>', unsafe_allow_html=True)
    st.markdown("""
    <h2 style="font-size:2.5rem;margin:.35rem 0 1rem 0;">Dear Lilian,</h2>
    <div class="letter">
      Happy Birthday! 🎂<br><br>
      I hope today brings you genuine happiness, peaceful moments,
      unexpected reasons to smile, and memories that you will look back
      on with warmth. May the year ahead introduce you to wonderful
      opportunities, kind people, exciting experiences, and goals that
      make you proud of how far you have come.<br><br>
      May you continue to discover new strengths in yourself, enjoy the
      little things, and make room for everything that inspires you.
      You deserve a day that feels special, a year that feels promising,
      and many moments that remind you how much good life can hold.<br><br>
      Enjoy your celebration, take lots of pictures, eat something
      delicious, laugh freely, and make this day your own.<br><br>
      <strong>Wishing you a beautiful birthday and an even more beautiful year ahead.</strong>
    </div>
    <p style="text-align:right;color:#a17b68;font-family:'Cormorant Garamond',serif;
    font-size:1.3rem;margin-top:1rem;">With warm wishes ✨</p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("<h2 style='text-align:center;font-size:2.8rem;'>Your Birthday Experience</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#8a7077;'>Take your time. There are little surprises waiting in each chapter.</p>", unsafe_allow_html=True)

tabs = st.tabs([
    "01 · Birthday mood",
    "02 · Open a surprise",
    "03 · Your wishes",
    "04 · A little quiz",
    "05 · Memories",
    "06 · Party poppers",
    "07 · Final chapter"
])

# ------------------------- TAB 1 -----------------------------
with tabs[0]:
    st.markdown("<h2 style='font-size:2.4rem;'>Set the mood for today</h2>", unsafe_allow_html=True)
    st.write("Every birthday has its own atmosphere. Choose the one that feels most like your celebration.")
    mood = st.radio(
        "What kind of birthday energy are we choosing?",
        ["Soft and elegant 🌷", "Golden and glamorous ✨", "Fun and full of laughter 🎉", "Calm and peaceful 🕊️"],
        horizontal=False
    )
    mood_messages = {
        "Soft and elegant 🌷": "A gentle day, lovely details, beautiful pictures, and moments worth keeping.",
        "Golden and glamorous ✨": "A little sparkle, a confident entrance, and a day that feels like a scene from a favourite drama.",
        "Fun and full of laughter 🎉": "Good music, funny moments, delicious treats, and laughter that lasts long after today.",
        "Calm and peaceful 🕊️": "A slower day, a grateful heart, and space to enjoy everything that matters."
    }
    st.markdown(f"<div class='panel'><div class='small-cap'>Your birthday atmosphere</div><h3 style='font-size:2rem;'>{mood}</h3><p>{mood_messages[mood]}</p></div>", unsafe_allow_html=True)

    st.markdown("#### Add a song to the celebration")
    st.write("Choose an audio file already saved on your device. You can use an MP3, WAV, or OGG file.")
    music = st.file_uploader("Upload a birthday song or favourite track", type=["mp3", "wav", "ogg"], key="music_upload")
    if music:
        st.audio(music)
        st.caption("Press play whenever you are ready. Music will not start automatically.")
    else:
        st.info("No song selected yet. You can still enjoy the birthday page without music.")

# ------------------------- TAB 2 -----------------------------
with tabs[1]:
    st.markdown("<h2 style='font-size:2.4rem;'>The little surprise collection</h2>", unsafe_allow_html=True)
    st.write("Six envelopes, six thoughtful messages. Choose any envelope to reveal what is inside.")
    gifts = [
        ("The Golden Envelope", "May new doors open for you this year. May you have the courage to walk through them and the patience to enjoy the journey."),
        ("The Smile Box", "May you find reasons to laugh often, people who bring out your happiest side, and memories that make ordinary days feel special."),
        ("The Opportunity Card", "May your talents find room to grow. May your effort be recognised, and may exciting opportunities meet your preparation."),
        ("The Peaceful Moment", "May you have peaceful mornings, restful evenings, and the confidence to take life one step at a time."),
        ("The Adventure Note", "May this year bring new places, new experiences, new ideas, and stories you will be happy to tell."),
        ("The Confidence Letter", "May you keep believing in your ability to learn, improve, begin again, and become everything you are working towards.")
    ]
    cols = st.columns(2)
    for i, (gift_title, gift_message) in enumerate(gifts):
        with cols[i % 2]:
            st.markdown("<div class='panel'>", unsafe_allow_html=True)
            st.markdown(f"<div class='small-cap'>Envelope {i+1:02d}</div><h3 style='font-size:1.8rem;'>{gift_title}</h3>", unsafe_allow_html=True)
            if st.button("Open this surprise", key=f"gift_{i}"):
                st.session_state.opened_gifts.add(i)
            if i in st.session_state.opened_gifts:
                st.success(gift_message)
            else:
                st.caption("A message is waiting inside.")
            st.markdown("</div>", unsafe_allow_html=True)
    st.caption(f"You have opened {len(st.session_state.opened_gifts)} of 6 surprises.")

# ------------------------- TAB 3 -----------------------------
with tabs[2]:
    st.markdown("<h2 style='font-size:2.4rem;'>A wish for the year ahead</h2>", unsafe_allow_html=True)
    st.write("Choose the wish you would most like to carry into your new year.")
    wishes = [
        "A year filled with beautiful opportunities",
        "A year of confidence, growth, and achievement",
        "A year of laughter, friendship, and lovely memories",
        "A year of peace, good health, and happiness",
        "A year of exciting discoveries and new experiences",
        "A year in which dreams become meaningful plans"
    ]
    st.session_state.chosen_wish = st.selectbox(
        "Choose your birthday wish",
        wishes,
        index=wishes.index(st.session_state.chosen_wish)
    )
    st.markdown(f"""
    <div class="panel" style="text-align:center;padding:2rem;">
      <div class="small-cap">Your chosen wish</div>
      <h2 style="font-size:2.3rem;">{st.session_state.chosen_wish}</h2>
      <p style="color:#806a70;">May this wish become part of a year you will always be glad you lived.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("And one more thing: you do not have to have everything figured out today. There is beauty in learning, growing, and discovering what comes next.")

# ------------------------- TAB 4 -----------------------------
with tabs[3]:
    st.markdown("<h2 style='font-size:2.4rem;'>The birthday mini quiz</h2>", unsafe_allow_html=True)
    st.write("A small, just-for-fun quiz. No pressure to get everything right!")
    q1 = st.radio("Which birthday treat sounds best?", ["A beautiful cake 🍰", "A lovely meal 🍓", "A fun day out 🎡", "A quiet, cosy celebration 🕯️"], key="q1")
    q2 = st.radio("Choose a birthday colour mood:", ["Champagne gold", "Blush pink", "Pearl white", "Midnight blue"], key="q2")
    q3 = st.radio("What would make the year memorable?", ["Learning something new", "Visiting somewhere new", "Reaching an important goal", "Making wonderful memories"], key="q3")
    if st.button("Reveal my birthday style"):
        st.balloons()
        st.success(f"Your birthday style is a lovely mix of {q1.lower()}, {q2.lower()}, and a year focused on: {q3.lower()}. Make it a year to remember!")

# ------------------------- TAB 5 -----------------------------
with tabs[4]:
    st.markdown("<h2 style='font-size:2.4rem;'>A little memory gallery</h2>", unsafe_allow_html=True)
    st.write("You can add a few pictures to make this page even more personal. These pictures are only displayed during the current app session.")
    photos = st.file_uploader(
        "Choose photos for the gallery",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True,
        key="gallery_upload"
    )
    if photos:
        for start in range(0, len(photos), 3):
            photo_cols = st.columns(3)
            for col, photo in zip(photo_cols, photos[start:start+3]):
                with col:
                    st.image(photo, use_container_width=True)
        st.caption("A collection of little moments worth remembering.")
    else:
        st.markdown("""
        <div class="panel" style="text-align:center;padding:2.5rem;">
          <div style="font-size:2.8rem;">📷 ✨ 🌷</div>
          <h3 style="font-size:2rem;">The gallery is ready for memories</h3>
          <p>Choose a few favourite pictures above whenever you wish.</p>
        </div>
        """, unsafe_allow_html=True)

# ------------------------- TAB 6 -----------------------------
with tabs[5]:

    st.markdown("""
    <div class='panel'>
      <div class='small-cap'>A spoken birthday greeting</div>
      <h3 style='font-size:2rem;'>Someone has a message for you…</h3>
      <p>Press play to hear a longer birthday message prepared especially for you.</p>
      <p style="text-align:right;color:#a17b68;font-family:'Cormorant Garamond',serif;font-size:1.35rem;">
        A Special Birthday Celebration from Claren!
      </p>
    </div>
    """, unsafe_allow_html=True)
    import streamlit.components.v1 as components
    components.html("""
    <div style="font-family:Arial,sans-serif;text-align:center;padding:12px;background:#fff8f5;border:1px solid #e6d3cb;border-radius:16px;">
      <button id="sayBirthday" style="background:linear-gradient(120deg,#9c6375,#704054);color:white;border:0;border-radius:28px;padding:14px 24px;font-size:15px;cursor:pointer;">
        🔊 PLAY THE FULL BIRTHDAY GREETING
      </button>
      <button id="stopBirthday" style="background:#fff;color:#704054;border:1px solid #b98b77;border-radius:28px;padding:12px 20px;font-size:14px;cursor:pointer;margin-left:8px;">
        STOP
      </button>
      <p id="voiceStatus" style="color:#795d67;font-size:12px;margin-top:10px;">Turn your volume up, then press play.</p>
    </div>
    <script>
      const button = document.getElementById("sayBirthday");
      const stopButton = document.getElementById("stopBirthday");
      const status = document.getElementById("voiceStatus");

      const fullMessage = `Hello, Lilian! Happy birthday, and welcome to your very special celebration.

      Today is a chance to pause, enjoy the moment, and celebrate another year of life, experiences, lessons, and new possibilities. This little birthday page has been prepared to bring a little extra happiness to your day. There are messages to discover, surprises to open, memories to enjoy, and a few cheerful moments waiting for you.

      First, take a deep breath, relax, and allow yourself to enjoy your day. You do not need to rush through anything. Explore each section, read the messages, choose your birthday wishes, and have fun with the surprises. Every little detail is here to make your celebration feel a little more special.

      May the year ahead bring you many reasons to smile. May you discover exciting opportunities, make progress towards the goals that matter to you, and find the confidence to try new things. May your hard work bring satisfying results, and may every challenge teach you something valuable.

      May you enjoy good health, peaceful days, genuine friendships, laughter, and moments that become beautiful memories. May you meet kind people, visit interesting places, learn new things, and experience opportunities that help you grow. When things are busy, may you also find time to rest, appreciate how far you have come, and enjoy the simple things around you.

      Birthdays are not only about cake, decorations, gifts, and photographs. They are also about new beginnings. A new year gives you another opportunity to explore your interests, make plans, discover your strengths, and create experiences that you will remember with happiness.

      So, Lilian, enjoy the music, enjoy the balloons, open the little surprises, and let yourself have a lovely celebration. Take some pictures, have your favourite treats, laugh as much as you can, and make today a day worth remembering.

      Once again, happy birthday, Lilian! May your next chapter be full of bright beginnings, meaningful achievements, wonderful discoveries, and many beautiful moments. Have a lovely celebration and an amazing year ahead!`;

      function speakInParts(text) {
        const chunks = text.match(/[^.!?]+[.!?]+|[^.!?]+$/g) || [text];
        let index = 0;
        function speakNext() {
          if (index >= chunks.length) {
            status.textContent = "The birthday message has finished. Have a wonderful day, Lilian!";
            return;
          }
          const part = new SpeechSynthesisUtterance(chunks[index].trim());
          part.lang = "en-US";
          part.rate = 0.9;
          part.pitch = 1.06;
          const voices = window.speechSynthesis.getVoices();
          const englishVoice = voices.find(v => v.lang && v.lang.toLowerCase().startsWith("en"));
          if (englishVoice) part.voice = englishVoice;
          part.onend = () => {
            index += 1;
            speakNext();
          };
          part.onerror = () => {
            status.textContent = "Audio could not finish. Please press play to try again.";
          };
          window.speechSynthesis.speak(part);
        }
        speakNext();
      }

      button.addEventListener("click", () => {
        if (!("speechSynthesis" in window)) {
          status.textContent = "This browser does not support spoken audio. Try Chrome or Edge.";
          return;
        }
        window.speechSynthesis.cancel();
        status.textContent = "Your full birthday message is playing…";
        speakInParts(fullMessage);
      });

      stopButton.addEventListener("click", () => {
        if ("speechSynthesis" in window) window.speechSynthesis.cancel();
        status.textContent = "The birthday greeting has been stopped.";
      });
    </script>
    """, height=145)
    st.caption("The spoken voice comes from the browser/device. The exact voice may differ between phones and computers. The name credit above is written on the page and is not spoken aloud.")
    st.markdown("<h2 style='font-size:2.5rem;'>🎉 It's party time, Lilian!</h2>", unsafe_allow_html=True)
    st.write("A birthday deserves a little extra sparkle. Choose a surprise below and let the celebration begin.")
    party_left, party_right = st.columns(2)
    with party_left:
        st.markdown("<div class='panel' style='text-align:center;'><div style='font-size:3.4rem;'>🎊</div><h3 style='font-size:1.9rem;'>The confetti moment</h3><p>Ready for a little burst of celebration?</p></div>", unsafe_allow_html=True)
        if st.button("POP THE PARTY CONFETTI!", key="confetti_button", use_container_width=True):
            st.balloons()
            st.toast("POP! A little birthday magic for you! 🎊")
            st.success("🎉🎉🎉 Sending you a shower of birthday wishes! 🎉🎉🎉")
    with party_right:
        st.markdown("<div class='panel' style='text-align:center;'><div style='font-size:3.4rem;'>🎈</div><h3 style='font-size:1.9rem;'>The balloon celebration</h3><p>Let's fill the moment with birthday balloons.</p></div>", unsafe_allow_html=True)
        if st.button("RELEASE THE BALLOONS!", key="balloon_button", use_container_width=True):
            st.balloons()
            st.success("🎈 Up, up, and away! May your year rise with happiness and possibility.")
    st.markdown("<div class='panel' style='text-align:center;'><div class='small-cap'>A birthday cheer</div><h2 style='font-size:2.6rem;'>Hip hip hooray!</h2><p style='font-size:1.25rem;'>🥳 🎂 🎁 🎀 🎉 🎈</p><p>May today be full of good music, lovely surprises, sweet treats, and happy memories.</p></div>", unsafe_allow_html=True)
    if st.button("ONE MORE BIG SURPRISE ✨", key="big_surprise", use_container_width=True):
        st.balloons()
        st.toast("You deserve a wonderful celebration, Lilian! 💗")
        st.markdown("<h2 style='text-align:center;'>SURPRISE!!! 🎉 HAPPY BIRTHDAY!!! 🎉</h2>", unsafe_allow_html=True)

with tabs[6]:
    st.markdown("<h2 style='font-size:2.4rem;'>The final chapter</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="letter">
      Some days pass quickly, but a thoughtful message can make a day feel
      a little more memorable. So before this birthday page comes to an end,
      here is one last wish for you:<br><br>
      May the coming year be kind to you. May you meet challenges with
      courage, celebrate progress no matter how small, and never forget
      that every new chapter gives you another chance to create something
      wonderful. May your plans grow, your confidence deepen, and your
      happiest moments arrive in ways you never expected.<br><br>
      Keep making room for joy. Keep discovering what you love. Keep
      becoming a person you are proud of.
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    if st.button("Open the final birthday wish"):
        st.session_state.show_final = True
        st.balloons()
    if st.session_state.show_final:
        st.markdown("""
        <div class="hero" style="padding:2.5rem 1.5rem;">
          <div class="eyebrow">One last wish</div>
          <h1 style="font-size:3.5rem;">Happy Birthday, Lilian!</h1>
          <div class="gold-line"></div>
          <p>May your next chapter be filled with bright beginnings, meaningful moments, and beautiful surprises.</p>
          <p style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;margin-top:1rem;">Enjoy every moment of your special day. 🎂</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
  MADE WITH THOUGHTFUL WISHES · A LITTLE BIRTHDAY PAGE FOR LILIAN
</div>
""", unsafe_allow_html=True)
