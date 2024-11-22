function generateSecurePassword(length, includeLowercase, includeUppercase, includeNumbers, includeSymbols) {
    const lowercaseChars = "abcdefghijklmnopqrstuvwxyz";
    const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const numberChars = "0123456789";
    const symbolChars = "!@#$%^&*()-_=+";

    let allowedChars = "";
    let password = "";

    if (includeLowercase) allowedChars += lowercaseChars;
    if (includeUppercase) allowedChars += uppercaseChars;
    if (includeNumbers) allowedChars += numberChars;
    if (includeSymbols) allowedChars += symbolChars;

    if (allowedChars.length === 0) {
        alert("Please select at least one character type!");
        return "";
    }

    const cryptoObj = window.crypto || window.msCrypto;
    const randomValues = new Uint32Array(length);
    cryptoObj.getRandomValues(randomValues);

    for (let i = 0; i < length; i++) {
        const randomIndex = randomValues[i] % allowedChars.length;
        password += allowedChars[randomIndex];
    }

    return password;
}

function generatePassword() {
    const length = parseInt(document.getElementById("length").value);
    const includeLowercase = document.getElementById("includeLowercase").checked;
    const includeUppercase = document.getElementById("includeUppercase").checked;
    const includeNumbers = document.getElementById("includeNumbers").checked;
    const includeSymbols = document.getElementById("includeSymbols").checked;

    const password = generateSecurePassword(length, includeLowercase, includeUppercase, includeNumbers, includeSymbols);
    document.getElementById("passwordDisplay").value = password;
}

function copyPassword() {
    const passwordDisplay = document.getElementById("passwordDisplay");
    passwordDisplay.select();
    passwordDisplay.setSelectionRange(0, 99999); // For mobile devices
    document.execCommand("copy");
    alert("Password copied to clipboard!");
}
