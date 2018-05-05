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
        "op -b -n2 -p 1 | fgrep \"Cpu(s)\" | tail -1 | awk -F'id,' -v prefix=\"$prefix\" '{{ split($1, vs, \",\"); v=vs[length(vs)]; sub(\"%\", \"\", v); printf \"%s%.1f%%\n\", prefix, 100 - v }}'")[1]

    data_json = stats.jsonify()
    data_json["cpu.usage"] = cpu_usage
    data_json = jsonify(data_json)
    return data_json


if __name__ == "__main__":
    app.run(host="0.0.0.0")
