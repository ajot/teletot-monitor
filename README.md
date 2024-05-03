# TeleTot Sound Monitor

## 📢 Overview
**TeleTot Sound Monitor** is a Telegram bot designed for parents who need a simple and effective way to monitor their baby while traveling. It overcomes typical hotel Wi-Fi limitations to deliver live audio from your baby's room directly to your phone. With just a quick Telegram command, you can listen to 10-second audio clips to ensure your baby is sleeping soundly or to check for any disturbances.

![TeletTot Sound Monitor](/assets/teletot.PNG)

## 🌟 Features
- **Instant Audio Monitoring**: Send a command via Telegram and receive a 10-second audio clip from your baby's room.
- **Designed for Travel**: Specifically useful in hotels where traditional baby monitors fail due to Wi-Fi restrictions.
- **Easy to Use**: Operates entirely through Telegram, making it accessible from anywhere.

## 👶 Who is This For?
This bot is perfect for traveling parents who want to keep an ear on their sleeping baby without the need for complex setups or specialized equipment. Whether you're in the next room or at a hotel restaurant, **TeleTot Sound Monitor** keeps you connected to your little one.

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or newer installed on your machine.
- A Telegram account.

### Creating Your Telegram Bot
1. **Start BotFather**: Go to Telegram and search for [@BotFather](https://t.me/botfather), which is the official bot for creating other bots.
2. **Create a New Bot**: Send the `/newbot` command and follow the instructions. BotFather will ask you for a name and username, then provide you with a token.
3. **Save the Token**: Keep the token secure as you will need it to run your TeleTot Sound Monitor bot.

### Setting up the Python Script
1. **Clone the Repository**
   ```
   git clone https://github.com/yourgithub/teletot-sound-monitor.git
   cd teletot-sound-monitor
   ```

2. **Install Dependencies**
   Run the following command to install the necessary Python packages:
   ```
   pip install -r requirements.txt
   ```

3. **Configure the Bot**
   - Rename `config-sample.py` to `config.py` in the root directory of the project.
   - Open `config.py` and replace `your_bot_token_here` with your actual Telegram bot token:
     ```python
     TELEGRAM_API_TOKEN = 'your_bot_token_here'
     ```

### Usage
To run the bot:
```
python src/main.py
```
Once the bot is running, use Telegram to send commands:
- Send `/record` to receive a 10-second audio clip from your baby's room.

## 🚀 Got Ideas or Feedback? 
I'd love to hear how you're using TeleTot Sound Monitor and any cool ideas you have to make it even better! Hit me up on Twitter [@amit](https://twitter.com/amit) and let’s chat about it. 

## 🤝 Contributing
Contributions are welcome! If you have improvements or features you'd like to add, please feel free to fork the repository, make your changes, and submit a pull request.

## 📜 License
**TeleTot Sound Monitor** is released under the MIT License. See the [LICENSE](LICENSE) file for more details.