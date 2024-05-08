import Mysql from 'mysql';


const conexion = Mysql.createConnection({
    host: "dbprueba.c3c8cswy2juv.us-west-2.rds.amazonaws.com",
    database: "act_uniminuto",
    user: "admin",
    password: "12345678"
});

conexion.connect(function (error) {
    if (error) {
        console.log("Error al conectar a la base de datos: " + error);
    } else {
        console.log("Conexión exitosa a la base de datos");

        // Realiza la consulta una vez que la conexión esté establecida
        conexion.query('SELECT * FROM Tareas', function (error, resultados, campos) {
            if (error) {
                console.log("Error al ejecutar la consulta: " + error);
            } else {
                console.log("Resultados de la consulta:");
                console.log(resultados); // Imprime los resultados de la consulta
            }
            
            // Cierra la conexión después de realizar la consulta
            conexion.end();
        });
    }
});