const fs = require('fs');

//reading files
// fs.readFile('./files/message.txt', (err, data) => {
//     if(err)
//     {
//         console.log(err);
//     }
//     console.log(data.toString());
// })

//writing files
// const path = './files/message.txt' 
// const path2 = './files/message2.txt'

// fs.writeFile(path, 'hello YNS!', (data) => {
//     fs.readFile(path, (err, data) => {
//         console.log(`file written with ${data}`);
//     })
// })

// fs.writeFile('./files/message2.txt', 'hello bitch!', (data) => {
//     fs.readFile(path2, (err, data) => {
//         console.log(`file written with ${data}`);
//     })
// })

//directories
// const path = './test-folder'
// if(! fs.existsSync(path)){
//     fs.mkdir(path, (err) => {
//         if (err) {
//             console.log(err);
//         }
//         else{
//             console.log('folder created');
//         }
//     })
// }
// else{
//     fs.rmdir(path, (err) => {
//         if (err) {
//             console.log(err);
//         }
//         else{
//             console.log('folder deleted');
//         }
//     })
// }


//deleting files
const path = './files/deleteme.txt'
fs.writeFile(path, 'hello delete me', (err, data) => {
    if(err)
    {
        console.log(err)
    }
    else{
        console.log('file created');
    }
})

if(fs.existsSync(path))
{
    fs.unlink(path, (err) => {
        if(err){
            console.log(err);
        }
        else{
            console.log('file deleted');
        }
    })
}

/*
    fs.readfile
    fs.writeFile
    fs.existsSync
    fs.mkdir
    fs.rmdir
*/