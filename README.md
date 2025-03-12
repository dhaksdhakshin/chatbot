# Streamlit Chatbot with Gemini Pro & Vision API

This is a chatbot built using Streamlit and Google's Gemini Pro API, including Vision API for handling images. The chatbot provides intelligent responses and can process both text and images .

## Features
- Interactive chatbot powered by **Gemini Pro**
- Supports text-based conversations
- Streamlit-based UI for a user-friendly experience 
- Customizable UI with a sleek modern look.
 
## File Structure
```
ChatBot/
│── main.py                # Main script for running the chatbot 
│── requirements.txt       # Dependencies
│── README.md              # Documentation
```

## Prerequisites
Make sure you have Python **3.8+** installed. If not, download it from [python.org](https://www.python.org/downloads/).

## Installation
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/streamlit-chatbot.git
cd streamlit-chatbot
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Chatbot
Once everything is set up, start the chatbot with:
```bash
streamlit run main.py
```
This will open a Streamlit web app in your browser.

## Troubleshooting
### Streamlit Not Found
If you get an error like `streamlit: command not found`, add the following path to your system’s **Environment Variables**:
```
C:\Users\YourUsername\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\Scripts
```
Then restart your terminal and try again.

### Issues with Dependencies
If some packages fail to install, upgrade `pip` and try reinstalling:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Customizing the UI
To improve the chatbot’s appearance, modify the `st.markdown()` and `st.write()` elements in `main.py`. You can also use **Streamlit themes** or **CSS** for styling.

## Contributing
Feel free to submit pull requests or report issues to improve this project!

## License
This project is licensed under the MIT License.

---
Happy coding!

