const fs = require('fs')

const path = './files/longmessage.txt'
const readStream = fs.createReadStream(path, { encoding: 'utf8' })
const writeStream = fs.WriteStream('./files/longmessage2.txt')

// readStream.on('data', (data) => {
//     console.log('------------LOADED-------------');
//     writeStream.write('------------LOADED-------------')
//     writeStream.write(data)
// })

readStream.pipe(writeStream)