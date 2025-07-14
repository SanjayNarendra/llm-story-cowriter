# llm-story-cowriter
an AI-powered collaborative fiction tool that lets users co-write imaginative stories set in futuristic or fantastical worlds. With pre-defined templates and modular writing prompts, users can shape narratives interactively using large language models.


## Features
- **Template-Based Story Initiation**  
  Choose from pre-built templates like Sci-Fi or Future Fantasy to kickstart your story with a powerful opening paragraph.

- **Interactive Prompt Buttons**  
  Dynamically loaded actions like:
  - 📝 Continue Story
  - ✂️ Condense
  - 🎭 Add a Twist
  - 💬 Inner Monologue
  - 🔁 Reframe  
  Each prompt transforms the story with a click using LLM-generated completions.

- **Editable Story Area**  
  The evolving story appears in a rich text box for editing and further expansion.

- **Modular Prompt System**  
  Prompts are defined via JSON with custom templates and behaviors (`append`, `replace`, etc.), enabling easy extension.


## Powered By
- [Streamlit](https://streamlit.io/) – Fast web UI for ML apps  
- [Ollama](https://ollama.com/) – Local LLM runner  
- [Mistral](https://mistral.ai/) – Lightweight transformer model used for story generation  


## Setup Instructions
1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/llm-story-cowriter.git
   cd llm-story-cowriter

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Launch Ollama with Mistral**
   ```bash
   ollama run mistral

4. **Run Streamlit app**
   ```bash
   streamlit run app.py