from django.core.files import File
from pydub import AudioSegment
from django.core.files.uploadedfile import InMemoryUploadedFile


def convert_to_mp3(audio_file: InMemoryUploadedFile, content_type='audio/mpeg') -> File:
    mp3_converted_file = AudioSegment.from_wav(audio_file)
    new_path = audio_file.name[:-3] + 'mp3'
    mp3_converted_file.export(new_path, bitrate="192k")
    converted_audiofile = File(
        file=open(new_path, 'rb'),
    )
    converted_audiofile.content_type = content_type
    return converted_audiofile
