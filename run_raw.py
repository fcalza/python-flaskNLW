from flask import Flask, request, jsonify
from barcode import Code128
from barcode.writer import ImageWriter

app = Flask(__name__)


@app.route('/create_tag', methods=['POST'])
def create_tag():
    data = request.get_json()
    print(data)
    product_code = data['product_code']
    tag=Code128(product_code, writer=ImageWriter())
    path_from_tag = f"{tag}"
    tag.save(path_from_tag)
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)