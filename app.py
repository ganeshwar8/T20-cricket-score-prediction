import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('t20.pkl', 'rb'))

cities =['','London', 'Sydney', 'Bristol', 'Wellington', 'St Lucia', 'Dubai',
       'Abu Dhabi', 'Johannesburg', 'Trinidad', 'Auckland', 'Dhaka',
       'Dehra Dun', 'Barbados', 'Colombo', 'Nagpur', 'Christchurch',
       'Harare', 'St Kitts', 'Jamaica', 'Centurion', 'Napier',
       'Southampton', 'Kandy', 'Adelaide', 'Delhi', 'Sharjah', 'Lucknow',
       'Mirpur', 'Chandigarh', 'Cape Town', 'Mount Maunganui',
       'Greater Noida', 'Nottingham', 'Durban', 'Dublin', 'Pune',
       'Pallekele', 'Hamilton', 'Lauderhill', 'Bulawayo', 'Chittagong',
       'Cardiff', 'Birmingham', 'Basseterre', 'Bangalore', 'Melbourne',
       'Mumbai', 'Al Amarat', 'East London', 'Manchester', 'Rawalpindi',
       'Brisbane', 'Lahore', 'Hambantota', 'Hobart', 'Kolkata', 'Perth',
       'Edinburgh', 'Antigua', 'Port Elizabeth', 'Guyana', 'Dharamsala',
       'Rotterdam', 'Chattogram', 'Chester-le-Street', 'Karachi',
       'Sylhet', 'Bready', 'Rajkot', 'Khulna']

team =['','England', 'Australia', 'New Zealand', 'Afghanistan',
       'South Africa', 'West Indies', 'Bangladesh', 'Netherlands',
       'Sri Lanka', 'Scotland', 'India', 'Pakistan', 'Zimbabwe',
       'Ireland']

st.title('T20-cricket-score-prediction')

col1, col2 = st.columns(2)

with col1:
       batting_team = st.selectbox('select batting team', sorted(team))

with col2:
       bowling_team = st.selectbox('select bowling team', sorted(team))

city = st.selectbox('select city', sorted(cities))

col3, col4, col5 = st.columns(3)

with col3:
       current_score = st.number_input('current_score')

with col4:
       overs = st.number_input('overs done(works for overs>5)')

with col5:
       wickets = st.number_input('wickets out')

last_five = st.number_input('Runs scored in last 5 overs')

if st.button('predict score'):
       balls_left = 120 - (overs*6)
       wickets_left = 10-wickets
       current_run_rate = current_score/overs

       input_da = pd.DataFrame(
              { 'batting_team': [batting_team], 'bowling_team': [bowling_team], 'city': city, 'current_score':
               [current_score], 'wickets_left': [wickets], 'balls_left': [balls_left],
               'current_run_rate': [current_run_rate], 'last_five_over_runs': [last_five]})

       result = model.predict(input_da)
       st.header('predicted score' + str(int(result[0])))


