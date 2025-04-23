import streamlit as st
import streamlit.components.v1 as components
import streamlit as st
import pickle
import pandas as pd
import random
# from src.remove_ import remove

def load_app():
    #LIBRARIES
    import streamlit as st
    import subprocess
    import pickle
    import nltk
    import pandas as pd
    from textblob import TextBlob
    from nltk.corpus import stopwords
    from nltk.stem import  PorterStemmer 
    import re
    import os
    import review_crawler


    #LOAD PICKLE FILES
    model = pickle.load(open('Models/best_model.pkl','rb')) 
    vectorizer = pickle.load(open('Models/count_vectorizer.pkl','rb')) 

    #FOR STREAMLIT
    nltk.download('stopwords')

    #TEXT PREPROCESSING
    sw = set(stopwords.words('english'))
    def text_preprocessing(review):
        # --TEXT PREPROCESSING--
        txt = TextBlob(review)
        result = txt.correct()
        removed_special_characters = re.sub("[^a-zA-Z]", " ", str(result))
        tokens = removed_special_characters.lower().split()
        stemmer = PorterStemmer()

        cleaned = []
        stemmed = []

        for token in tokens:
            if token not in sw:
                cleaned.append(token)

        for token in cleaned:
            token = stemmer.stem(token)
            stemmed.append(token)

        return " ".join(stemmed)

    #TEXT CLASSIFICATION
    def text_classification(review):
        # review = text_preprocessing(url)
        if len(review) < 1:
            st.write("  ")    
        else:
            with st.spinner("Classification in progress..."):
                cleaned_review = text_preprocessing(review)
                process = vectorizer.transform([cleaned_review]).toarray()
                prediction = model.predict(process)
                p = ''.join(str(i) for i in prediction)
                st.write(review)

                if p == 'True':
                    st.success("The review entered is Legitimate.")
                if p == 'False':
                    st.error("The review entered is Fake.")


    #PAGE FORMATTING AND APPLICATION
    def main():
        st.title("Fake Product Detection Of Electronic Products Using Machine Learning Techniques")


        #--IMPLEMENTATION OF THE CLASSIFIER--
        st.subheader("Fake Product Review Classifier")
        url = st.text_area("Enter Url: ")
        if st.button("Check"):
            subprocess.call(f" python review_crawler.py {url} ", shell=True)
            df = pd.read_csv('reviews.csv')
            reviews = df['body'].to_list()
            while len(reviews) > 0:
                for review in reviews:
                    text_classification(review)
                    reviews.remove(review)





    #RUN MAIN
    main()

    
def load_app1():
    import streamlit as st

    st.title('TV📺')
    # Define the options for the dropdown
    tv_options = ["Samsung TV", "Sony TV"]

    # Create the dropdown menu
    selected_tv = st.selectbox("Select a TV brand:", tv_options)

    # Samsung TV data
    samsung_tvs = [
        {
"name": "Samsung QLED Q60A",
"image": "image/sam7.jpg",
"description": "The Samsung QLED Q60A offers a sleek design and impressive picture quality with vibrant colors and good contrast, perfect for an immersive viewing experience."
},
        {
            "name": "Samsung QLED Q60T",
            "image": "image/sam1.jpg",
            "description": "The Samsung QLED Q60T offers stunning picture quality with vibrant colors and deep blacks."
        },
        {
            "name": "Samsung Crystal UHD TU8000",
            "image": "image/sam2.jpg",
            "description": "Screen Size	50 Inches"
            "Brand:Samsung Display "
            "Technology:QLED"
            "Resolution:4K"
            "Refresh Rate:60 Hz ""Special Feature	100% Color Volume with Quantum Dot; Quantum HDR; Smart TV Powered by TIZEN; Quantum Processor 4K Lite100% Color Volume with Quantum Dot; Quantum HDR; Smart TV Powered by TIZEN; Quantum ProcessorLite"
        },
        {
            "name": "Samsung Frame TV",
            "image": "image/sam3.jpg",
            "description": "The Frame TV seamlessly blends into any living space with customizable bezel options."
        },
        {
"name": "Samsung QLED Q70T",
"image": "image/sam4.jpg",
"description": "The Samsung QLED Q70T offers a balanced picture quality with a good mix of vibrant colors, deep blacks, and impressive motion handling, suitable for both movies and gaming."
},
        {
"name": "Samsung QLED Q90T",
"image": "image/sam5.jpg",
"description": "The Samsung QLED Q90T features top-tier picture quality with deep blacks, high peak brightness, and an impressive array of smart features."
}
    ]

    # Sony TV data
    sony_tvs = [
        {
            "name": "Sony Bravia X800H",
            "image": "image/son1.jpg",
            "description": "Sony Bravia X800H delivers a powerful picture with a wide range of colors and enhanced clarity."
        },
        {
            "name": "Sony OLED A8H",
            "image": "image/son2.jpg",
            "description": "The Sony OLED A8H features perfect blacks, incredible contrast, and stunning color depth."
        },
        {
            "name": "Sony X900H",
            "image": "image/son3.jpg",
            "description": "The X900H combines stunning picture quality with an immersive audio experience."
        }
    ]

    # Function to display TV details in a row
    def display_tv_details(tvs):
        for i in range(0, len(tvs), 3):
            cols = st.columns(3)
            for col, tv in zip(cols, tvs[i:i + 3]):
                col.image(tv["image"], caption=tv["name"], use_column_width=True)
                col.write(tv["description"])
    
    
    # Display the selected TV brand details
    if selected_tv == "Samsung TV":
        display_tv_details(samsung_tvs)
    elif selected_tv == "Sony TV":
        display_tv_details(sony_tvs)

        
def load_app_mobiles():
    import streamlit as st

    st.title('Newly Launched Mobiles📱')
    # Define the options for the dropdown
    mobile_brands = ["Samsung", "Apple", "Google"]

    # Create the dropdown menu
    selected_brand = st.selectbox("Select a mobile brand:", mobile_brands)

    # Mobile data
    mobiles = {
        "Samsung": [
            {
                "name": "Samsung Galaxy S21",
                "image": "image/s21.jpg",
                "description": "Display: Dynamic AMOLED 2X\n"
                               "Camera: Triple camera setup with 64MP main sensor\n"
                               "Battery: 4000mAh\n"
                               "Features: Exynos 2100, 5G support, One UI 3.1"
            },
            {
                "name": "Samsung Galaxy Note 20",
                "image": "image/s20.jpg",
                "description": "Display: Super AMOLED Plus\n"
                               "Camera: Triple camera setup with 108MP main sensor\n"
                               "Battery: 4300mAh\n"
                               "Features: Exynos 990, 5G support, S Pen"
            },
            {
    "name": "Samsung Galaxy M31",
    "image": "image/sam8.jpg",
    "description": "Display: Super AMOLED\n"
                   "Camera: Quad camera setup with 64MP main sensor\n"
                   "Battery: 6000mAh\n"
                   "Features: Exynos 9611, 4G support, One UI 2.1"
},

            {
    "name": "Samsung Galaxy A71",
    "image": "image/sam9.jpg.jpeg",
    "description": "Display: Super AMOLED Plus\n"
                   "Camera: Quad camera setup with 64MP main sensor\n"
                   "Battery: 4500mAh\n"
                   "Features: Snapdragon 730, 4G support, One UI 2.0"
},
            {
    "name": "Samsung Galaxy A52",
    "image": "image/a52.jpg",
    "description": "Display: Super AMOLED\n"
                   "Camera: Quad camera setup with 64MP main sensor\n"
                   "Battery: 4500mAh\n"
                   "Features: Snapdragon 720G, 4G support, One UI 3.1"
},
         {
    "name": "Samsung Galaxy Z Fold 2",
    "image": "image/sam6.jpg.jpeg",
    "description": "Display: Foldable Dynamic AMOLED 2X\n"
                   "Camera: Triple camera setup with 12MP main sensor\n"
                   "Battery: 4500mAh\n"
                   "Features: Snapdragon 865+, 5G support, One UI 2.5"
}
   

            
        ],
        "Apple": [
            {
                "name": "Apple iPhone 13",
                "image": "image/i13.jpg",
                "description": "Display: Super Retina XDR display\n"
                               "Camera: Dual 12MP camera system\n"
                               "Battery: Up to 19 hours video playback\n"
                               "Features: A15 Bionic chip, 5G support, iOS 15"
            },
            {
                "name": "Apple iPhone 13 Pro",
                "image": "image/i13p.jpg",
                "description": "Display: Super Retina XDR display with ProMotion\n"
                               "Camera: Triple 12MP camera system\n"
                               "Battery: Up to 22 hours video playback\n"
                               "Features: A15 Bionic chip, 5G support, iOS 15"
            }
        ],
        "Google": [
            {
                "name": "Google Pixel 6",
                "image": "image/g1.jpg.jpeg",
                "description": "Display: AMOLED\n"
                               "Camera: Dual camera with 50MP main sensor\n"
                               "Battery: 4614mAh\n"
                               "Features: Google Tensor chip, 5G support, Android 12"
            },
            {
                "name": "Google Pixel 6 Pro",
                "image": "image/g2.jpg.jpeg",
                "description": "Display: AMOLED\n"
                               "Camera: Triple camera with 50MP main sensor\n"
                               "Battery: 5003mAh\n"
                               "Features: Google Tensor chip, 5G support, Android 12"
            }
        ]
    }

    # Function to display mobile details in a row
    def display_mobile_details(brand_mobiles):
        for i in range(0, len(brand_mobiles), 3):
            cols = st.columns(3)
            for col, mobile in zip(cols, brand_mobiles[i:i + 3]):
                col.image(mobile["image"], caption=mobile["name"], use_column_width=True)
                col.write(mobile["description"])
        

    # Display the selected mobile brand details
    if selected_brand in mobiles:
        display_mobile_details(mobiles[selected_brand])
        
# Run the mobile app
#load_app_mobiles()        
        
def load_app_smartwatches():
    import streamlit as st

    st.title('Newly Launched Smartwatches⌚')
    # Define the options for the dropdown
    watch_brands = ["Smart Watch"]

    # Create the dropdown menu
    selected_brand = st.selectbox("Select a smartwatch brand:", watch_brands)

    # Smartwatch data
    smartwatches = {
        "Smart Watch": [
            {
                "name": "Noise ColorFit Pro 3",
                "image": "image/noise1.jpg",
                "description": "Display: 1.55\" HD Touchscreen\n"
                               "Battery: Up to 10 days\n"
                               "Features: SpO2 monitor, 14 sports modes, 5ATM waterproof"
            },
            {
                "name": "Noise NoiseFit Evolve 2",
                "image": "image/noise3.jpg",
                "description": "Display: 1.2\" AMOLED display\n"
                               "Battery: Up to 7 days\n"
                               "Features: 24/7 heart rate monitoring, sleep tracking, 3ATM waterproof"
            },
        
        
            {
                "name": "Boat Xtend",
                "image": "image/boat1.jpg",
                "description": "Display: 1.69\" LCD Display\n"
                               "Battery: Up to 10 days\n"
                               "Features: Built-in Alexa, SpO2 monitor, 14 sports modes"
            },
            {
                "name": "Boat Storm",
                "image": "image/boat2.jpg",
                "description": "Display: 1.3\" Curved Display\n"
                               "Battery: Up to 10 days\n"
                               "Features: SpO2 & heart rate monitor, 9 sports modes, 5ATM waterproof"
            },
            {
                "name": "Apple Watch Series 7",
                "image": "image/apple1.jpg",
                "description": "Display: Always-On Retina display\n"
                               "Battery: Up to 18 hours\n"
                               "Features: Blood oxygen & ECG apps, 50m water resistant, watchOS 8"
            },
            {
                "name": "Apple Watch SE",
                "image": "image/apple4.jpg.jpeg",
                "description": "Display: Retina display\n"
                               "Battery: Up to 18 hours\n"
                               "Features: Fitness tracking, heart rate monitor, watchOS 8"
            }
        ]
    }

    # Function to display smartwatch details in a row
    def display_watch_details(brand_watches):
        for i in range(0, len(brand_watches), 3):
            cols = st.columns(3)
            for col, watch in zip(cols, brand_watches[i:i + 3]):
                col.image(watch["image"], caption=watch["name"], use_column_width=True)
                col.write(watch["description"])
            
    
    # Display the selected smartwatch brand details
    if selected_brand in smartwatches:
        display_watch_details(smartwatches[selected_brand])

# Run the smartwatches app
#load_app_smartwatches()


        
        
        
        
        
        
def load_app2():
    st.title('Laptops💻')
    # Define the options for the dropdown
    laptop_options = ["laptops"]

    # Create the dropdown menu
    selected_laptop = st.selectbox("Select a laptop brand:", laptop_options)

    # Dell laptop data
    laptops = {
          "laptops":[
        {
            "name": "Dell XPS 13",
            "image": "image/7.jpg",
            "description": "The Dell XPS 13 offers a stunning 4K display, powerful performance, and a sleek design."
        },
        {
            "name": "Dell Inspiron 15",
            "image": "image/8.jpg",
            "description": "Experience seamless multitasking with the Dell Inspiron 15, featuring a powerful Intel processor."
        },
        {
            "name": "Dell G5 15",
            "image": "image/9.jpg",
            "description": "The Dell G5 15 is a gaming laptop with a high-refresh-rate display and excellent graphics performance."
        },
   
        {
            "name": "HP Spectre x360",
            "image": "image/10.jpg",
            "description": "The HP Spectre x360 is a convertible laptop with a vibrant display and long battery life."
        },
        {
            "name": "HP Envy 13",
            "image": "image/11.jpg",
            "description": "The HP Envy 13 offers premium performance in a lightweight and stylish design."
        },
        {
            "name": "HP Pavilion 15",
            "image": "image/12.jpg",
            "description": "The HP Pavilion 15 provides a great balance of performance and affordability."
            }
        ]
     }
    # Function to display laptop details in a row
    def display_laptop_details(laptops):
        for i in range(0, len(laptops), 3):
            cols = st.columns(3)
            for col, laptop in zip(cols, laptops[i:i + 3]):
                col.image(laptop["image"], caption=laptop["name"], use_column_width=True)
                col.write(laptop["description"])

    # Display the selected laptop brand details
    if selected_laptop in laptops:
        display_laptop_details(laptops[selected_laptop])
def main():

    st.sidebar.image("image/s1.jpg.jfif", use_column_width=True, output_format='PNG', width=100)
    st.sidebar.title("Welcome")
    option = st.sidebar.radio("", ["Categories", "About Us","Fake Product"])

    if option == "Categories":
        st.sidebar.write("Select a category:")
        category_option = st.sidebar.radio("Categories", [ "Mobiles","Laptop","TV","Smart Watches"])

       
        if category_option == "TV":
            load_app1()
        elif category_option == "Laptop":
            load_app2()
        elif category_option == "Mobiles":
            load_app_mobiles() 
        elif category_option == "Smart Watches":
            load_app_smartwatches()     
    elif option == "About Us":
        st.markdown("## About Us")
        st.write("""
        The rapid growth of internet access has given rise to a digital era. The availability of internet access has pushed almost 70% of the population to switch to internet for their daily needs and accessories. Mainly, E-commerce platforms are being used at a much higher rate than ever before. People who buy from these e-commerce platforms make decisions on whether to buy a product or not solely based on the ratings and reviews of a product that are provided by these platforms. Due to the simple nature of this review system, sellers and even individuals tend to exploit it by writing dishonest reviews with an intention of either boosting its ratings or simply to sabotage it. These fake reviews are aimed at deceiving customers and convince them to buy/deter a certain product. Due to the lack of a robust system to identify real and fake reviews, these spams manage to show up on top. To avoid this problem and provide a more efficient way to filter and provide a more efficient way to reviews.
        """)
    elif option == "Fake Product":
        load_app()


# Run the main function
if __name__ == "__main__":
    main()
