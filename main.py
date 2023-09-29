import streamlit as st
import datetime
from news_api import get_news

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.write("# News Panel")

# # Define a list of categories
# categories = ["Competitors", "IOS", "Android"]

# # Create a sidebar for category selection
# selected_category = st.sidebar.selectbox("Select Category", categories)

# # Allow users to enter a custom category
custom_category = st.sidebar.text_input("Enter a Custom Category", value='data.ai')

# # Determine the selected category



from_date = st.sidebar.date_input(label="Start Date",
                                   value = datetime.datetime.now() - datetime.timedelta(7),
                                   min_value = datetime.datetime.now() - datetime.timedelta(30),
                                   max_value = datetime.datetime.now())

to_date = st.sidebar.date_input(label="end Date",
                                   value = datetime.datetime.now(),
                                   min_value = from_date,
                                   max_value = datetime.datetime.now())

# dates_selection = st.sidebar.slider(label="select date range",
#                                     min_value = datetime.datetime.now() - datetime.timedelta(30),
#                                     max_value = datetime.datetime.now(),
#                                     value = datetime.datetime.now() - datetime.timedelta(7))

sort_by_category = {"relevancy", "popularity", "publishedAt"}

sort_by = st.sidebar.selectbox("sort by", sort_by_category)

# st.header(f"News for Category: {selected_category}")

if custom_category:

    st.header(f'Search Results for {custom_category}')
    articles = get_news(query=custom_category,
                        from_date=from_date,
                        to_date=to_date,
                        sorty_by=sort_by)
    for article in articles['data']:
        text='[{title}]({link})'.format(title=article['title'],link=article['url'])
        st.markdown(text, unsafe_allow_html=True, help=article['description'])


col1, col2, col3 = st.columns(3)

with col1:
    st.header('Android')
    articles = get_news(query='android',
                        from_date=from_date,
                        to_date=to_date,
                        sorty_by=sort_by)
    for article in articles['data']:
        text='[{title}]({link})'.format(title=article['title'],link=article['url'])
        st.markdown(text, unsafe_allow_html=True, help=article['description'])

with col2:
    st.header('IOS')
    articles = get_news(query='ios',
                        from_date=from_date,
                        to_date=to_date,
                        sorty_by=sort_by)
    for article in articles['data']:
        text='[{title}]({link})'.format(title=article['title'],link=article['url'])
        st.markdown(text, unsafe_allow_html=True, help=article['description'])

with col3:
    st.header('Data.ai Competitors')
    articles = get_news(query='sensortower',
                        from_date=from_date,
                        to_date=to_date,
                        sorty_by=sort_by)
    for article in articles['data']:
        text='[{title}]({link})'.format(title=article['title'],link=article['url'])
        st.markdown(text, unsafe_allow_html=True, help=article['description'])






