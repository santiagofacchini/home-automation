const Http = new XMLHttpRequest();
const hue_ip = '192.168.88.105'
const hue_user = 'YtR6H-GYX4YCGbqAD3bpzOu-lF5tYFMInpl114sa'
const sala_id = '5'
const comedor_id = '1'
const dormitorio_id = '3'
const sala_endpoint = 'http://192.168.88.109:4000/lights/sala-de-estar'
const comedor_endpoint = 'http://192.168.88.109:4000/lights/comedor'
const dormitorio_endpoint = 'http://192.168.88.109:4000/lights/dormitorio'

function sala() {
    fetch('http://' + hue_ip + '/api/' + hue_user + '/lights/' + sala_id)
        .then((response) => response.json())
        .then((data) => {
            if (data['state']['on'] == false) {
                document.getElementById(sala_id).style.setProperty("color", "#f4af36")
                Http.open("GET", sala_endpoint)
                Http.send()
            } else {
                document.getElementById(sala_id).style.setProperty("color", "#898d95")
                Http.open("GET", sala_endpoint)
                Http.send()
            }
        });
}

function comedor() {
    fetch('http://' + hue_ip + '/api/' + hue_user + '/lights/' + comedor_id)
        .then((response) => response.json())
        .then((data) => {
            if (data['state']['on'] == false) {
                document.getElementById(comedor_id).style.setProperty("color", "#f4af36")
                Http.open("GET", comedor_endpoint)
                Http.send()
            } else {
                document.getElementById(comedor_id).style.setProperty("color", "#898d95")
                Http.open("GET", comedor_endpoint)
                Http.send()
            }
        });
}

function dormitorio() {
    fetch('http://' + hue_ip + '/api/' + hue_user + '/lights/' + dormitorio_id)
        .then((response) => response.json())
        .then((data) => {
            if (data['state']['on'] == false) {
                document.getElementById(dormitorio_id).style.setProperty("color", "#f4af36")
                Http.open("GET", dormitorio_endpoint)
                Http.send()
            } else {
                document.getElementById(dormitorio_id).style.setProperty("color", "#898d95")
                Http.open("GET", dormitorio_endpoint)
                Http.send()
            }
        });
}
