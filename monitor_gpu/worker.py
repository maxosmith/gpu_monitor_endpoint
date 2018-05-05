""" Endpoint for GPU status. """
import commands

from flask import Flask
from flask import jsonify
import gpustat


app = Flask(__name__)


@app.route("/")
def main():
    stats = gpustat.new_query()
    cpu_usage = commands.getstatusoutput(
        "grep 'cpu ' /proc/stat | awk '{{usage=($2+$4)*100/($2+$4+$5)}} END {{print usage \"%\"}}'")[1]

    data_json = stats.jsonify()
    data_json["cpu.usage"] = cpu_usage
    data_json = jsonify(data_json)
    return data_json


if __name__ == "__main__":
    app.run(host="0.0.0.0")
