import gradio as gr
from evo_ukiyoe_v1 import load_evo_ukiyoe
from datetime import datetime  # 追加

# Pipeをロード
pipe = load_evo_ukiyoe(device="cpu")

# 画像生成の関数
def generate_image(prompt):
    # 現在の時刻をフォーマットしてファイル名に利用
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    images = pipe(prompt + " 輻の浮世絵。超詳細。", negative_prompt='', guidance_scale=8.0, num_inference_steps=40).images
    images[0].save(f"image_{timestamp}.png")  # 時刻のファイル名で保存
    return images[0]

# Gradio インターフェース
with gr.Blocks(css=f"""
    body {{
        background-color: black;
        background-size: cover;
        background-repeat: no-repeat;
        color: white;
    }}
    """) as demo:
    
    # テキストとボタンのデザイン調整
    gr.Markdown("<h1 style='color: white; text-align: center;'>浮世絵生成器</h1>")
    
    # 入力フィールド
    prompt_input = gr.Textbox(label="プロンプト", value="着物を着ている猫が庭でお茶を飲んでいる。", elem_id="prompt_input")
    
    # 画像表示
    image_output = gr.Image(label="生成された画像", elem_id="image_output")
    
    # ボタンと出力設定
    generate_button = gr.Button("画像を生成", elem_id="generate_button")
    
    # ボタンが押されたときに generate_image 関数を実行
    generate_button.click(fn=generate_image, inputs=prompt_input, outputs=image_output)

# アプリケーションをポート7860で実行
demo.launch(server_port=7860)

