import ex from 'express';
import { fileURLToPath } from 'url';
import path from 'path';

// Importa el archivo db_uniminuto.js 
import './src/db_uniminuto.js';

const app = ex();
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

app.use(ex.static("build"));
app.use(ex.json());
app.use(ex.urlencoded({ extended: true })); 

app.listen(8080, function() {
    console.log("Servidor en línea");
});

app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname, "build", "index.html")); 
});

app.get('/home', function(req, res) {
    res.sendFile(path.join(__dirname, "build", "index.html")); 
});

app.get('/actividades', function(req, res) {
    res.sendFile(path.join(__dirname, "build", "index.html")); 
});
app.post("/insertar_tarea", (req, res) => {
    console.log(req.body)
    const { documento, nombres, tarea, horas } = req.body;
    console.log(documento, nombres, tarea, horas);

});

