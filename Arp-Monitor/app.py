from flask import Flask, jsonify, render_template_string
import json

app = Flask(__name__)

def load():
    try:
        with open("data.json","r") as f:
            return json.load(f)
    except:
        return []

@app.route("/")
def home():
    return render_template_string("""
<!DOCTYPE html>
<html>
<head>
<title>Network Monitor</title>

<style>
body {
    background: #0d1117;
    color: #c9d1d9;
    font-family: Arial;
    margin: 20px;
}

h1 {
    text-align: center;
    color: #58a6ff;
}

h2 {
    border-bottom: 1px solid #30363d;
    padding-bottom: 5px;
}

#alerts div {
    background: #2d0f0f;
    border-left: 5px solid red;
    padding: 8px;
    margin: 5px 0;
    border-radius: 6px;
    font-weight: bold;
}

#devices div {
    background: #161b22;
    border-left: 5px solid #00ff99;
    padding: 8px;
    margin: 5px 0;
    border-radius: 6px;
}

#logs {
    max-height: 250px;
    overflow-y: scroll;
    background: #0d1117;
    padding: 10px;
    border: 1px solid #30363d;
    border-radius: 6px;
}
</style>

</head>

<body>

<h1>🛡 NETWORK MONITOR</h1>

<h2>🚨 Tehditler</h2>
<div id="alerts"></div>

<h2>📡 Bağlı Cihazlar</h2>
<div id="devices"></div>

<h2>📜 Canlı Log Akışı</h2>
<div id="logs"></div>

<script>
async function update(){
    let res = await fetch("/data?x=" + Date.now());
    let data = await res.json();

    // ALERTS
    document.getElementById("alerts").innerHTML =
        data.filter(x=>x.type==="ALERT")
        .map(x=>`<div>⚠️ ${x.message}</div>`).join("");

    // DEVICES (DUPLICATE FIX)
    let deviceMap = {};

    data.filter(x => x.type === "DISCOVERY").forEach(x => {
        x.devices.forEach(d => {
            deviceMap[d.ip] = d.mac;
        });
    });

    let deviceList = Object.entries(deviceMap);

    document.getElementById("devices").innerHTML =
        deviceList.map(d => `
            <div>
                📡 IP: <b>${d[0]}</b><br>
                🧷 MAC: ${d[1]}
            </div>
        `).join("");

    // LOGS
    document.getElementById("logs").innerHTML =
        data.filter(x=>x.type==="LOG")
        .map(x=>"• "+x.message).join("<br>");
}

setInterval(update, 1000);
update();
</script>

</body>
</html>
""")

@app.route("/data")
def data():
    return jsonify(load())

app.run(debug=True, port=5000)
