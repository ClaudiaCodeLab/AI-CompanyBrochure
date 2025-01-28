# Company Brochure Generator

A Python-based application that uses web scraping and a large language model (LLM) to generate brochures for companies based on their website content. The app provides a Gradio-based interface for ease of use.

---

## Features
- **Web Scraping:** Scrapes the company's landing page and other relevant links to gather content.
- **LLM Integration:** Uses a locally running LLaMA model (via Ollama) to analyze and generate a polished brochure.
- **Error Handling:** Robust handling of unavailable or broken links.
- **Gradio Interface:** A user-friendly web interface for generating brochures.

---

## Installation

### Prerequisites
1. Python 3.8 or higher.
2. [Ollama](https://ollama.ai/) installed and running.
3. LLaMA model pulled locally:
   ```bash
   ollama pull llama3.2

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/company-brochure-generator.git
    cd company-brochure-generator

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows 

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
### Running the App
Launch the Gradio interface:
    ```bash
    python app.py

### Using the App
1. Enter the company name and website URL in the respective fields.
2. Click "Generate Brochure."
3. View the generated brochure in the output panel.

### File Structure

AI-CompanyBrochure/
│-- app.py                  # Entry point for Gradio interface
│-- config.py               # Configuration (API keys, constants)
│-- llm_client.py           # Handles interactions with the LLM
│-- web_scraper.py          # Web scraping logic
│-- brochure_generator.py   # Core logic for generating brochures
│-- requirements.txt        # Dependencies
│-- README.md               # Project documentation

## Dependencies
- gradio
- openai
- requests
- beautifulsoup4

Install all dependencies via:
    ```bash
    pip install -r requirements.txt

## Troubleshooting
- Ollama Issues: Ensure the Ollama service is running locally.
    ```bash
    ollama serve
- Model Not Found: Pull the required model:
    ```bash
    ollama pull llama3.2
- Broken URLs: The app skips broken or unavailable URLs and logs warnings.

## License
This project is licensed under the MIT License.

