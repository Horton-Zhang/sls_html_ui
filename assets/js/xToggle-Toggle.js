

function onToggle(element, address) {
    var value = element.getAttribute('value');
    if (value == "0") {
        element.setAttribute("value","1");
        console.log('element.value:', value);
    } else {
        element.setAttribute("value","0");
        console.log('element.value:', value);
    }
    fetch(address, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ value: value }),
    })
        .then(data => {
            console.log('Value:', value);
            console.log('Response data:', data);
    })
}