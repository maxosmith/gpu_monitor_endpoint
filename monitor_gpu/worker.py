""" Endpoint for GPU status. """
import commands

from flask import Flask
from flask import jsonify
import gpustat


app = Flask(__name__)


@app.route("/")
def main():
    stats = gpustat.new_query()
    cpu_usage = commands.getstatusoutput("top -b -n 2 | grep %Cpu | sed -n 2p | awk -F',' '{{print $4}}'")[1]
    cpu_usage = 100 - float(cpu_usage.split(' ')[1])
    cpu_usage = "{}%".format(cpu_usage)
    
    data_json = stats.jsonify()
    data_json["cpu.usage"] = cpu_usage
    data_json = jsonify(data_json)
    return data_json


if __name__ == "__main__":
    app.run(host="0.0.0.0")
