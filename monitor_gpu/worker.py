""" Endpoint for GPU status. """
from flask import Flask
from flask import jsonify
import gpustat


app = Flask(__name__)


@app.route("/")
def main():
    stats = gpustat.new_query()
    cpu_usage = >>> x = commands.getstatusoutput(
        "grep 'cpu ' /proc/stat | awk '{{usage=($2+$4)*100/($2+$4+$5)}} END {{print usage \"%\"}}'")[0]

    data_json = jsonify(stat.jsonify())
    data_json["cpu.usage"] = cpu_usage
    return data_json


if __name__ == "__main__":
    app.run(host="0.0.0.0")
