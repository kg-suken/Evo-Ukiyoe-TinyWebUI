from evo_ukiyoe_v1 import load_evo_ukiyoe
prompt = "城下町"
pipe = load_evo_ukiyoe(device="cpu")
images = pipe(prompt + "輻の浮世絵。超詳細。", negative_prompt='', guidance_scale=8.0, num_inference_steps=40).images
images[0].save("image.png")