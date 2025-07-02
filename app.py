import gradio as gr
from pdf_parser import extract_text_from_pdf
from llm_chat import query_llm_with_context

pdf_context = ""

def handle_upload(pdf_file):
    global pdf_context
    if not pdf_file:
        return "❌ Please upload a PDF first."
    pdf_context = extract_text_from_pdf(pdf_file)
    return "✅ PDF uploaded and processed. You can now ask questions."

def handle_question(user_input):
    if not pdf_context:
        return "📄 Upload a PDF first."
    if not user_input.strip():
        return "❓ Please enter a question."
    return query_llm_with_context(pdf_context, user_input)

with gr.Blocks(title="PDF Summary Chatbot") as demo:
    gr.Markdown("## 📄 PDF Summary Chatbot (Local AI)")
    with gr.Row():
        pdf_input = gr.File(label="Upload PDF", type="binary")
        upload_btn = gr.Button("Process PDF")
    upload_status = gr.Textbox(label="Status", interactive=False)

    question_input = gr.Textbox(label="Ask something about the PDF")
    answer_output = gr.Textbox(label="AI Response", lines=6)

    upload_btn.click(handle_upload, inputs=[pdf_input], outputs=[upload_status])
    question_input.submit(handle_question, inputs=[question_input], outputs=[answer_output])

demo.launch()
