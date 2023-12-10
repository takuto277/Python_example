## Google Colab + DiffusersライブラリでAI画像を生成

# 1.確認とライブラリインストール
!nvidia-smi
!pip install diffusers==0.12.1 transformers==4.19.2 ftfy accelerate


# 2.実行
import torch
from diffusers import StableDiffusionPipeline

# model_id = "CompVis/stable-diffusion-v1-4"
# model_id = "CompVis/stable-diffusion-v1-2"
model_id = "stabilityai/stable-diffusion-2-1-base"
device = "cuda"

# プロンプト
prompt = "the girl eat pizza"

# パイプラインの作成
pipe = StableDiffusionPipeline.from_pretrained(model_id, revision="fp16", torch_dtype=torch.float16)
pipe = pipe.to(device)

# パイプラインの実行
generator = torch.Generator(device).manual_seed(42) # seedを前回と同じ42にする
with torch.autocast("cuda"):
    image = pipe(prompt, guidance_scale=7.5, generator=generator).images[0]  

# 生成した画像の保存
image.save("the_girl_pizza_v2-1-base.png")

# import torch
# from diffusers import StableDiffusionPipeline
# import matplotlib.pyplot as plt

# def generate_image():
#     # モデルの読み込み
#     model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")

#     # 画像生成のための初期設定
#     batch_size = 1  # 生成する画像の数
#     image_shape = (3, 256, 256)  # 生成する画像の形状（RGBイメージ）

#     # ランダムなノイズを作成
#     noise = torch.randn(batch_size, *image_shape)

#     # ノイズを用いて画像生成
#     generated_images = model.generate_images(noise)

#     return generated_images

# # 画像生成の実行
# generated_images = generate_image()

# # 生成された画像の表示
# plt.imshow(generated_images[0].permute(1, 2, 0).cpu().numpy())
# plt.axis('off')
# plt.show()