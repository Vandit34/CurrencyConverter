import streamlit as st
import requests

def convert_currency(amount, toCurrency, fromCurrency):
    url = f"https://v6.exchangerate-api.com/v6/5df93b8f5001fdb353a2ced4/latest/{fromCurrency}"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data['conversion_rates'][toCurrency]
    converted_amount = amount * exchange_rate
    return converted_amount

st.title('Currency Converter')

amount = st.number_input('Enter the amount you want to convert', value=1.0)
fromCurrency = st.text_input('Enter from currency: ')
toCurrency = st.text_input('Enter to currency: ')

if st.button('Convert'):
    result = convert_currency(amount, toCurrency, fromCurrency)
    st.write(f'{amount} {fromCurrency} is equivalent to {result} {toCurrency}')