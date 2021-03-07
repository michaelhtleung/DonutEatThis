

window.onload = function() {
    let imageCapture = document.getElementById("capture_image");
    let imageUpload = document.getElementById("upload_image");
    
    // const axios = require('axios');
    console.log('loaded.');

    imageCapture.onchange = function() {
        console.log('onchange');
        document.getElementById("form").submit();
        console.log('image taken');
        // send_axios();
    };
    imageUpload.onchange = function() {
        console.log('onchange');
        document.getElementById("form").submit();
        console.log('image received');
        // send_axios();
    };

    function send_axios() {
        // let firstFile = evt.target.files[0]; // upload the first file only
        // axios.post('/', { hello: 'world' });
        console.log('pre-pre-axios-ing')
        let formData = new FormData();
        var imagefile = document.querySelector('#file');
        formData.append("file", imagefile.files[0]);
        console.log('pre-axios-ing')
    
        axios.post('/', formData, {
            headers: {
            'Content-Type': 'multipart/form-data'
            }
        })    
        .then((response) => {
            console.log('success');
        })
        .catch((err) => {
            console.log('failure');
        });
    }

    function show_hide(show) {
        var all = document.getElementById("all");
        var safe = document.getElementById("safe");
        var unsafe = document.getElementById("unsafe");
        if (show === "all") {
          all.style.display = "block";
          safe.style.display = "none";
          unsafe.style.display = "none";
        } else if (show === "safe") {
            safe.style.display = "block";
            all.style.display = "none";
            unsafe.style.display = "none";
        } else{
            unsafe.style.display = "block";
            all.style.display = "none";
            safe.style.display = "none";
        }
      }
}