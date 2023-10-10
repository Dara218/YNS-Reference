const express = require('express')
const axios = require('axios')
const redis = require('redis')

const app = express()

const redisClient = redis.createClient(6379);

app.listen(3000, () => console.log('listening to 3000'))

// app.get('/products', (req, res) => 
// {
//     redisClient.get('products', (err, products) => {
//         if(err) console.error(err);
//         if(products)
//         {
//             res.send(products)
//         }
//         else{
//             axios.get("https://fakestoreapi.com/products")
//             .then((results) => {
//                 redisClient.set('products', results.data)
//                 res.send(results.data)
//             })
//             .catch(err => console.error(err))
//         }
//     })
    
// })

app.get('/products', (req, res) => 
{
    redisClient.get('products', (err, products) => 
    {
        if(err) res.send(err)
        if(products) res.send(products)
        else
        {
            axios.get("https://fakestoreapi.com/products")
            .then(products => {
                redisClient.set('products', products.data)
                res.send(products)
            })
            .catch(err => console.error(err))
        }
    })
})