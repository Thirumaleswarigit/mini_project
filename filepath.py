import streamlit as st
tab1,tab2,tab3=st.tabs(["Home","contact","settings"])

st.title("Images")

col1, col2, col3 = st.columns(3)


with col1:
    with st.popover("Info1"):
        
        c1, c2 = st.columns(2)
        with c1:
            st.use_container_width=True,
            st.image(
                "https://tse2.mm.bing.net/th/id/OIP.eqjWHgIQbpOMrjYF9D6xiwHaE7?pid=Api&P=0&h=180",
                caption="Cat",
                #use_container_width=True,
            )
        with c2:
            st.use_container_width=True,
            st.image(
                "https://tse2.mm.bing.net/th/id/OIP.3ASJSRy03PAtNYOTM-RQwgHaFj?pid=Api&P=0&h=180",
                caption="Cats",
                #use_container_width=True,
            )
with col2:
    with st.popover("Info2"):
        
        c1, c2 = st.columns(2)
        with c1:
            st.use_container_width=True,
            st.image(
                "https://tse2.mm.bing.net/th/id/OIP.HkoEj5uMTaX2FGlUUuHUmwHaEy?pid=Api&P=0&h=180",
                caption="Dog",
                #use_container_width=True,
            )
        with c2:
            st.use_container_width=True,
            st.image(
                "https://tse3.mm.bing.net/th/id/OIP.YfrOQrCNbEIxTLv41GxELQHaEL?pid=Api&P=0&h=180",
                caption="Dogs",
                #use_container_width=True,
            )

with col3:
    with st.popover("Info3"):
       
        c1, c2 = st.columns(2)
        with c1:
            st.use_container_width=True
            st.image(
                "https://tse1.mm.bing.net/th/id/OIP.Rr-dqE4JjaQ2VFN7P4JqswHaEo?pid=Api&P=0&h=180",
                caption="Peacock",
                #use_container_width=True,
            )
        with c2:
            st.use_container_width=True,
            st.image(
                "https://tse4.mm.bing.net/th/id/OIP.XFC4Dh-I9uJmYES9ecd6XQHaEZ?pid=Api&P=0&h=180",
                caption="Duckling",
                #use_container_width=True,
            )

st.divider()

st.sidebar.title("Select Age Category")


option = st.sidebar.radio(
    "Choose one:",
    [
        "Select",
        "Category A (Age 0-25)",
        "Category B (Age 26-50)",
        "Category C (Age 51-75)",
        "Category D (Age 76-100)",
    ]
)

projects=st.sidebar.selectbox("choose projects",["select","project1","project2","project3","project4"])
data = [
    # 1–25
    {"name": "Aarav", "age": 18, "gender": "Male", "age_group": "1-25"},
    {"name": "Priya", "age": 22, "gender": "Female", "age_group": "1-25"},
    {"name": "Rahul", "age": 24, "gender": "Male", "age_group": "1-25"},
    {"name": "Sneha", "age": 19, "gender": "Female", "age_group": "1-25"},
    {"name": "Kiran", "age": 25, "gender": "Male", "age_group": "1-25"},

    # 26–50
    {"name": "Vikram", "age": 30, "gender": "Male", "age_group": "26-50"},
    {"name": "Meera", "age": 35, "gender": "Female", "age_group": "26-50"},
    {"name": "Raj", "age": 40, "gender": "Male", "age_group": "26-50"},
    {"name": "Pooja", "age": 45, "gender": "Female", "age_group": "26-50"},
    {"name": "Amit", "age": 50, "gender": "Male", "age_group": "26-50"},

    # 51–75
    {"name": "Karthik", "age": 55, "gender": "Male", "age_group": "51-75"},
    {"name": "Anjali", "age": 60, "gender": "Female", "age_group": "51-75"},
    {"name": "Rajesh", "age": 65, "gender": "Male", "age_group": "51-75"},
    {"name": "Lakshmi", "age": 70, "gender": "Female", "age_group": "51-75"},
    {"name": "Sundar", "age": 75, "gender": "Male", "age_group": "51-75"},

    # 76–100
    {"name": "Suresh", "age": 80, "gender": "Male", "age_group": "76-100"},
    {"name": "Kamala", "age": 85, "gender": "Female", "age_group": "76-100"},
    {"name": "Mohan", "age": 90, "gender": "Male", "age_group": "76-100"},
    {"name": "Leela", "age": 95, "gender": "Female", "age_group": "76-100"},
    {"name": "Raman", "age": 100, "gender": "Male", "age_group": "76-100"},
]
# --- FILTER FUNCTION ---
def filter_data(min_age, max_age):
    result = []
    for person in data:
        if person["age"] >= min_age and person["age"] <= max_age:
            result.append(person)
    return result

# --- DISPLAY BASED ON SELECTION ---
if option == "Category A (Age 0-25)":
    st.subheader("👶 Category A: Age 0–25")
    st.table(filter_data(0, 25))

elif option == "Category B (Age 26-50)":
    st.subheader("🧑 Category B: Age 26–50")
    st.table(filter_data(26, 50))

elif option == "Category C (Age 51-75)":
    st.subheader("👵 Category C: Age 51–75")
    st.table(filter_data(51, 75))

elif option == "Category D (Age 76-100)":
    st.subheader("🎂 Category D: Age 76–100")
    st.table(filter_data(76, 100))

if projects=="project1":
    st.title("Weather Prediction ")
    st.write('''
                **Description:**
                The Smart Weather App provides real-time weather updates based on city name.  
                It uses the OpenWeather API to show temperature, humidity, and predictions 
                with personalized suggestions.''')
    st.write("https://weatherprediction-8waijgitrzy9mh8s6lh5s5.streamlit.app/")
elif projects=="project2":
    st.title("Random Code Genarator")
    st.write('''
              **Description:**
              Built using Streamlit, the app generates two random lines of Python code and
              displays them instantly on the screen. It’s useful for quick learning, debugging
              practice, or even coding inspiration. With a clean interface and real-time 
              generation, it makes exploring programming concepts both engaging and effortless.''')
    st.write("https://randomcodegen-uvyuyudbagwgk6ktewhuuf.streamlit.app/")
elif projects=="project3":
    st.title("Students Register Form")
    st.write('''
             **Description:**
               I created a Student Registration Form using the Streamlit module that collects 
               details like First Name, Last Name, Email, and Phone Number through a simple interface. 
               After submission, the entered information is displayed in a table format, making it 
               easy to view and verify the student details.
             ''')
    st.write("https://studentsdetails-htegejejgsh6w5ygxkstmd.streamlit.app/")     

elif projects=="project4":
    st.write("Introduction about Modules")
    st.write('''
             **Description**
               The JSON module in Python is used to handle data in JSON format, allowing easy 
               conversion between Python objects and JSON strings. The Requests module helps 
               in sending HTTP requests to web servers, making it simple to fetch, send, or 
               interact with APIs for real-time data exchange.
             ''')
    st.write("https://new-registerapp-bkdu4hbc4ewfkqepjv3gnm.streamlit.app/")
