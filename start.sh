echo "Cloning main Repository"
  git clone https://github.com/Ashrafmdmatin41/accept.git /Accept
  git clone $UPSTREAM_REPO /accept
cd /accept
pip3 install -U -r requirements.txt
echo "𝙎𝙩𝙖𝙧𝙩𝙞𝙣𝙜 𝙀𝙡𝙨𝙖....🧞‍♂️"
python3 bot.py
