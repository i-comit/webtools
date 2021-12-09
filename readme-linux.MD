In order for the chrome driver in linux to work, you must install the chrome binary, by running these commands in order within bash:

Forgot to mention, you will need a computer with 64-bit architecture.

wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list

sudo apt-get update 

sudo apt-get install google-chrome-stable
