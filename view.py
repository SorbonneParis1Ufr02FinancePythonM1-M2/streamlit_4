import pandas as pd
import streamlit as st

from repository import get_data


def to_streamlit(config: dict):
    income_statements, balance_sheet_statements, cash_flow_statements = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

    st.set_page_config(page_title=config['streamlit']['page_title'],
                       layout=config['streamlit']['layout'],
                       initial_sidebar_state=config['streamlit']['sidebar_state'])

    tickers = st.sidebar.multiselect(config['streamlit']['multiselect_tickers_label'], config["tickers"])

    go = st.sidebar.button(config['streamlit']['button_label'])

    if go:
        income_statements, balance_sheet_statements, cash_flow_statements = get_data(tickers)

        exp_describe = st.expander(config['expanders']['describe'])

        with exp_describe:
            st.subheader(config['streamlit']['income_statements_name'])
            st.dataframe(income_statements.describe(include='all'))

            st.subheader(config['streamlit']['balance_sheet_statements_name'])
            st.dataframe(balance_sheet_statements.describe(include='all'))

            st.subheader(config['streamlit']['cash_flow_statements_name'])
            st.dataframe(cash_flow_statements.describe(include='all'))

        st.subheader(config['streamlit']['income_statements_name'])
        st.dataframe(income_statements)

        st.subheader(config['streamlit']['balance_sheet_statements_name'])
        st.dataframe(balance_sheet_statements)

        st.subheader(config['streamlit']['cash_flow_statements_name'])
        st.dataframe(cash_flow_statements)
