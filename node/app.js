const express = require('express')
const morgan = require('morgan')

const app = express()

app.set('view engine', 'ejs')

app.listen(3000, () => console.log('listening to port 3000'))

// app.use(express.static('public'))
// app.use(morgan('dev'))
app.use(express.urlencoded({ extended: true }))

app.get('/', (req, res) => 
{
    const blogs = [
        {  title: 'one piece', snippet: 'lorem ipsum test 1' },
        {  title: 'bleach', snippet: 'lorem ipsum test 2' },
        {  title: 'dragon ball', snippet: 'lorem ipsum test 3' }
    ]

    const products = []

    fetch("https://fakestoreapi.com/products")
        .then((res) => res.json())
        .then((json) => {
            products.value = json
            res.render('index', { pageTitle: 'Home', blogs, products: products.value })
        })
        .catch(err => console.error(err))
})

app.post('/store-product', (req, res) => 
{
    fetch('https://fakestoreapi.com/products', {
        method: 'POST',
        body: req.body
    })
    .then(() => res.redirect('/'))
    .catch(err => console.error(err))

    // const product = new Product(req.body)

    // product.save()
    // .then(res => redirect('/'))
    // .catch(err => console.error(err))

    /*
        if laravel siguro: 
        fetch('/api/products/store', {
            method: 'POST',
            body: req.body
        })
        .then(() => res.redirect('/'))
        .catch(err => console.error(err))
    */
})

app.get('/product/:id', (req, res) => 
{
    fetch(`https://fakestoreapi.com/products/${req.params.id}`)
    .then(res => res.json())
    .then(json => res.render('product', { pageTitle: 'Update Product', product: json }))
    .catch(err => console.error(err))
})

// put dapat to like, app.put
app.post('/update-product/:id', (req, res) => 
{
    fetch(`https://fakestoreapi.com/products/${req.params.id}`, {
        method: 'PUT',
        body: req.body
    })
    .then(() => res.redirect('/'))
    .catch(err => console.error(err))
})

app.delete('/delete-product/:id', (req, res) => 
{
    console.log('deleted!');
    fetch(`https://fakestoreapi.com/products/${req.params.id}`,{
        method: 'DELETE'
    })
    .then(() => res.redirect('/'))
    .catch(err => console.error(err))
})

app.get('/about', (req, res) => {
    // res.sendFile('./views/about.html', { root: __dirname })
    res.render('about', { pageTitle: 'About' })
})

app.get('/create-product', (req, res) => {
    res.render('create-product', { pageTitle: 'Create Product' })
})

// redirect
app.get('/about-us', (req, res) => {
    res.redirect('/about', { pageTitle: 'Create Blog' })
})

// 404
app.use((req, res) => {
    res.status(400).render('404', { pageTitle: 'Not found' })
})