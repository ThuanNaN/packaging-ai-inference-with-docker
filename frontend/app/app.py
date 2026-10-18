import gradio as gr
from api.ocr import ocr_api

def refresh():
    return None, "Ready", None

with gr.Blocks(title="OCR") as demo:
    gr.Markdown("# OCR\nThis is a OCR application")
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(type="filepath", label="Input Image")
            with gr.Row():
                run_btn = gr.Button("Run OCR", variant="primary")
                refresh_btn = gr.Button("Refresh")
        with gr.Column():
            status = gr.Text(label="Status", value="Ready", interactive=False)
            output_image = gr.Image(label="Output Image")

    run_btn.click(ocr_api, inputs=input_image, outputs=[status, output_image])
    refresh_btn.click(refresh, outputs=[input_image, status, output_image])

demo.launch(
    server_name="0.0.0.0",
    server_port=3000,
    share=False
)
