import librosa
import librosa.display
import argparse
import cv2



def get_audio_data(pathname):
    audio_data, sr = librosa.load(pathname)
    return audio_data


def audio_to_melspectrogram( audio):
    spectrogram = librosa.feature.melspectrogram(y=audio)
    return spectrogram


def read_as_melspectrogram( pathname):
    audio_data = get_audio_data( pathname)
    melspectrogram = audio_to_melspectrogram( audio_data)
    return melspectrogram


def rename_file(img_name):
    img_name = img_name.split("/")[-1]
    img_name = img_name.split(".")[0]
    img_name += ".png"
    return img_name


def save_image_from_sound(sound_path,output=""):
    output = output.strip()
    if output:
        filename = output
    else:
        filename = rename_file(sound_path)
    x = read_as_melspectrogram(sound_path)
    cv2.imwrite(filename, x)
    return x

sound_to_image = save_image_from_sound

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, default="",  help="input sound file path")
    parser.add_argument("--output", type=str, default="",  help="output image file path")
    args = parser.parse_args()

    save_image_from_sound(args.input,output=args.output)

