import os
import argparse
from yololibs import readjson
from PIL import Image, ImageFont, ImageDraw, ImageEnhance


def boxImg(img, objects, out_dir):
    color_code = {'D00': [(0, 247, 255),'black'],
                  'D10': [(191, 255, 0),'black'],
                  'D20': [(255, 181, 43),'black'],
                  'D40': [(196, 0, 0),'white']}
    
    source_img = Image.open(img).convert("RGB")

    for obj in objects:
        # change coordinates from yolo input to what PIL accepts
        shape_raw = list(obj['relative_coordinates'].values())
        dims = source_img.size
        shape = [int((shape_raw[0] - shape_raw[2] / 2) * dims[0]),
                int((shape_raw[1] - shape_raw[3] / 2) * dims[1]),
                int((shape_raw[0] + shape_raw[2] / 2) * dims[0]),
                int((shape_raw[1] + shape_raw[3] / 2) * dims[1])]
        
        # draw box
        name = obj['name']
        color = color_code[name]
        box = ImageDraw.Draw(source_img)
        box.line([shape[0], shape[1], shape[2], shape[1]], fill=color[0], width=3)
        box.line([shape[0], shape[1], shape[0], shape[3]], fill=color[0], width=3)
        box.line([shape[2], shape[1], shape[2], shape[3]], fill=color[0], width=3)
        box.line([shape[0], shape[3], shape[2], shape[3]], fill=color[0], width=3)

        # set text label
        confidence = str(round(obj['confidence'] * 100)) + '%'
        font = ImageFont.load_default()
        text = name + ' (' + confidence + ')'

        # get text size
        text_size = font.getsize(text)

        # set button size + 10px margins
        button_size = (text_size[0]+5, text_size[1]+5)

        # create image with correct size and black background
        button_img = Image.new('RGB', button_size, color[0])

        # put text on button with 10px margins
        button_draw = ImageDraw.Draw(button_img)
        button_draw.text((2.5, 2.5), text, font=font, fill=color[1])

        # put button on source image in position (0, 0)
        source_img.paste(button_img, (int(shape[0]), int(shape[1] - 15)))

    # save in new file
    source_img.save(os.path.join(out_dir, os.path.split(img)[1]), "JPEG")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", "--json_file", help="json file with predictions", type=str, required=True)
    parser.add_argument("-out", "--output_dir", help="output directory", type=str)
    args = parser.parse_args()
    json_file = args.json_file
    output_dir = args.output_dir
    
    json_file = readjson(json_file)
    os.mkdir(output_dir)
    for element in json_file:
        boxImg(element['filename'], element['objects'], output_dir)