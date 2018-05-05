""" Endpoint for monitoring GPU clusters status. """
from flask import Flask
import gpustat
import requests

from ansi2html import ansi2html


app = Flask(__name__)

MACHINES = [
    "",
]

REFRESH_RATE = 10

@app.route("/")
def main():
    page = "<html>"
    page += "<head>"
    page += "<meta http-equiv=\"refresh\" content=\"{}\">".format(REFRESH_RATE)
    page += "</head>"
    page += "<body>"

    cluster_stats = []
    time_logged = False
    for machine_index, machine in enumerate(MACHINES):
        try:
            machine_stats = requests.get(machine).json()
        except:
            continue

        if not time_logged:
            time_logged = True
            page += "{} (Refreshed every {}s)</br></br>".format(machine_stats["query_time"], REFRESH_RATE)

        page += "{} (CPU Usage: {})</br>".format(machine_stats["hostname"], machine_stats["cpu.usage"])

        for gpu in machine_stats["gpus"]:
            page += "{}</br>".format(ansi2html(str(gpustat.GPUStat(gpu))))
            
        page += "</br>"
        
    page += "</body>"
    page += "</html>"

    print("Done.")
    return page.replace("(B", '')


if __name__ == "__main__":
    app.run(host="0.0.0.0")
            
