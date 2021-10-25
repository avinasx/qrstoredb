function genQrCode(el){
    let = idVal = document.getElementById("id").value;
    let link = window.location.href+"details?id="+idVal;
    if(idVal===""){
        return true;
    }
    console.log(link);

    let qrContainer = document.getElementById('qrContainer');
    qrContainer.innerHTML =""
    qrContainer.innerHTML ="<a target='_blank' href='"+link+"'>See Details</a>"+"<hr>";

    new QRCode(qrContainer, link.replace(" ","%20"));

    async function postData(url, data ) {
        // Default options are marked with *
        const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        
        headers : { 
            'Content-Type': 'application/json',
            // 'Accept': 'application/json'
            },
        
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data) // body data type must match "Content-Type" header
        });
    return response; // parses JSON response into native JavaScript objects
    }

    postData('/gen', { link: link , fname: idVal})
    .then(data => {
        console.log(data); // JSON data parsed by `data.json()` call
    });
}