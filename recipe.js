const fs = require('fs')
 
fs.readFile('recipe.txt', (err, data) => {
    if (err) throw err;
 
    document.write(data.toString());
})