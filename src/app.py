from flask import Flask, request, jsonify

from schemes import product_schema, convert_execution_result_to_dict


app = Flask(__name__)


if __name__ == "__main__":
    app.run(port='8000')