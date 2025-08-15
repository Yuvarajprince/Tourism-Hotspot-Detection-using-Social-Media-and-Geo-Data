import streamlit as st
import pandas as pd
import pymongo
import openai
import webbrowser
from streamlit_option_menu import option_menu

# ===== MongoDB Setup =====
MONGO_URI = "mongodb://localhost:27017"
client = pymongo.MongoClient(MONGO_URI)
db = client["tourism_db"]
collection = db["places"]

# ===== Load Dataset =====
DATA_PATH = "updated_tourist_places_dataset.csv"
df = pd.read_csv(DATA_PATH)

# ===== OpenAI API Key for Chatbot =====
OPENAI_API_KEY = "your-openai-api-key"
openai.api_key = OPENAI_API_KEY

# ===== Streamlit Page Configurations =====
st.set_page_config(page_title="🌍 Tourist HotSpot Finder", layout="wide")

# ===== Custom CSS Styling =====
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background: url("https://source.unsplash.com/1600x900/?skyline,travel") no-repeat center center fixed;
        background-size: cover;
    }
    .image-container {
        position: relative;
        text-align: center;
        width: 100%;
    }
    .centered-title {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 42px;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        background: rgba(0, 0, 0, 0.5);
        padding: 10px 20px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ===== Sidebar Menu Navigation =====
with st.sidebar:
    selected_page = option_menu(
        menu_title="Tourist Explorer",
        options=["🏠 Home", "🔍 Search Places", "📌 Saved Places", "📊 Analysis", "🤖 Chatbot"],
        icons=["house", "search", "bookmark", "bar-chart", "robot"],
        menu_icon="globe",
        default_index=0
    )

# ======= Home Page =======
if selected_page == "🏠 Home":
    image_url = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"

    # Display title over image
    st.markdown(f"""
        <div class="image-container">
            <img src="{image_url}" width="100%">
            <div class="centered-title">🌍 Welcome to Tourist HotSpot Finder</div>
        </div>
    """, unsafe_allow_html=True)

    st.write("### ✈️ Explore the best travel destinations around the world.")
    st.write("🌟 Discover amazing places, plan your trips, and make your journey memorable!")


# ======= Search Places Page =======
elif selected_page == "🔍 Search Places":
    st.markdown("<h2 style='text-align: center;'>🔍 Search Tourist Places</h2>", unsafe_allow_html=True)

    country = st.selectbox("🌍 Select Country", sorted(df["Country"].unique()))
    state = st.selectbox("🏞️ Select State", sorted(df[df["Country"] == country]["State"].unique()))
    city = st.selectbox("🏙️ Select City", sorted(df[(df["Country"] == country) & (df["State"] == state)]["City"].unique()))
    category_input = st.text_input("🏝️ Enter Place Type (Optional)", "").strip()

    if st.button("🔍 Search"):
        results = df[(df["Country"].str.lower() == country.lower()) & 
                     (df["State"].str.lower() == state.lower()) & 
                     (df["City"].str.lower() == city.lower())]
        
        if category_input:
            results = results[results["Tourist Place"].str.contains(category_input, case=False)]
        
        if not results.empty:
            st.success(f"✅ Found {len(results)} places in {city}!")
            selected_place = st.selectbox("📍 Select a Place", results["Tourist Place"].tolist())

            if selected_place:
                place_details = results[results["Tourist Place"] == selected_place].iloc[0]
                st.write(f"📍 **{selected_place}**")
                st.write(f"🌟 **Rating:** {place_details['Reviews']}")
                st.write(f"⏳ **Recommended Stay:** {place_details['Recommended Stay']}")
                st.write(f"📅 **Best Time to Visit:** {place_details['Best Visiting Time']}")
                st.write(f"🏨 **Nearby Attractions:** {place_details['Nearby Attractions']}")
                st.write(f"💰 **Entry Fee:** {place_details['Entry Fee']}")
                st.write(f"👨‍👩‍👧‍👦 **Family-Friendly:** {place_details['Family-Friendly']}")
                st.write(f"🏕️ **Adventure Level:** {place_details['Adventure Level']}")
                st.write(f"♿ **Accessibility:** {place_details['Accessibility']}")

                # Save place to MongoDB
                collection.insert_one(place_details.to_dict())

                # Open Google Maps
                maps_url = place_details['Google Maps Link']
                if st.button("🗺️ View in Google Maps"):
                    webbrowser.open(maps_url)
        else:
            st.error("❌ No matching places found.")

# ======= Saved Places Page =======
elif selected_page == "📌 Saved Places":
    st.markdown("<h2 style='text-align: center;'>📌 Saved Tourist Places</h2>", unsafe_allow_html=True)

    saved_places = list(collection.find({}, {"_id": 0}))
    
    if saved_places:
        for place in saved_places:
            st.markdown(f"""
                <div style="border: 2px solid #FFA500; padding: 15px; border-radius: 10px; margin-bottom: 10px; background-color: #FFF3E0;">
                    <h4 style="color: #FF5733;">📍 {place['Tourist Place']}</h4>
                    <p><b>📍 Location:</b> {place.get('City', 'Unknown')}, {place.get('State', 'Unknown')}, {place.get('Country', 'Unknown')}</p>
                    <p><b>⭐ Reviews:</b> {place.get('Reviews', 'N/A')}</p>
                    <p><b>📜 Description:</b> {place.get('Description', 'No description available')}</p>
                    <a href="{place['Google Maps Link']}" target="_blank" style="text-decoration: none;">
                        <button style="background-color: #FFA500; color: white; padding: 10px 15px; border: none; border-radius: 5px; cursor: pointer;">
                            🗺️ View on Google Maps
                        </button>
                    </a>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.write("No saved places yet.")

# ======= Analysis Page =======
elif selected_page == "📊 Analysis":
    st.markdown("<h2 style='text-align: center;'>📊 Analysis of Tourist Places</h2>", unsafe_allow_html=True)

    st.write(f"- 🏔️ **Total Number of Tourist Places:** {len(df)}")
    st.write(f"- 🌎 **Total Number of Countries Represented:** {len(df['Country'].unique())}")
    st.write(f"- ⭐ **Average Rating of Places:** {df['Reviews'].mean():.2f}")
    
    st.write("### 🌍 Top 5 Most Popular Tourist Places")
    top_places = df.sort_values(by="Reviews", ascending=False).head(5)
    st.table(top_places[["Tourist Place", "Country", "State", "City", "Reviews"]])

# ======= Chatbot Page =======
elif selected_page == "🤖 Chatbot":
    st.markdown("<h2 style='text-align: center;'>🤖 Travel Chatbot</h2>", unsafe_allow_html=True)
    
    chatbot_responses = {
    "What are the best places to visit in Paris?": "Some of the best places to visit in Paris are the Eiffel Tower, Louvre Museum, Notre-Dame Cathedral, and the Champs-Élysées.",
    "When is the best time to visit Bali?": "The best time to visit Bali is from April to October during the dry season.",
    "What are the top adventure destinations in India?": "Some top adventure destinations in India are Ladakh for biking, Rishikesh for river rafting, Andaman for scuba diving, and Spiti Valley for trekking.",
    "Can you suggest budget-friendly travel destinations?": "Some budget-friendly travel destinations are Vietnam, Thailand, Nepal, Indonesia, and Turkey.",
    "What is the best place for a honeymoon trip?": "The best honeymoon destinations include Maldives, Santorini, Paris, Bali, and Venice.",
    "Which country has the best beaches?": "Countries with the best beaches include the Maldives, Seychelles, Thailand, Australia, and Greece.",
    "Where can I see the Northern Lights?": "The Northern Lights can be seen in Norway, Iceland, Sweden, Finland, and Canada.",
    "What are the best places to visit in Dubai?": "The best places to visit in Dubai include Burj Khalifa, Dubai Mall, Palm Jumeirah, and Desert Safari.",
    "Where can I go for a peaceful and quiet vacation?": "Some peaceful destinations include Bhutan, Faroe Islands, New Zealand, and the Swiss Alps.",
    "Which are the best eco-friendly travel destinations?": "Best eco-travel spots include Costa Rica, Norway, Bhutan, and New Zealand.",
    "What are the top historical places in Rome?": "Top historical places in Rome include the Colosseum, Pantheon, Roman Forum, and St. Peter's Basilica.",
    "What are the most famous landmarks in London?": "Famous landmarks in London include Big Ben, Tower of London, Buckingham Palace, and London Eye.",
    "Which are the best ski resorts in Switzerland?": "Best ski resorts in Switzerland include Zermatt, St. Moritz, Verbier, and Engelberg.",
    "What are the must-visit places in Japan?": "Must-visit places in Japan include Mount Fuji, Kyoto, Tokyo Tower, and Hiroshima Peace Memorial.",
    "Which city is known as the Venice of the East?": "Udaipur in India is known as the Venice of the East due to its beautiful lakes and palaces.",
    "What are the best summer destinations in Europe?": "Best summer destinations in Europe include Santorini, Amalfi Coast, Barcelona, and the French Riviera.",
    "What are the safest countries for solo travelers?": "Some of the safest countries for solo travelers are Iceland, Japan, Switzerland, Canada, and New Zealand.",
    "Where can I experience the best wildlife safari?": "The best wildlife safaris are in Maasai Mara (Kenya), Kruger National Park (South Africa), and Serengeti (Tanzania).",
    "What are the best places for food lovers?": "Best places for food lovers include Bangkok, Tokyo, Paris, Istanbul, and Mexico City.",
    "Which cities have the best nightlife?": "Cities with the best nightlife include Las Vegas, Berlin, Amsterdam, Bangkok, and Ibiza.",
    "What are the best islands to visit in the Caribbean?": "Best Caribbean islands include Barbados, St. Lucia, Jamaica, and the Bahamas.",
    "Which are the top luxury travel destinations?": "Top luxury destinations include Dubai, Monaco, Maldives, Seychelles, and Bora Bora.",
    "What are the best places to visit in Australia?": "Best places in Australia include Sydney Opera House, Great Barrier Reef, Uluru, and Melbourne.",
    "What is the best time to visit Japan?": "The best time to visit Japan is during cherry blossom season (March-April) or autumn (September-November).",
    "What are the best places for a road trip in the USA?": "Best road trip routes in the USA include Route 66, Pacific Coast Highway, and Blue Ridge Parkway.",
    "Which countries are the most visa-friendly for travelers?": "Most visa-friendly countries include Indonesia, Thailand, Georgia, and Serbia.",
    "What are the best places to visit in South America?": "Top places in South America include Machu Picchu, Iguazu Falls, Patagonia, and the Amazon Rainforest.",
    "Which are the best cities to visit in Canada?": "Best cities in Canada include Vancouver, Toronto, Montreal, and Quebec City.",
    "Where can I go for an offbeat travel experience?": "Offbeat travel spots include Svalbard (Norway), Bhutan, Faroe Islands, and Socotra (Yemen).",
    "What are the best street food destinations in the world?": "Best street food destinations include Bangkok, Mexico City, Istanbul, Mumbai, and Ho Chi Minh City.",
    "What are the best places for cultural experiences?": "Best cultural destinations include Kyoto, Cairo, Varanasi, Marrakech, and Athens.",
    "Where are the most beautiful waterfalls in the world?": "Top waterfalls include Iguazu Falls, Victoria Falls, Angel Falls, and Niagara Falls.",
    "Which are the best train journeys in the world?": "Best train journeys include the Trans-Siberian Railway, Glacier Express, and the Orient Express.",
    "What are the best places to see cherry blossoms?": "Best places for cherry blossoms include Japan, Washington D.C., South Korea, and Paris.",
    "Which are the most romantic destinations?": "Most romantic destinations include Venice, Paris, Santorini, Prague, and Kyoto.",
    "What are the best places to visit in New Zealand?": "Best places in New Zealand include Milford Sound, Queenstown, Rotorua, and Wellington.",
    "Where are the best hiking destinations?": "Best hiking destinations include Patagonia, Himalayas, Rocky Mountains, and the Dolomites.",
    "Which countries have the best cultural festivals?": "Best cultural festivals include Carnival (Brazil), Oktoberfest (Germany), Holi (India), and La Tomatina (Spain).",
    "What are the best places to visit in Egypt?": "Best places in Egypt include the Pyramids of Giza, Luxor, Nile River, and the Red Sea.",
    "Where can I go for the best snorkeling experience?": "Best snorkeling spots include the Maldives, Great Barrier Reef, Red Sea, and Raja Ampat.",
    "What are the best places for winter travel?": "Best winter destinations include Lapland, Canada, Switzerland, and Japan’s ski resorts.",
    "What are the most unique places to visit?": "Most unique places include Salar de Uyuni, Cappadocia, Antelope Canyon, and the Great Blue Hole.",
    "Which cities have the best Christmas markets?": "Best Christmas markets include Vienna, Prague, Strasbourg, and Nuremberg.",
    "What are the most beautiful villages in the world?": "Most beautiful villages include Hallstatt (Austria), Shirakawa-go (Japan), and Reine (Norway).",
    "Where can I see the best autumn foliage?": "Best autumn foliage spots include Kyoto, Vermont (USA), Bavaria (Germany), and Quebec.",
    "What are the most underrated travel destinations?": "Underrated destinations include Albania, Georgia, Madagascar, and Bolivia.",
    "Where can I experience the best desert landscapes?": "Best deserts include the Sahara, Atacama, Wadi Rum, and the Namib Desert.",
    "What are the best UNESCO World Heritage sites?": "Top UNESCO sites include Machu Picchu, Petra, Great Wall of China, and Angkor Wat.",
}
    # Convert keys to a list of suggested questions
    suggested_questions = list(chatbot_responses.keys())

    # User selects a predefined question
    selected_question = st.selectbox("Select a question:", ["Choose a question..."] + suggested_questions)

    # Determine which query to use
    query_to_ask = selected_question if selected_question != "Choose a question..." else ""

    # Button to get answer
    if st.button("💬 Get Answer"):
        if not query_to_ask:
            st.warning("Please select a question.")
        elif query_to_ask in chatbot_responses:
            st.success(chatbot_responses[query_to_ask])
        else:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful travel assistant."},
                        {"role": "user", "content": query_to_ask}
                    ]
                )
                st.success(response["choices"][0]["message"]["content"])
            except Exception as e:
                st.error(f"Error fetching response: {e}")