// from chatGPT so ...

const express = require('express');
const path = require('path')

const app = express();
const port = process.env.PORT || 8123; // use the port provided by the environment

// serve static files from the public_html directory
app.use(express.static(path.join(__dirname, 'public_html')));

// serve 'event_files' directory
app.use('/event_files', express.static(path.join(__dirname, 'event_files')));

// define routes
app.get('/', (req, res) => {
	res.sendFile(path.join(__dirname, 'public_html', 'index.html'));
});

//start the server
app.listen(port, () => {
	console.log('Server is listening on port ${PORT}');
});




