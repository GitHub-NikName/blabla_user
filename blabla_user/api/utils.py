from django.core.files import File
from pydub import AudioSegment


def convert_to_mp3(audio_file, content_type='audio/mpeg'):
    mp3_converted_file = AudioSegment.from_wav(audio_file)
    new_path = audio_file.name[:-3] + 'mp3'
    mp3_converted_file.export(new_path, bitrate="192k")
    converted_audiofile = File(
        file=open(new_path, 'rb'),
    )
    converted_audiofile.content_type = content_type
    return converted_audiofile
