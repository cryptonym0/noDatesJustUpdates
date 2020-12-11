function nameMe(name){
    return {
        [name]: {
            message: `My name is ${name}`
        }
    };
}

console.log(nameMe('Steve'));

// [LOG]: {
//     "Steve": {
//         "message": "My name is Steve"
//     }
// }

function nameMeLower(name){
    return {
        [name.toLowerCase()]: {
            message: `My name is ${name}`
        }
    };
}

console.log(nameMeLower('SteVE'));

// [LOG]: {
//     "steve": {
//         "message": "My name is SteVE"
//     }
// }