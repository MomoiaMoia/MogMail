from PIL import Image, ImageDraw, ImageFont

import configparser

props = configparser.ConfigParser()
props.read("pymail.conf", encoding="utf-8")

# 打开图片
im = Image.open("resources/background-total.png")
draw = ImageDraw.Draw(im)

# 设置字体
font = ImageFont.truetype("resources/HanYiQiHei-55Jian-Regular-2.ttf", 32)

# 分割文本段与换行
lines = props.get("pymail", "content").split("<br>")
draw_lines = []
for line in lines:
    if len(line) < 29:
        draw_lines.append(line)
    else:
        results = [line[i:i+29] for i in range(0, len(line), 29)]
        for res in results:
            draw_lines.append(res)

# 计算宽度
text_width = draw.textlength(props.get("pymail", "id"), font=font)

# DRAW
content_y = 230
for line in draw_lines:
    draw.text((250,content_y), line, font=font, fill=(0, 0, 0))
    content_y += 50
draw.text((1406-190-text_width,910), props.get("pymail", "id"), font=font, fill=(0, 0, 0))

im.save("outputs/output.png")
print(" * 生成成功！图片存储在outputs目录下。")
input(" * 按任意键退出...")