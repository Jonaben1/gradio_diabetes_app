mkdir -p ~/.gradio/


echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.gradio/config.toml
