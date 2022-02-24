$(document).ready(function () {
    GetData();
    // Play_audio();
    // load_and_play()
    // get_audio_play()
    $('#alert_btn').click(function () {
        // Play_audio()
        load_and_play()
        // alert()
    })
    // $('#alert_btn').trigger('click')
    // playSound()
    skhst_cheers()

});

function Play_audio() {
    $("#alert_audio").get(0).play();
}

function load_and_play() {
    // var audio = new Audio('./sound.mp3');
    var audio = new Audio
    audio.src = './sound.mp3';
    // when the sound has been loaded, execute your code
    audio.oncanplaythrough = (event) => {
        var playedPromise = audio.play();
        if (playedPromise) {
            playedPromise.catch((e) => {
                console.log(e)
                if (e.name === 'NotAllowedError' || e.name === 'NotSupportedError') {
                    console.log(e.name);
                }
            }).then(() => {
                console.log("playing sound !!!");
            });
        }
    }
}
function GetData() {
    var url = 'https://api.thingspeak.com/channels/1361501/feeds.json?key=QPZGNFSI8520A5CZ&results=1';
    $.ajax
        ({
            url: url,
            type: 'GET',
            contentType: "application/json",
            //dataType: "json",
            //crossDomain: true,
            success: function (data, textStatus, xhr) {
                $.each(data, function (i, item) {
                    if (i == 'feeds') {
                        var ubound = item.length;
                        var temperature = item[ubound - 1].field1
                        var humidity = item[ubound - 1].field2
                        $('#txtField1').text(temperature);
                    }
                });
            },
            error: function (xhr, textStatus, errorThrown) {
                alert(errorThrown);
            }
        });

    setTimeout(GetData, 10000);
}


function loadSound() {
    createjs.Sound.registerSound("assets/thunder.mp3", 18);
}

function playSound() {
    createjs.Sound.play(18);
}

function skhst_cheers() {
    var url = 'https://badasstechie.github.io/Clips/Siren.mp3';
    window.AudioContext = window.AudioContext || window.webkitAudioContext; //fix up prefixing
    var context = new AudioContext(); //context
    var source = context.createBufferSource(); //source node
    source.connect(context.destination); //connect source to speakers so we can hear it
    var request = new XMLHttpRequest();
    request.open('GET', url, true);
    request.responseType = 'arraybuffer'; //the  response is an array of bits
    request.onload = function () {
        context.decodeAudioData(request.response, function (response) {
            source.buffer = response;
            source.start(0); //play audio immediately
            source.loop = true;
        }, function () { console.error('The request failed.'); });
    }
    request.send();
}