# ライブラリーのインポート
from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt
import re

def main():
    # アクセストークンの設定
    access_tokens="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" # @param {type:"string"}

    prompt = "Tokyo Sky Tree by Marc Chagall"
    print("🌱1")
    
    # モデルのインスタンス化
    model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=access_tokens)
    model.to("cuda")
    print("🌱2")

    # 画像のファイル名
    filename = re.sub(r'[\\/:*?"<>|,]+', '', prompt).replace(' ','_')
    print("🌱3")

    # 画像数
    num = 1
    
    for i in range(num):
        # モデルにpromptを入力し画像生成
        image = model(prompt,num_inference_steps=50)["sample"][0]
        # 保存
        outputfile = f'{filename} _{i:02} .png'
        image.save(f"outputfile/{outputfile}")
        print("🌱4")
    for i in range(num):
        outputfile = f'{filename} _{i:02} .png'
        plt.imshow(plt.imread(f"outputfile/{outputfile}"))
        plt.axis('off')
        print("🌱5")

if __name__ == '__main__':
    main()