import gradio as gr
from brochure_generator import generate_brochure

def generate_brochure_gradio(company_name, url):
    return generate_brochure(company_name, url)

with gr.Blocks() as app:
    gr.Markdown("# Company Brochure Generator")

    company_name = gr.Textbox(label="Company Name")
    company_url = gr.Textbox(label="Company URL")
    output = gr.Markdown(label="Generated Brochure")

    generate_button = gr.Button("Generate Brochure")
    generate_button.click(generate_brochure_gradio, inputs=[company_name, company_url], outputs=output)

app.launch()