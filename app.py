# from rembg import remove
# from PIL import Image

# # Загрузка изображения
# input_path = 'input.png'
# output_path = 'result.png'

# input_image = Image.open(input_path)

# # Удаление фона
# output_image = remove(input_image)

# # Сохранение результата
# output_image.save(output_path)



# from flask import Flask, request, send_file, jsonify
# from flask_cors import CORS
# from rembg import remove
# from PIL import Image
# import io

# app = Flask(__name__)
# CORS(app, origins=["http://localhost:5173"])  # Разрешить запросы с Vite

# @app.route('/')
# def index():
#     return 'Background Removal API is running!'

# @app.route('/remove-bg', methods=['POST'])
# def remove_bg():
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image provided'}), 400

#     image_file = request.files['image']
#     input_image = Image.open(image_file.stream).convert("RGBA")
    
#     # Remove background
#     output_image = remove(input_image)

#     # Save to in-memory file
#     byte_io = io.BytesIO()
#     output_image.save(byte_io, 'PNG')
#     byte_io.seek(0)

#     return send_file(byte_io, mimetype='image/png')

# if __name__ == '__main__':
#     app.run(debug=True)




from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from rembg import remove
from PIL import Image
import io

app = Flask(__name__)
CORS(app, origins=["http://localhost:5173"])  # Разрешить запросы с Vite

@app.route('/')
def index():
    return 'Background Removal API is running!'

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    input_image = Image.open(image_file.stream).convert("RGBA")
    
    # Убираем фон с использованием модели isnet-general-use
    output_image = remove(input_image, model_name='isnet-general-use')

    # Сохраняем результат в памяти
    byte_io = io.BytesIO()
    output_image.save(byte_io, 'PNG')
    byte_io.seek(0)

    return send_file(byte_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
