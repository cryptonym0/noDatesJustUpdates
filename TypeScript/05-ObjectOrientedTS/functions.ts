/***********************************************************
 * Optional Parameters, will return undefines in strict mode
 ***********************************************************/
function greet(name: string, language: string = "", exclamationMark?: string) {
    if(language === "en"){
       return `Hello ${name}${exclamationMark}`;
    } else if(language === "fr"){
       return `Bonjour ${name}${exclamationMark}`;
    }else if(language ==="es"){
       return `Hola ${name}${exclamationMark}`;
    }else{
        return `Yo, ${name}${exclamationMark}`;
    }
}

console.log(greet("John"));
console.log(greet("Sydney", "es"));
console.log(greet("Phillip", "fr", "!"));
// Yo, Johnundefined
// Hola Sydneyundefined
// Bonjour Phillip!
