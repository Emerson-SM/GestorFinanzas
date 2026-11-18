import streamlit as st


def apply_custom_styles():

    st.markdown(
        """<style>

        /* Main page */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        /* Section headings */
        h1, h2, h3 {
            font-weight: 600;
        }

        /* Buttons */
        div.stButton > button {
            border-radius: 8px;
            font-weight: 600;
            padding: 0.45rem 1rem;
            transition: 0.2s ease;
        }

        /* Primary buttons */
        div.stButton > button[kind="primary"] {
            background-color: #10B981;
            color: #0E1117;
            border: 1px solid #10B981;
        }

        div.stButton > button[kind="primary"]:hover {
            background-color: #059669;
            border-color: #059669;
            color: white;
        }

        /* Secondary buttons */
        div.stButton > button[kind="secondary"] {
            background-color: #1B2330;
            color: #E6EDF3;
            border: 1px solid #303B4B;
        }

        div.stButton > button[kind="secondary"]:hover {
            border-color: #10B981;
            color: #10B981;
        }

        /* Containers / Cards */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 12px;
        }

        /* Metrics */
        div[data-testid="stMetric"] {
            padding: 0.3rem 0;
        }

        div[data-testid="stMetricLabel"] {
            color: #9CA3AF;
        }

        div[data-testid="stMetricValue"] {
            font-weight: 600;
        }

        /* Dividers */
        hr {
            border-color: #303B4B;
            margin-top: 1.5rem;
            margin-bottom: 1.5rem;
        }

        </style>""", unsafe_allow_html=True
    )