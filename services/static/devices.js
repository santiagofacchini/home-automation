const Http = new XMLHttpRequest()
const hue_ip = '192.168.88.105'
const hue_user = 'YtR6H-GYX4YCGbqAD3bpzOu-lF5tYFMInpl114sa'
const sala_id = '5'
const comedor_id = '1'
const dormitorio_id = '3'
const sala_endpoint = 'http://192.168.88.109:4000/lights/sala-de-estar'
const comedor_endpoint = 'http://192.168.88.109:4000/lights/comedor'
const dormitorio_endpoint = 'http://192.168.88.109:4000/lights/dormitorio'
const sprinklers_ip = '192.168.88.254'
const sprinklers_port = '8081'
const sprinklers_endpoint = 'http://192.168.88.109:4000/sprinklers'
const sprinklers_id = '4'

function get_all_states() {
    ['1', '3', '5'].forEach(id => {
        fetch('http://' + hue_ip + '/api/' + hue_user + '/lights/' + id)
            .then((response) => response.json())
            .finally((data) => {
                if (data['state']['on'] == true) {
                    document.getElementById(id).style.setProperty("color", "#f4af36")
                } else {
                    document.getElementById(id).style.setProperty("color", "#898d95")
                }
            }) 
        })
    fetch("http://192.168.88.109:4000/sprinklers/get-state")
        .then((response) => response.json())
	    .then((data) => {
            if (data["data"]["switch"] == "on") {
	            document.getElementById(sprinklers_id).style.setProperty("color", "#f4af36")
	        } else {
                document.getElementById(sprinklers_id).style.setProperty("color", "#898d95")
	        }
	    })
};

function sala() {
    fetch('http://' + hue_ip + '/api/' + hue_user + '/lights/' + sala_id)
        .then((response) => response.json())
        .then((data) => {
            if (data['state']['on'] == false) {
                document.getElementById(sala_id).style.setProperty("color", "#f4af36")
                Http.open("GET", sala_endpoint)
                Http.send()
                console.log(Http.response)
            } else {
                document.getElementById(sala_id).style.setProperty("color", "#898d95")
                Http.open("GET", sala_endpoint)
                Http.send()
                console.log(Http.response)
            }
        })
};

function comedor() {
    fetch('http://' + hue_ip + '/api/' + hue_user + '/lights/' + comedor_id)
        .then((response) => response.json())
        .then((data) => {
            if (data['state']['on'] == false) {
                document.getElementById(comedor_id).style.setProperty("color", "#f4af36")
                Http.open("GET", comedor_endpoint)
                Http.send()
                console.log(Http.response)
            } else {
                document.getElementById(comedor_id).style.setProperty("color", "#898d95")
                Http.open("GET", comedor_endpoint)
                Http.send()
                console.log(Http.response)
            }
        })
};

function dormitorio() {
    fetch('http://' + hue_ip + '/api/' + hue_user + '/lights/' + dormitorio_id)
        .then((response) => response.json())
        .then((data) => {
            if (data['state']['on'] == false) {
                document.getElementById(dormitorio_id).style.setProperty("color", "#f4af36")
                Http.open("GET", dormitorio_endpoint)
                Http.send()
                console.log(Http.response)
            } else {
                document.getElementById(dormitorio_id).style.setProperty("color", "#898d95")
                Http.open("GET", dormitorio_endpoint)
                Http.send()
                console.log(Http.response)
            }
        })
};

function aspersores() {
    fetch(sprinklers_endpoint)
        .then((response) => response.json())
        .then((data) => {
            if (data['data']['switch'] == 'off') {
                document.getElementById(sprinklers_id).style.setProperty("color", "#898d95")
            } else {
                 document.getElementById(sprinklers_id).style.setProperty("color", "#f4af36")
            }
         })
};

function all_on() {
    Http.open("GET", "http://192.168.88.109:4000/lights/all-on")
    Http.send()
    console.log(Http.response)
    ['1', '3', '5'].forEach(id => {
        fetch('http://' + hue_ip + '/api/' + hue_user + '/lights/' + id)
            .then((response) => response.json())
            .finally((data) => {
                if (data['state']['on'] == true) {
                    document.getElementById(id).style.setProperty("color", "#898d95")
                } else {
                    document.getElementById(id).style.setProperty("color", "#f4af36")
                }
            }) 
        })
};

function all_off() {
    Http.open("GET", "http://192.168.88.109:4000/lights/all-off")
    Http.send()
    console.log(Http.response)
    ['1', '3', '5'].forEach(id => {
        fetch('http://' + hue_ip + '/api/' + hue_user + '/lights/' + id)
            .then((response) => response.json())
            .finally((data) => {
                if (data['state']['on'] == true) {
                    document.getElementById(id).style.setProperty("color", "#898d95")
                } else {
                    document.getElementById(id).style.setProperty("color", "#f4af36")
                }
            }) 
        })
};
