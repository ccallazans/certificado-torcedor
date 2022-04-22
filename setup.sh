mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]\n\
primaryColor='#005ba8'\n\
backgroundColor='#f6f6f6'\n\
#secondaryBackgroundColor='#005ba8'\n\
textColor='#262730'\n\
font='sans serif'\n\
\n\
" > ~/.streamlit/config.toml

