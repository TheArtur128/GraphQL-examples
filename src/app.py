from flask import Flask, request, jsonify

from schemes import product_schema, convert_execution_result_to_dict


app = Flask(__name__)


@app.route("/api/products", methods=('POST', ))
def product_endpoint():
    return jsonify(convert_execution_result_to_dict(product_schema.execute(request.json["query"])))

if __name__ == "__main__":
    app.run(port='8000')