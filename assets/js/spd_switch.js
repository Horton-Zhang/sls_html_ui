function  spd_switch(element, address) {
    fetch(address, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ value: element.getAttribute('value') }),
    })
        .then(data => {
            console.log('Value:', value);
            console.log('Response data:', data);
    })
}
