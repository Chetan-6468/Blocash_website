const crypto = require('crypto');

const message = "b40eda4711bfaff62d41b38c8a0444a2ae5ee1f14a9a6b4d800c16916fc80096";

// Generate a key pair
const { privateKey, publicKey } = crypto.generateKeyPairSync('rsa', {
    modulusLength: 2048,
    publicKeyEncoding: {
        type: 'spki',
        format: 'pem'
    },
    privateKeyEncoding: {
        type: 'pkcs8',
        format: 'pem'
    }
});

// Sign the message with the private key to generate a digital signature
const sign = crypto.createSign('SHA256');
sign.update(message);
sign.end();
const signature = sign.sign(privateKey, 'hex');

console.log("Digital signature: " + signature);
console.log("Public key: " + publicKey);
console.log("Private key: " + privateKey);
