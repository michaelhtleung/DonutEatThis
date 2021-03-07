


window.onload = function() {
    var ingredients = null;

    let page1 = document.getElementById("page1");
    let page2 = document.getElementById("page2");
    let page3 = document.getElementById("page3");
    page1.style.display = 'initial';
    page2.style.display = 'none';
    page3.style.display = 'none';

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
            ingredients = response.data
            page1.style.display = 'none';
            page2.style.display = 'initial';
            page3.style.display = 'none';

            let parent = document.getElementById("all");

            // populate page 2
            // var title = document.createElement("div");
            // title.classList.add("header");

            var items_tag = document.createElement("div");
            items_tag.classList.add("items");
            parent.appendChild(items_tag)

            for (var i = 0; i < ingredients.length; i++){
                thing = ingredients[i]
                var item_tag = document.createElement("div");
                item_tag.classList.add("item");
                items_tag.appendChild(item_tag)

                var p = document.createElement("div");
                var node = document.createTextNode(thing[i].synonym);
                p.appendChild(node)
                item_tag.appendChild(p)

                var b = document.createElement("box-icon");
                if (thing.score >= 0) {
                    b.setAttribute("name", "sad");
                    b.setAttribute("color", "#75cbac");
                } else {
                    b.setAttribute("name", "happy");
                    b.setAttribute("color", "#ff8f8f");
                }
                item_tag.appendChild(b)
            }
            

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