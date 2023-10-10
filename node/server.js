const http = require('http')
const fs = require('fs')
const _ = require('lodash')

const server = http.createServer((req, res) => {
    // console.log(req.url, req.method);

    const test = _.once(() => console.log('test'))

    test()
    test()

    res.setHeader('Content-Type', 'text/html')

    let path = './views/'

    switch (req.url)
    {
        case '/': 
            path += 'index.html'
            res.statusCode = 200
            break

        case '/about':
            path += 'about.html'
            res.statusCode = 200
            break
        
        case '/about-us':
            res.setHeader('Location', '/about')
            res.statusCode = 301
            break
        
        default: 
            path += '404.html'
            res.statusCode = 404
            break
    }

    // read html
    fs.readFile(path, (err, data) => {
        if(err)
        {
            console.log('error reading the file')
            res.end()
        }
        else{
            // res.write(data);
            res.end(data)
        }
    })
})

server.listen(3000, 'localhost', () => {
    console.log('listening on port 3000');
})