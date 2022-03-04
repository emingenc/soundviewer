import librosa
import cv2
import numpy as np
import argparse
import soundfile


def rename_file(img_name):
    img_name = img_name.split("/")[-1]
    img_name = img_name.split(".")[0]
    img_name += ".wav"
    return img_name


def image_to_sound(image_path, output = ''):

        m=cv2.imread(image_path,0)
        img=m.astype(np.float64)
        output = output.strip()
        if output:
            filename = output
        else:
            filename = rename_file(image_path)
        sound=librosa.feature.inverse.mel_to_audio(img,)
        soundfile.write(filename,sound,samplerate=22050)
        return filename , sound



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="",  help="input sound file path")
    parser.add_argument("--output", type=str, default="",  help="output image file path")
    args = parser.parse_args()

    image_to_sound(args.input, args.output)
