

window.onload = function() {

    let imageCapture = document.getElementById("capture_image");
    let imageUpload = document.getElementById("upload_image");
    
    // const axios = require('axios');
    console.log('loaded.');

    // imageCapture.addEventListener('change', function(evt) {
    //     let buttons = document.getElementById("buttons_id");
    //     buttons.style.display = 'none';
    //     console.log('==== inside change event listener')
    //     send_axios(evt);
    // });

    // imageUpload.onchange = function() {
    //     console.log('onchange');
    //     console.log('image received');
    //     // send_axios();
    // };

    imageCapture.onchange = function(evt) {
        console.log('=== inside send axios')
        // axios.post('/', { hello: 'world' });
        console.log('pre-pre-axios-ing')
        let formData = new FormData();

        // var imagefile = document.querySelector('#file');
        // formData.append("file", imagefile.files[0]);

        let firstFile = evt.target.files[0]; // upload the first file only
        formData.append("file", firstFile);

        console.log('pre-axios-ing')
    
        axios.post('/uploadImage', formData, {
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

    // function show_hide(show) {
    //     var all = document.getElementById("all");
    //     var safe = document.getElementById("safe");
    //     var unsafe = document.getElementById("unsafe");
    //     if (show === "all") {
    //       all.style.display = "block";
    //       safe.style.display = "none";
    //       unsafe.style.display = "none";
    //     } else if (show === "safe") {
    //         safe.style.display = "block";
    //         all.style.display = "none";
    //         unsafe.style.display = "none";
    //     } else{
    //         unsafe.style.display = "block";
    //         all.style.display = "none";
    //         safe.style.display = "none";
    //     }
    // }
}