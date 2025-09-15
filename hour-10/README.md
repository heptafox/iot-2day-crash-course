# Hour 10 — AI + IoT: Simple Smart Sensors 🤖

## The Big Idea
**Traditional IoT**: Fixed rules (if temp > 30, turn on fan)  
**AI IoT**: Smart decisions with explanations!

**Simple Flow**: Sensor → AI → Action

---

## What We'll Build

### 🎯 Three Simple Programs

1. **01_hello_ai.py** - Talk to AI and get JSON back
2. **02_ai_decider_server.py** - Server that asks AI to decide ON/OFF  
3. **03_pico_ai_client.py** - Pico reads sensor → asks AI → controls LED

---

## 🚀 Quick Setup

### For Laptop Programs

1. **Install requirements**
```bash
cd hour-10
pip install flask requests python-dotenv
```

2. **Get OpenRouter API Key**
- Go to https://openrouter.ai
- Sign up and get your API key
- Create `.env` file:
```
OPENROUTER_API_KEY=sk-or-your-key-here
```

3. **Try Hello AI**
```bash
python 01_hello_ai.py
```

4. **Start Decision Server**
```bash
python 02_ai_decider_server.py
```

### For Pico W

1. **Hardware Setup**
- DHT11 sensor → Pin 16
- LED → Pin 15 (with resistor)

2. **Edit the Script**
Open `03_pico_ai_client.py` and change:
```python
WIFI_SSID = "YourWiFiName"
WIFI_PASSWORD = "YourPassword"  
API_KEY = "sk-or-your-openrouter-key"
```

3. **Upload to Pico W**
- Use Thonny IDE
- Copy script to Pico W
- Run it!

---

## 🎮 How It Works

**The Magic Loop:**
1. 🌡️ Pico reads temperature & humidity
2. 🤖 Asks AI: "Should LED be ON or OFF?"
3. 💡 AI decides and explains why
4. ⚡ LED turns ON/OFF based on AI decision

**Example AI Response:**
```json
{
  "decision": "ON",
  "reason": "Temperature 32°C is above 30°C threshold"
}
```

---

## 🔧 Simple Rule

**Current AI Rule**: Turn LED ON if temperature > 30°C OR humidity > 80%

**Want to change it?** Edit the prompt in any script!

---

## 🎯 Learning Goals

✅ Understand AI + IoT basics  
✅ See how AI makes decisions  
✅ Learn to prompt AI for structured responses  
✅ Build complete sensor → AI → action loop  

---

## 🐛 Troubleshooting

**"API Key Error"** → Check your OpenRouter key  
**"WiFi Failed"** → Check WiFi name/password  
**"Sensor Error"** → Check DHT11 wiring  
**"AI Failed"** → Script uses backup rules automatically  

---

## 🎉 Try This!

- Change the temperature threshold in the AI prompt
- Add more sensors (like soil moisture)  
- Make AI control different outputs (buzzer, servo, etc.)
- Ask AI to explain weather conditions

**The power of AI + IoT**: Same sensors, infinite possibilities through different prompts! 🚀


