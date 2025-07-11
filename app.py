import streamlit as st

import joblib

import pandas as pd

teams = ['Royal Challengers Bangalore',
 'Kings XI Punjab',
 'Mumbai Indians',
 'Kolkata Knight Riders',
 'Chennai Super Kings',
 'Sunrisers Hyderabad',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Bangalore', 'Chandigarh', 'Delhi', 'Mumbai', 'Kolkata', 'Jaipur',
       'Hyderabad', 'Chennai', 'Cape Town', 'Port Elizabeth', 'Durban',
       'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Bengaluru', 'Indore', 'Dubai', 'Sharjah', 'Navi Mumbai',
       'Guwahati', 'Mohali']

pipe = joblib.load('pipe.pkl')

st.title('IPL win Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team =st.selectbox('Select the batting team',teams)

with col2:
    bowling_team = st.selectbox('Select the bowling team', teams)

selected_city = st.selectbox('Select host city' , sorted(cities))

target = st.number_input('Target')

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs Completed')
with col5:
    wickets = st.number_input('Wickets Out')

if st.button('Predict Probability'):
    left_runs = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (left_runs*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],
                  'city':[selected_city],'left_runs':[left_runs],'balls_left':[balls_left],'wickets':[wickets],
                  'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win * 100)) + "%")
    st.header(bowling_team + "- " + str(round(loss * 100)) + "%")





