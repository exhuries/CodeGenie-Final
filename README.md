# CodeGenie-Final

# CodeGenie – AI-Powered Code Generation Tool

CodeGenie is a browser-based application that uses a large language model (LLM) to generate code from plain English prompts. It helps users, especially beginners, convert their coding ideas into functional code without needing to search online or write boilerplate manually.

## Features

- Text prompt input for asking coding questions or requests
- Real-time code generation using the CodeLlama model (7B, quantized)
- Clean interface built with Streamlit
- Lightweight enough to run on Google Colab with CPU
- Easy deployment via LocalTunnel for sharing the app live

## How It Works

1. User enters a code-related prompt (e.g., “Write a Python program to check prime numbers”).
2. The prompt is sent to a locally running instance of the CodeLlama model using llama-cpp-python.
3. The model processes the input and returns the appropriate code.
4. The code is displayed in the Streamlit web interface with syntax highlighting.

## Project Structure

.
├── app.py                 # Streamlit frontend interface  
├── CodeModel.py           # Model loading and code generation logic  
├── requirements.txt       # Python dependencies  
├── Final Deliverables/    # Screenshots, demo video, report  
├── Assignments/           # Team member contributions  
└── Project Design & Planning/

## How to Run (in Google Colab)

1. Upload `app.py` and `CodeModel.py` in your Colab notebook.
2. Install required packages:
   ```
   !pip install streamlit llama-cpp-python
   !npm install -g localtunnel
   ```
3. Run Streamlit in the background:
   ```
   !streamlit run app.py --server.address=localhost > /content/logs.txt 2>&1 &
   ```
4. Launch LocalTunnel to expose the port:
   ```
   !npx localtunnel --port 8501
   ```
5. Click the public URL shown in the output to view the app in your browser.

## Team Members

- Rahul Biju Veyccal (22BCT0237)   
- Shaik Kaif Sharif (23BCE9393)  
- Suyash Pandey (22BCT0111)  
- Vansh Saxena (23BCE10177) 

## Screenshots

Prompt example:

![User Prompt](./Final Deliverables/Screenshots/user_prompt.jpg)

Generated output:

![Generated Code](./Final Deliverables/Screenshots/code_output.jpg)

## Report and Demo

- Final Project Report (PDF): `Final Deliverables/Report.pdf`  
- Demonstration Video: `Final Deliverables/Demo Video/CodeGenie_Demo.mp4`

## License

This project is for academic and educational purposes only.
