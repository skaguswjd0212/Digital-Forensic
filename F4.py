from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze_file():
    file = request.files['file']
    file_extension = file.filename.rsplit('.', 1)[1].lower()

    if file_extension in ['jpg', 'pdf', 'wav', 'zip']:
        analysis_result = analyze_file_4(file, file_extension)
    elif file_extension in ['png', 'docx', 'pptx', 'mp4', 'hwp']:
        analysis_result = analyze_file_8(file, file_extension)
    elif file_extension in ['gif']:
        analysis_result = analyze_file_6(file, file_extension)
    elif file_extension in ['exe']:
        analysis_result = analyze_file_2(file, file_extension)
    elif file_extension in ['mp3']:
        analysis_result = analyze_file_3(file, file_extension)
    else:
        analysis_result = "Unsupported file type."
    return render_template('result.html', result=analysis_result)


def analyze_file_4(file, file_extension):
    # 파일 시그니처 길이가 4바이트
    header_signature = file.read(4)
    # .jpg
    if (file_extension == 'jpg') and (header_signature == b'\xFF\xD8\xFF\xE0' or b'\xFF\xD8\xFF\xE8'):
        result = "헤더 시그니처와 확장자 헤더 시그니처가 같습니다."
    # .pdf
    elif (file_extension == 'pdf') and (header_signature == b'\x25\x50\x44\x46'):
        result = "헤더 시그니처와 확장자 헤더 시그니처가 같습니다."
    # .wav
    elif (file_extension == 'wav') and (header_signature == b'\x52\x49\x46\x46'):
        result = "헤더 시그니처와 확장자 헤더 시그니처가 같습니다."
    # zip
    elif (file_extension == 'zip') and (header_signature == b'\x50\x4B\x03\x04'):
        result = "헤더 시그니처와 확장자 헤더 시그니처가 같습니다."

    else:
        result = "헤더 시그니처와 확장자 헤더 시그니처가 다릅니다."
    return result


def analyze_file_8(file, file_extension):
    #파일 시그니처 길이가 8바이트
    header_signature = file.read(8)
    # .mp4
    if (file_extension == 'mp4') and (header_signature == b'\x00\x00\x00\x18\x66\x74\x79\x70'):
        result = "헤더 시그니처와 확장자 헤더 시그니처가 같습니다."
    # .png
    elif (file_extension == 'png') and (header_signature == b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'):
        result = "헤더 시그니처와 확장자 헤더 시그니처가 같습니다."
    # .pptx
    elif (file_extension == 'pptx') and (header_signature == b'\x50\x4B\x03\x04\x14\x00\x06\x00'):
        result = "헤더 시그니처와 확장자 헤더 시그니처가 같습니다."
    # .hwp
    elif (file_extension == 'hwp') and (header_signature == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1'):
        result = "헤더 시그니처와 확장자 헤더 시그니처가 같습니다."
    # .docx
    elif (file_extension == 'docx') and (header_signature == b'\x50\x4B\x03\x04\x14\x00\x06\x00'):
        result = "헤더 시그니처와 확장자 헤더 시그니처가 같습니다."
    else:
        result = "헤더 시그니처와 확장자 헤더 시그니처가 다릅니다."
    return result


def analyze_file_6(file, file_extension):
    # 파일 시그니처 길이가 6바이트
    header_signature = file.read(6)
    # .gif
    if (file_extension == 'gif') and (header_signature == b'\x47\x49\x46\x38\x37\x61' or b'\x47\x49\x46\x38\x39\x61'):
        result = "헤더 시그니처와 확장자 헤더 시그니처가 같습니다."
    else:
        result = "헤더 시그니처와 확장자 헤더 시그니처가 다릅니다."
    return result


def analyze_file_2(file, file_extension):
    # 파일 시그니처 길이가 2바이트
    header_signature = file.read(2)
    # .exe
    if (file_extension == 'exe') and (header_signature == b'\x4D\x5A'):
        result = "헤더 시그니처와 확장자 헤더 시그니처가 같습니다."
    else:
        result = "헤더 시그니처와 확장자 헤더 시그니처가 다릅니다."
    return result


def analyze_file_3(file, file_extension):
    # 파일 시그니처 길이가 3바이트
    header_signature = file.read(3)
    # .mp3
    if (file_extension == 'mp3') and (header_signature == b'\x49\x44\x33'):
        result = "헤더 시그니처와 확장자 헤더 시그니처가 같습니다."
    else:
        result = "헤더 시그니처와 확장자 헤더 시그니처가 다릅니다."
    return result


if __name__ == '__main__':
    app.run()
