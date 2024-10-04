SakanaAI/Evo-UkiyoeをPythonで動かす方法
================================

間違いなどがあったら指摘していただけるとうれしいです。質問もお待ちしています。

## YouTube
[![](https://img.youtube.com/vi/FIdQXpeo-2Q/0.jpg)](https://www.youtube.com/watch?v=FIdQXpeo-2Q)

環境整備コマンド
--------

1:インストールとDL

[Git](https://gitforwindows.org/) [Python](https://www.python.org/) [VSCode](https://code.visualstudio.com/) [huggingface](https://huggingface.co/SakanaAI/Evo-Ukiyoe-v1)

2:gitからクローン


    git clone https://huggingface.co/SakanaAI/Evo-Ukiyoe-v1

3:移動


    cd Evo-Ukiyoe-v1

4:venvを準備


    python -m venv venv

    .\venv\Scripts\activate

5:ライブラリをインストール


    pip install -r requirements.txt

プログラム
-----
HuggingFaceのアクセストークンが必要です


app.py


    from evo_ukiyoe_v1 import load_evo_ukiyoe
    prompt = "着物を着ている猫が庭でお茶を飲んでいる。"
    pipe = load_evo_ukiyoe(device="cuda")
    images = pipe(prompt + "輻の浮世絵。超詳細。", negative_prompt='', guidance_scale=8.0, num_inference_steps=40).images
    images[0].save("image.png")
    

[Download](./app.py)

evo\_ukiyoe\_v1.py

[Download](./evo_ukiyoe_v1.py)

Web.py

[Download](./Web.py)

実行コマンド
------

app.pyを実行


    python ./run.py

Web.pyを実行


    python ./Web.py

